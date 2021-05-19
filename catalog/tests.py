from django.test import TestCase

# Create your tests here.
from catalog.models import Book, Author

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        author= Author.objects.create(first_name='Big', last_name='Bob')
        author.save()
        Book.objects.create(author=author, title='test')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').help_text
        self.assertEqual(field_label, 'Enter a brief description of the book')


    def test_get_absolute_url_label(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')