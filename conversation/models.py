from django.db import models
from gallery.models import Gallery


# Create your models here.
class Conversation(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='conversations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='created_messages', on_delete=models.CASCADE)