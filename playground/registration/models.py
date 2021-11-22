from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/'+ filename

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    link= models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']
##Crear senales

##Este decorador es para que se haga automaticamente, estas señales puede ser post_save, post_migrate o post_delete depende de para lo que se use
@receiver(post_save, sender=User)
#Se encargara de que el perfil exista
def ensure_profile_exists(sender,instance,**kwargs):
    if kwargs.get('created', False):#Si existe entonces es que la instancia se acaba de crear
        Profile.objects.get_or_create(user=instance)    
        #print("entre a la senal")