# import pymupdf4llm

# md_text = pymupdf4llm.to_markdown("alejo-carpentier-los-pasos-perdidos.pdf")

# # now work with the markdown text, e.g. store as a UTF8-encoded file
# import pathlib
# pathlib.Path("output.md").write_bytes(md_text.encode())

import pymupdf # imports the pymupdf library
from collections import Counter
import pathlib
import re
from googletrans import Translator
import asyncio

class Chapter:
    def __init__(self, title, start, stop):
        self.title = title
        self.page_start = start
        self.page_stop = stop
        self.dictionary = Counter()

    async def process(self, pymudoc: pymupdf.Document, translator, chapter_count:int):
        for page in pymudoc.pages(self.page_start, self.page_stop, 1):
            for word in re.split(r"\s*[,!? ]\s*", page.get_text("text")):
                # print(word)
                self.dictionary.update([word])
                 
        first_elements = map(lambda x: x[0], self.dictionary.most_common())  
        translations = await translator.translate(list(first_elements)[::-1], dest='en')

        with open("out"+str(chapter_count)+".txt", 'w') as f:
            for translation in translations:
                if translation.origin != translation.text:
                    print(translation.origin + ":\t"+ translation.text, file=f)

class Document:
    def __init__(self, pymudoc: pymupdf.Document):
        self.pymudoc = pymudoc
        self.chapters = []
        self.chapter_count = 0

    def add_chapter(self, title: str, start_page: int, end_page: int):
        self.chapters.append(Chapter(title, start_page, end_page))
    
    async def process_chapter(self, title, start, stop):
        chapter = Chapter(title, start, stop)
        await chapter.process(self.pymudoc, self.translator, self.chapter_count)
        self.chapter_count += 1
    
    async def process_pdf(self, translator, output_doc):
        self.translator = translator
        self.output_doc = output_doc
        await self.walk_outline(self.pymudoc.outline)

    async def walk_outline(self, outline: pymupdf.Outline):
        if outline is None:
            return
    
        end_page = self.pymudoc.page_count
        if outline.down is not None:
            end_page = outline.down.page
        elif outline.next is not None:
            end_page = outline.next.page
        
        await self.process_chapter(outline.title, outline.page, end_page)

        await self.walk_outline(outline.down)
        await self.walk_outline(outline.next)


async def main():
    translator = Translator()
    doc = pymupdf.open("alejo-carpentier-los-pasos-perdidos.pdf") # open a document
    outline = doc.outline
    document = Document(doc)
    output_doc = 'output.txt'
    open(output_doc, 'w').close()
    await document.process_pdf(translator, output_doc)

if __name__ ==  '__main__':
    loop = asyncio.run(main())
    



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