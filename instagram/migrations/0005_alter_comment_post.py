# Generated by Django 4.2.7 on 2023-11-17 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_alter_post_options_alter_post_photo_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(limit_choices_to={'is_public': True}, on_delete=django.db.models.deletion.CASCADE, to='instagram.post'),
        ),
    ]