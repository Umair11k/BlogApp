# Generated by Django 3.2.9 on 2021-11-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_comment_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sender_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]