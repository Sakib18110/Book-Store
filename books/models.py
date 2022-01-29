from django.db import models

# Create your models here.
class books(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    order_date=models.DateField()

    def __str__(self):
        return self.book_name


class order_book(models.Model):
    book_name=models.CharField(max_length=100)
    order_date=models.DateTimeField()

    class Meta:
        ordering=['order_date']

    def __str__(self):
        return self.book_name