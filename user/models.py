from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    
 

class Discussion(models.Model): 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_discussions')
    message = models.CharField(max_length=100)
    liker = models.ManyToManyField(Profile, blank=True)
    likes = models.PositiveBigIntegerField(default=0)
    replies = models.ManyToManyField('Discussion', blank=True, related_name='discussion_replies')

    def get_all_replies(self): 
        return len(self.replies.all())
    
    def __str__(self): 
        return f"{self.user.user.username} | {self.message}"