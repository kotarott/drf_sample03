from django.db import models

# Create your models here.
class Quote(models.Model):
    quote_author = models.CharField(max_length=50)
    quote_body = models.CharField(max_length=200)
    context = models.TextField()
    source = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_body
