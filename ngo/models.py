from django.db import models
from django.core.validators import RegexValidator

class NGO(models.Model):
    name = models.CharField(max_length=200, unique=True)
    registration_number = models.CharField(
        max_length=50,
        unique=True,
        validators=[RegexValidator(r'^[A-Z0-9/-]+$')]
    )
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')]
    )
    website = models.URLField(blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "NGO"
        verbose_name_plural = "NGOs"
        ordering = ['name']