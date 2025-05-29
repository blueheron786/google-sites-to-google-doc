import re
from collections import deque
from time import perf_counter
from urllib.parse import urljoin
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_BREAK
from requests_html import HTMLSession

# Configuration
SITE_SUFFIX = "SITE_SUFFIX_HERE"  # Replace with the actual site suffix
OUTPUT_FILE_NAME = f"{SITE_SUFFIX}.docx"
BASE_URL = f"https://sites.google.com/site/{SITE_SUFFIX}"

class SiteToDocxConverter:
    def __init__(self):
        self.session = HTMLSession()
        self.visited = set()
        self.to_visit = deque([BASE_URL])
        self.pages = []
        self.start_time = perf_counter()

    def normalize_url(self, href):
        return urljoin("https://sites.google.com/", href).replace("//", "/").replace("https:/", "https://")

    def clean_title(self, title):
        cleaned = re.sub(r"[^\w\s-]", "", title).strip()
        return cleaned or "Untitled"

    def extract_content(self, url):
        try:
            # print(f"Processing: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            links = [a.attrs["href"] for a in response.html.find("a[href]") 
                    if a.attrs.get("href", "").startswith(f"/site/{SITE_SUFFIX}/")]
            
            for link in links:
                normalized = self.normalize_url(link)
                if normalized not in self.visited:
                    self.to_visit.append(normalized)

            if header := response.html.find("header", first=True):
                header.element.drop_tree()

            if not (content := response.html.find("body", first=True)):
                print(f"Skipped (no content): {url}")
                return

            blocks = []
            for element in content.element.iter():
                text = element.text_content().strip()
                if not text:
                    continue
                    
                if element.tag == "p" and not any(p.tag == "li" for p in element.iterancestors()):
                    blocks.append(("p", text))
                elif element.tag == "li":
                    blocks.append(("li", text))

            if not blocks:
                print(f"Skipped (no valid content): {url}")
                return

            title = (response.html.find("h1", first=True) or {}).text or url
            self.pages.append((url, title.strip(), blocks))
            print(f"Added: {title}")

        except Exception as e:
            print(f"Failed: {url} - {str(e)}")

    def create_document(self):
        print("\nCreating document...")
        doc = Document()
        
        # Configure heading style
        heading_style = doc.styles["Heading 1"]
        heading_style.font.size = Pt(20)
        heading_style.paragraph_format.keep_with_next = True
        heading_style.paragraph_format.space_before = Pt(24)
        heading_style.paragraph_format.space_after = Pt(12)

        # Add content sorted by title
        self.pages.sort(key=lambda x: x[1])
        
        for i, (url, title, blocks) in enumerate(self.pages):
            doc.add_paragraph(self.clean_title(title), style="Heading 1")
            
            for block_type, text in blocks:
                if block_type == "li":
                    doc.add_paragraph(text, style="List Bullet")
                else:
                    doc.add_paragraph(text)
            
            if i < len(self.pages) - 1:
                doc.add_page_break()

        doc.save(OUTPUT_FILE_NAME)
        print(f"Document saved: {OUTPUT_FILE_NAME}")

    def run(self):
        print(f"Crawling site: {BASE_URL}")
        
        while self.to_visit:
            url = self.to_visit.popleft()
            if url not in self.visited:
                self.visited.add(url)
                self.extract_content(url)
        
        self.create_document()
        
        runtime = perf_counter() - self.start_time
        print(f"\nCompleted in {runtime:.1f} seconds")
        print(f"Pages processed: {len(self.pages)}")

if __name__ == "__main__":
    converter = SiteToDocxConverter()
    converter.run()