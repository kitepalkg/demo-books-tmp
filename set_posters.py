# Paste into `python manage.py shell` on prod, with BOOKS set to the folder of the demo-books-tmp checkout
# (the one import_books read). Dry run unless APPLY = True.
# For each manifest row it finds the imported book (same title and author) and replaces its poster with
# <BOOKS>/<slug>/poster.jpg. The old poster file is not deleted: each line prints its name, so a book can be
# put back with  b = Book.objects.get(pk=ID); b.poster.name = 'OLD NAME'; b.save(update_fields=['poster'])
from pathlib import Path

from django.core.files import File
from django.db import transaction

from books.management.commands.import_books import read_manifest
from books.models import Book

BOOKS = Path('/path/to/demo-books-tmp')  # set this
APPLY = False

rows = read_manifest(BOOKS / 'manifest.md')
plan = []
for row in rows:
    poster = BOOKS / row['slug'] / 'poster.jpg'
    books = list(Book.objects.filter(title=row['title'], author__name=row['author']))
    assert poster.is_file(), f'{row["slug"]}: no poster.jpg'
    assert len(books) == 1, f'{row["slug"]}: {len(books)} books with that title and author'
    plan.append((books[0], poster))
    print(books[0].pk, row['slug'], 'old:', books[0].poster.name)
print(len(plan), 'books')

if APPLY:
    with transaction.atomic():
        for book, poster in plan:
            with poster.open('rb') as f:
                book.poster.save(f'{poster.parent.name}.jpg', File(f), save=False)
            book.save(update_fields=['poster'])
            print(book.pk, 'new:', book.poster.name)
    print('done')
