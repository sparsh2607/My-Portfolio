from django.db import models
 
# Models can be expanded later for dynamic project management via admin
class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    year = models.CharField(max_length=4)
    tags = models.CharField(max_length=300, help_text='Comma-separated tags')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['order', '-created_at']
 
    def __str__(self):
        return self.title
 
    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]