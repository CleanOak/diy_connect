# Generated by Django 5.1 on 2024-08-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/dojf2qfyl/image/upload/v1721073499/nobody_nruqan.jpg', upload_to='', verbose_name='images/'),
        ),
    ]
