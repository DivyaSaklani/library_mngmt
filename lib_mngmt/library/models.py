from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import timedelta, date

class Book(models.Model):
    BOOK_TYPE_CHOICES = [
        ('book', 'Book'),
        ('movie', 'Movie'),
    ]
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=50, unique=True)
    book_type = models.CharField(max_length=5, choices=BOOK_TYPE_CHOICES, default='book')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    MEMBERSHIP_DURATION_CHOICES = [
        (6, '6 months'),
        (12, '1 year'),
        (24, '2 years'),
    ]
    duration = models.IntegerField(choices=MEMBERSHIP_DURATION_CHOICES, default=6)

    def __str__(self):
        return f"{self.user.username} - {self.duration} months"

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"Transaction for {self.book.title} by {self.user.username}"
