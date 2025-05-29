# Google Sites to Google Doc

Google Sites used to be awesome. Now, not so much.

Export it as a Google Doc instead, with one page per site-page, preserving headings (title) and lists.

# Usage

Open up `main.py` and set a value for `SITE_SUFFIX`.

```
python install -r requirements.txt
python main.py
```

This will generate a `site_suffix_here.docx` file.

- Open it in the Office suite of your choice (I prefer Libre Office)
- Insert a table of contents on the first page
- Upload it to Google Docs
- File > Save as Google Docs

You're done! You can tweak the final doc, ToC, etc. as you wish

# Limitations

Due to the complexity of uploading something that Google Docs understands as a dynamic, updatable table of contents, that's not included. You still need some sort of office package, like Libre Office, to generate the table of contents before you upload it. If someone knows how to fix this, PRs are more than welcome!

Also, the converter doesn't save anything except the title, list items, and texts; you need to modify the source if you use, say, sub-headings, images, etc. and wish to preserve them.