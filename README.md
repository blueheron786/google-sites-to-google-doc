# 📝 Google Sites to Google Doc

**Classic Google Sites** used to be awesome. Now ... not so much.  

This tool helps you export your Classic Google Site into a `.docx` document, with:

- ✅ One page per site section
- ✅ Headers preserved
- ✅ Bulleted lists retained
- ✅ Easily copy-pasteable into Google Docs

---

## 🚀 Usage

1. **Set the site suffix**  
   Open `main.py` and set the `SITE_SUFFIX` value to match your Classic Google Site URL:  
   ```python
   SITE_SUFFIX = "yoursite"
   # If your site is https://sites.google.com/site/yoursite/
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the converter**  
   ```bash
   python main.py
   ```

4. **Open and convert**  
   - Open the generated `yoursite.docx` in an office suite (e.g., **LibreOffice**, **Word**)
   - Insert a Table of Contents on the first page
   - Save it and upload to **Google Docs**
   - Use `File > Save as Google Docs`

---

## ⚠️ Limitations

- 🧭 **No auto-generated ToC**: You'll need to insert a table of contents manually using a Word processor (LibreOffice, Word, etc.) before uploading to Google Docs.
- 📄 **Limited formatting**: Only titles, paragraphs, and bullet lists are extracted. No images, sub-headings, or fancy styling. Modify the script if you need richer formatting.
- 🔍 **Classic Sites only**: This script only supports Classic Google Sites (i.e., URLs like `sites.google.com/site/...`). It won’t work with the newer Google Sites format.

---

## 🙌 Contributions

Pull requests welcome!  

If you know how to:
- Programmatically generate a proper ToC that Google Docs recognizes
- Handle images or sub-headings
- Improve site traversal or formatting fidelity

... feel free to open an issue or submit a PR!
