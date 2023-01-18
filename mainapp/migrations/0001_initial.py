# Generated by Django 3.2.7 on 2023-01-13 05:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=127, verbose_name='номер телефона')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=127, verbose_name='пол')),
                ('role', models.CharField(choices=[('Orginizer', 'Orginizer'), ('Participant', 'Participant'), ('Other', 'Other'), ('Admin', 'Admin')], default='Participant', max_length=127, verbose_name='роль')),
                ('date_birthday', models.DateField(verbose_name='Дата рождения')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Useradmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_checked', models.PositiveBigIntegerField(default=0, verbose_name='Проверенно турниров')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_admin', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_play', models.PositiveBigIntegerField(default=0, verbose_name='сыгранно турнира')),
                ('tournament_won', models.PositiveIntegerField(default=0, verbose_name='выйгранно турниров')),
                ('type_sport', models.CharField(blank=True, max_length=127, null=True, verbose_name='тип спорта')),
                ('experience', models.PositiveBigIntegerField(default=0, verbose_name='Опыт')),
                ('rank', models.CharField(blank=True, max_length=127, null=True, verbose_name='Уровень спортсмена')),
                ('club', models.CharField(blank=True, max_length=127, null=True, verbose_name='Клуб')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_amount', models.PositiveBigIntegerField(default=0, verbose_name='Количество сделанных турниров ')),
                ('club', models.CharField(max_length=127, verbose_name='Клуб')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]