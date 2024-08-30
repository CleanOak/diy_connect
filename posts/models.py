from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Post model, related to 'owner' of an instance
    """
    image_filter_choices = [
        ('trees', 'Trees'),
        ('animals', 'Animals'),
        ('mountains', 'Mountains'),
        ('water', 'Water'),
        ('places', 'Places'),
        ('cities', 'Cities')
    ]


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', 
    default='https://res.cloudinary.com/dojf2qfyl/image/upload/v1724965652/no_image_mvrwpr.avif',
    blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f'{self.id} {self.title}'

