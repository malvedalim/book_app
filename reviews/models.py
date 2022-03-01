from django.db import models
from django.contrib import auth




class Publisher(models.Model):
    """The firm that publishes the book"""
    name = models.CharField(
        max_length=50,
        help_text="The name of the publisher"
    )
    website = models.URLField(
        help_text="The publisher's email"
    )
    email = models.EmailField(
        help_text="The email of the publisher"
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    """The details about the book"""
    title = models.CharField (
        max_length=70,
        help_text="The title of the book"
    )
    publication_date = models.DateField(
        verbose_name="Date of the book"
    )
    isbn = models.CharField(
        max_length=20,
        verbose_name="ISBN number of the book"
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete= models.CASCADE
    )
    contributor = models.ManyToManyField(
        'Contributor',
        through="BookContributor"
    )
    def __str__(self):
        return self.title

class Contributor(models.Model):
    """A contributor to the book e.g author,publisher,editor, co-author"""
    first_name = models.CharField(
        max_length=50,
        help_text="Contributor's first name"
    )
    last_name = models.CharField (
        max_length=60,
        help_text="Contributor's last name."

    )
    email = models.EmailField (
        help_text="Email of the contributor."
    )

    def __str__(self):
        return self.first_name

class BookContributor(models.Model):
    """An intermediary table to establish relationships to Book and Contributor Table"""
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", 'Author'
        CO_AUTHOR = "CO-AUTHOR" , "Co-author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey (
        Book,
        on_delete=models.CASCADE
    )
    contributor = models.ForeignKey (
        Contributor, on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name="The role of the contributor in the book.",
        choices=ContributionRole.choices,
        max_length=20
    )
class Review(models.Model):
    content = models.TextField(
        help_text="The text of the review"
    )
    rating = models.IntegerField(
        help_text="The rating of the reviewer gives to the book."
    )
    date_created= models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the review was created"
    )
    date_edited = models.DateTimeField(
        null=True,
        help_text="The date and time the reviews was edited."
    )
    creator = models.ForeignKey(
        #Get the user that logs in using Djangos auth module
        auth.get_user_model(),
        on_delete=models.CASCADE,
        help_text="The user that made the review"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        help_text="The book that is being reviewed"
    )