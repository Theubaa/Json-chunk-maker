# 🧩 JSON Chunk Splitter

A simple and powerful web tool to split large JSON files into smaller chunks of **1MB or less**. Built with [Streamlit](https://streamlit.io), this tool makes it easy to upload a `.json` file, split it, and download the result as a zipped folder of chunked JSON files — all from your browser!

---

## 🚀 Features

- 📤 Upload any large `.json` file (must be a list/array at the root)
- 🧠 Automatically splits the file into multiple files, each ≤ 1MB
- 📦 Download all chunks in a single `.zip` archive
- ⚡ Fast, accurate, and super easy to use
- 🧱 Built with Python + Streamlit

---

## 🔧 Requirements

- Python 3.8+
- Streamlit

Install dependencies:

```bash
pip install streamlit
▶️ Run the App
bash
Copy
Edit
streamlit run json_chunker_app.py
Then open the local link provided in your terminal (usually http://localhost:8501).

🖼️ Screenshot
<img src="https://github.com/user-attachments/assets/274f2f0f-8011-4da2-97e7-b268253948af">
## 🖼️ Screenshot

![Screenshot](https://raw.githubusercontent.com/yourusername/yourrepo/main/assets/screenshot.png)

📂 Input Format
Uploaded JSON must be a top-level array like:

json
Copy
Edit
[
  {"id": 1, "name": "Item A"},
  {"id": 2, "name": "Item B"},
  ...
]



📁 Output
The tool creates multiple files like chunk_1.json, chunk_2.json, etc.

Each file is ≤ 1MB in size.

Files are compressed into json_chunks.zip for download.

🧑‍💻 Author
Made by The_ubaa

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

yaml


---

### ✅ Instructions

1. Replace `![JSON Chunk Splitter UI](...)` with a real screenshot if you have one.
2. Update `[Your Name](...)` with your GitHub link.
3. Add a `LICENSE` file if needed (MIT is common and safe).

Let me know if you want a demo GIF or badge integrations!
