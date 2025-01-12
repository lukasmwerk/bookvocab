# import pymupdf4llm

# md_text = pymupdf4llm.to_markdown("alejo-carpentier-los-pasos-perdidos.pdf")

# # now work with the markdown text, e.g. store as a UTF8-encoded file
# import pathlib
# pathlib.Path("output.md").write_bytes(md_text.encode())

import pymupdf # imports the pymupdf library
doc = pymupdf.open("alejo-carpentier-los-pasos-perdidos.pdf") # open a document
outline = doc.outline

import pathlib


def walk_outline(outline: pymupdf.Outline):
    if outline is None:
        return
    print(outline.title)

    end_page = doc.page_count
    if outline.down is not None:
        end_page = outline.down.page
    elif outline.next is not None:
        end_page = outline.next.page

    print(outline.page, end_page)

    text = chr(12).join([doc.get_page_text(i) for i in range(outline.page, end_page)])
    print(text[0:20])
    print("\n\n\n")
    with open("output.txt", "a") as f:
        f.write("===============================\n" + text + "\n")

    walk_outline(outline.down)
    walk_outline(outline.next)

open('output.txt', 'w').close()
walk_outline(outline)
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