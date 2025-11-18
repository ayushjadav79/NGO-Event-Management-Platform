from django.db import models
from ngo.models import NGO

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='events')
    poster = models.ImageField(upload_to='event_posters/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.ngo.name}"

    class Meta:
        ordering = ['-date_time']