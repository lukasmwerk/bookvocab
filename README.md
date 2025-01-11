# bookvocab

Generate chapter-by-chapter _prefaces_: short preambles that contain vocab, lingual/cultural context and any other helpful information to the reader prior to starting a chapter.

This tool is intended for people learning a foreign language, by reading books and documents in that language.

The intended use is for readers to read through a _preface_ before starting a chapter, and get vocabulary or context that they will need throughout the chapter.

## How to use

Can't use it yet because I'm still working on it.

## Roadmap

_This outlines a potential roadmap for expanding on this mini-project._

Generation

1.  Support full vocab lists on generated dictionaries.
2.  Add a display mechanism and export function.
3.  Support sections (Important, Advanced, Common, Seen Before).
4.  Support phrases and concepts.
5.  Add Prioritization (recognizing importance of items, based on modelling, frequency, location, has the reader encountered the concept before).
6.  Add GUI or web app, allowing easy import and export, print.
7.  Add support for scanned documents.
8.  Export/Abstract modelling for use in other contexts

Language Support

1.  Spanish Language support - end of road if no continued development.
2.  Add German, Dutch, Italian, French, common Latin script languages.
3.  Add Cyrillic, Chinese, Arabic, Japanese, Hangul, Devanagari, Bengali.

Technological Dependencies

*   PDF parsers, both through image text extraction, document outline parsing, chapter identification and binary data parsing.
*   Prioritization and classifier models, for consolidating priority information and grouping into generated sections.
*   Translation models, for identifying languages and translating words and phrases.
*   Lookup mechanisms, to identify and query on lingual and cultural concepts.
*   File builders and exporters.
*   Identification modeling for spoilers, and words or phrases that could spoil plot.
*   Optimization and streaming mechanisms - raw speed is not a high priority, anything under 1 minute for a 300 page book is acceptable, progressive rendering and exposure to early chapters quickly is also possible.
*   Web server infrastructure and implementation in the case of a web app.

## Documentation

Implementation details and documentation lives next to the code in this repository, while documentation for higher level concepts and use lives in the wiki tab.