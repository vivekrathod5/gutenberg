from django.db import models
from django.core.validators import MinValueValidator



class Author(models.Model):
    class Meta():
        db_table = 'books_author'
    birth_year = models.SmallIntegerField(null=True, blank=True)
    death_year = models.SmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)


class Books(models.Model):
    class Meta():
        db_table = 'books_book'
    download_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, null=True, blank=True)


class BookAuthors(models.Model):
    class Meta():
        db_table = 'books_book_authors'
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Bookshelves(models.Model):
    class Meta():
        db_table = 'books_book_bookshelves'
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey('Bookshelf', on_delete=models.CASCADE)


class BookLanguages(models.Model):
    class Meta():
        db_table = 'books_book_languages'
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)


class BookSubjects(models.Model):
    class Meta():
        db_table = 'books_book_subjects'
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


class Bookshelf(models.Model):
    class Meta():
        db_table = 'books_bookshelf'
    name = models.CharField(max_length=64)


class Format(models.Model):
    class Meta():
        db_table = 'books_format'
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)


class Language(models.Model):
    class Meta():
        db_table = 'books_language'
    code = models.CharField(max_length=4)


class Subject(models.Model):
    class Meta():
        db_table = 'books_subject'
    name = models.CharField(max_length=256)
