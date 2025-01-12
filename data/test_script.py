# import pymupdf4llm

# md_text = pymupdf4llm.to_markdown("alejo-carpentier-los-pasos-perdidos.pdf")

# # now work with the markdown text, e.g. store as a UTF8-encoded file
# import pathlib
# pathlib.Path("output.md").write_bytes(md_text.encode())

import pymupdf # imports the pymupdf library
from collections import Counter
doc = pymupdf.open("alejo-carpentier-los-pasos-perdidos.pdf") # open a document
outline = doc.outline

import pathlib
import re

class Chapter:
    def __init__(self, title, start, stop):
        self.title = title
        self.page_start = start
        self.page_stop = stop
        self.dictionary = Counter()
    def process(self, pymudoc: pymupdf.Document, output_doc: str):
        for page in pymudoc.pages(self.page_start, self.page_stop, 1):
            for word in re.split(r"\s*[,!? ]\s*", page.get_text("text")):
                # print(word)
                self.dictionary.update([word])   
        print(self.dictionary.most_common()[:-50:-1])

class Document:
    def __init__(self, pymudoc: pymupdf.Document):
        self.pymudoc = pymudoc
        self.chapters = []

    def add_chapter(self, title: str, start_page: int, end_page: int):
        self.chapters.append(Chapter(title, start_page, end_page))
    
    def process_chapter(self, title, start, stop):
        chapter = Chapter(title, start, stop)
        chapter.process(self.pymudoc, output_doc)
    
    def process_pdf(self, output_doc):
        self.output_doc = output_doc
        self.walk_outline(outline)

    def walk_outline(self, outline: pymupdf.Outline):
        if outline is None:
            return
    
        end_page = doc.page_count
        if outline.down is not None:
            end_page = outline.down.page
        elif outline.next is not None:
            end_page = outline.next.page
        
        self.process_chapter(outline.title, outline.page, end_page)

        self.walk_outline(outline.down)
        self.walk_outline(outline.next)


document = Document(doc)
output_doc = 'output.txt'
open(output_doc, 'w').close()
document.process_pdf(output_doc)


    



# while outline.next != None:
#     while outline.down != None:
#         print(outline.page)
#         outline = outline.down

#     outline = outline.next




# count = 0

# with open("output.txt", "a") as f:
#     for page in doc: # iterate the document pages
#         # if count > 3000:
#         #     break
#         # count += 1
#         text = page.get_text() # get plain text encoded as UTF-8
#         print(text, file=f)