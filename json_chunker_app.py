import json
import os
import zipfile
import tempfile

import streamlit as st

MAX_CHUNK_SIZE = 1024 * 1024  # 1MB


def split_json_to_chunks(json_data, max_size=MAX_CHUNK_SIZE):
    chunks = []
    current_chunk = []
    current_size = 2  # For '[' and ']'

    for item in json_data:
        item_str = json.dumps(item, ensure_ascii=False, separators=(",", ":"))
        item_size = len(item_str.encode("utf-8")) + 2  # Add for comma, newline

        if current_size + item_size > max_size:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
                current_size = 2

        current_chunk.append(item)
        current_size += item_size

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def create_zip_from_chunks(chunks):
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "json_chunks.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for idx, chunk in enumerate(chunks):
            chunk_filename = f"chunk_{idx + 1}.json"
            chunk_path = os.path.join(temp_dir, chunk_filename)
            with open(chunk_path, "w", encoding="utf-8") as f:
                json.dump(chunk, f, ensure_ascii=False, indent=2)
            zipf.write(chunk_path, arcname=chunk_filename)

    return zip_path


# -------------- Streamlit UI ------------------

st.set_page_config(page_title="JSON Chunk Splitter", page_icon="🧩")
st.title("🧩 JSON Chunk Splitter Tool")

st.markdown("""
Upload a **JSON file** that is an array of objects (e.g. `[{"a":1}, {"b":2}]`)  
This tool will split it into chunks of **≤ 1MB** each and give you a ZIP to download.
""")

uploaded_file = st.file_uploader("📤 Upload JSON file", type=["json"])

if uploaded_file is not None:
    try:
        json_data = json.load(uploaded_file)

        if not isinstance(json_data, list):
            st.error("❌ Uploaded JSON must be a list/array at the top level.")
        else:
            st.success(f"✅ Loaded JSON with {len(json_data)} items.")
            if st.button("🚀 Convert & Split"):
                with st.spinner("Processing and splitting into chunks..."):
                    chunks = split_json_to_chunks(json_data)
                    zip_path = create_zip_from_chunks(chunks)
                    with open(zip_path, "rb") as f:
                        st.success(f"✅ Conversion complete! {len(chunks)} chunk files created.")
                        st.download_button(
                            label="📥 Download ZIP of Chunks",
                            data=f,
                            file_name="json_chunks.zip",
                            mime="application/zip",
                        )
    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
