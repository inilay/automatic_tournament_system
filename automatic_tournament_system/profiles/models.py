from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from tournaments.models import Tournament


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def get_name(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    tournaments = models.ManyToManyField(Tournament, related_name='profiles')
    user_icon = models.ImageField(upload_to='photos/media/%Y/%m/%d/', default='/user_icon_default.png')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )