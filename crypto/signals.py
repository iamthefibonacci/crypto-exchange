from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


User = get_user_model()


@receiver(post_save, sender=User)
def create_token_for_user(sender, **kwargs) -> None:
    instance = kwargs.pop('instance')
    created = kwargs.pop('created')

    if created:
        Token.objects.create(user=instance)
