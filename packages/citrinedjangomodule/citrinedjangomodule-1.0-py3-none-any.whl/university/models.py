from django.db import models
from django.utils.text import Truncator
from django.utils import timezone
from django.contrib.auth.models import User
# from user.models import User
from staff.models import Staff


class University(models.Model):
    """ Model to represent the clo in a course """
    name = models.CharField(max_length=300)
    mission = models.CharField(max_length=30000)
    vision = models.CharField(max_length=30000)
    goals = models.CharField(max_length=30000)
    values = models.CharField(max_length=30000)
    phone_number = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    director = models.ForeignKey(Staff,on_delete=models.PROTECT,related_name='director',null=True)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000,null=True)
    code = models.CharField(max_length=1000, null=True)
    country = models.CharField(max_length=1000,null=True)
    postal_code = models.CharField(max_length=1000,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    last_activity = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='university'
    )

    class Meta:
        ordering = [ 'code']
    def save(self, *args, **kwargs):
        if not self.id:
            model_class = self.__class__
            last_instance = model_class.objects.order_by('-id').first()
            self.id = last_instance.id + 1 if last_instance else 1
        super().save(*args, **kwargs)

    def __str__(self):
        truncated_image = Truncator(self.name)
        return truncated_image.chars(300)
