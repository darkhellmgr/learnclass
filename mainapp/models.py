from django.db import models

# Create your models here.
IMP_CHOICES = (
    ('Nepal', 'Nepal'),
    ('Bhutan', 'Bhutan'),
    ('Sweden', 'Sweden'),
)


class School(models.Model):
    name = models.CharField(max_length=200, blank=False)
    street_address = models.CharField(max_length=200, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=100, choices=IMP_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
