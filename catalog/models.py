from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import AbstractUser,BaseUserManager
import uuid

# m1 language model
class Language(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def get_absolute_url(self):
        return reverse('catalog:language-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    
# m2 genre model
class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book Genre "
    )
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catalog:genre-detail',args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="Genre already exists(Case insensitive match)"
            )
        ]

#m3 book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.RESTRICT,null=True)
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book" #help text is what appears in ui form
        )
    isbn=models.CharField('ISBN',max_length=13,
                          unique=True,
                          help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a> ')
    genre = models.ManyToManyField(
        Genre,help_text="Select a genre for this book"
    )
    language = models.ForeignKey('language',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self): #these helper functions are for viewing admin dashboard better,instead of directly calling columns,we use these functions
        return reverse('catalog:book_detail',args=[str(self.id)])
    def display_genre(self):
        return ','.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre' #if not defined it will show function name directly as column header

#m4 bookinstance model
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text="Unique ID for this particular book across")
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved')
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text="Book Availability",
    )
    class Meta:
        ordering = ['due_back']
    def __str__(self) :
        return f'{self.id} ({self.book.title})'
    
#m5 author model
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died',null=True,blank=True)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        return reverse('catalog:author-detail',args=[str(self.id)])
    def __str__(self):
        return f"{self.last_name},{self.first_name}"
    
