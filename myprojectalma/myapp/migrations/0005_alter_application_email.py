# Generated by Django 5.0.6 on 2024-06-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_application_user_application_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
