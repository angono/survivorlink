from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User 
from django.dispatch import receiver  


# Create your models here. 
class Story(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Who is publishing the story.")
    title = models.CharField(max_length=300, help_text="Title of your story.")
    content = models.TextField(blank=True, help_text="Describe the story. This field is optional.")
    is_available = models.BooleanField(default=True, help_text="Is this for everyone.")
    author = models.CharField(max_length=100, blank=True, help_text="Who is the owner of the story. This field is optional.")
    date = models.DateTimeField(auto_now_add=True) 
    video_url = models.CharField(max_length=1000, blank=True)
    # thumbnail = models.CharField(max_length=1000, blank=True)


    class Meta:
        ordering = ['-date',] 
        verbose_name_plural = 'Stories'

    def __str__(self):
        return f"{self.publisher} - {self.title} - {self.date}" 
    
    def get_absolute_url(self):
        return reverse('story:story-detail', kwargs={'pk': self.pk})






