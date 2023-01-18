from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver

from django.db.models.signals import post_save

from mainapp.config import *


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=127, verbose_name='номер телефона')
    gender = models.CharField(
        max_length=127,verbose_name='пол',
        choices=GENDER, default=MALE
    )
    role= models.CharField(
        max_length=127,verbose_name='роль',
        choices=ROLE, default=PARTICIPANT
        
    )
    date_birthday = models.DateField(
        verbose_name='Дата рождения',null=True,blank=True
    )

    def __str__(self) -> str:
        return self.username

class Organizer(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,related_name='organizer',verbose_name='Пользователь'
    )
    tournament_amount = models.PositiveBigIntegerField(
        default=0,verbose_name='Количество сделанных турниров '
    )
    club = models.CharField(max_length=127,verbose_name='Клуб')

    def __str__(self) -> str:
        return self.user.username

class Participant(models.Model):
    user= models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='participant',verbose_name='Пользователи',
        null=True,blank=True
    )
    tournament_play = models.PositiveBigIntegerField(
        default=0,verbose_name='сыгранно турнира'
    )
    tournament_won = models.PositiveIntegerField(
        default=0, verbose_name='выйгранно турниров'
    )
    type_sport = models.CharField(
        max_length=127, verbose_name='тип спорта',
        null=True, blank=True)
    experience = models.PositiveBigIntegerField(
        default=0, verbose_name='Опыт'
    )
    rank = models.CharField(
        max_length=127,verbose_name='Уровень спортсмена',
        null=True, blank=True
    )
    club = models.CharField(
        max_length=127,verbose_name='Клуб',
        null=True, blank=True
    )
    def __str__(self) -> str:
        return self.user.username 

class UserAdmin(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,related_name='user_admin',verbose_name='Пользователь')
    tournament_checked = models.PositiveBigIntegerField(
        default=0,verbose_name='Проверенно турниров'
    )

    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=User)
def create_connected_models(sender, instance, created, **kwargs):
    if created:
        print()
        if instance.role == PARTICIPANT:
            Participant.objects.create(user=instance)
        elif instance.role == ORGINIZER:
            Organizer.objects.create(user=instance)
        elif instance.role == ADMIN:
            UserAdmin.objects.create(user=instance)


    


