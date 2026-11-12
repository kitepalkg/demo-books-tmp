Temporary: public-domain EPUBs for a one-off import. Will be deleted.

## What is here

61 complete books in Russian (novels, plays, long poems, stories, children's tales) by 20 authors.
Layout: `manifest.md` and `<slug>/<slug>.epub`, as `manage.py import_books <dir>` expects.

## Source and licence

Every book is an export of one page of Russian Wikisource (ru.wikisource.org) made with ws-export
on 2026-11-12. The `source` column of `manifest.md` gives the page. Every author died more than
70 years ago (the latest in 1938); there are no translations. Wikisource publishes these texts as
public domain; the last page of each book is Wikisource's own page about the e-book.

## Changed after the export

- embedded fonts removed (4 MB per book);
- reading-order entries that repeated the same chapter removed (3 books);
- the Wikisource maintenance banner «Источник текста не указан» removed (4 books:
  `lermontov-geroy-nashego-vremeni`, `dostoevsky-idiot`, `dostoevsky-belye-nochi`,
  `saltykov-istoriya-odnogo-goroda`); the text of those four has no stated printed source on Wikisource;
- title and author metadata set to the values of `manifest.md`.

The text of the books is not changed.
