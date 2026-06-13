from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Recipe

@receiver(post_save,sender=Recipe)
def send_recipe_email(sender,instance,created,**kwargs):
    if created and instance.author.email:
        send_mail('Recipe Published Successfully',' Hi ,Your recipe has been published.''Thank you for sharing your delicious recipe with us! Happy Cooking!',None,[instance.author.email],fail_silently=True)
