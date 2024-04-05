# Generated by Django 4.2.7 on 2024-03-30 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_firsttodo_create_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firsttodo',
            name='create_at',
        ),
        migrations.AddField(
            model_name='firsttodo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
