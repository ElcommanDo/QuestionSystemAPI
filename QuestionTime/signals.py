from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from question.models import Question
from .utils import generate_random_string
@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_text = generate_random_string()
        instance.slug = instance.content + '-' + random_text
