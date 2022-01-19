from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User 
from django.dispatch import receiver  


# Create your models here. 
class Tip(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The author's name.")
    title = models.CharField(max_length=300, help_text="What is the title?.")
    content = models.TextField(help_text="Write the content.")
    is_available = models.BooleanField(default=True, help_text="Is this for everyone.")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date',] 
        verbose_name_plural = 'Tips'

    def __str__(self):
        return f"{self.author} - {self.title} - {self.date}" 
    
    def get_absolute_url(self):
        return reverse('tips:tip-detail', kwargs={'pk': self.pk})






