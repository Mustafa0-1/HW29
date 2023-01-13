# Generated by Django 4.1.5 on 2023-01-13 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_location_options_alter_user_options'),
        ('ads', '0002_alter_ad_options_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='users.user'),
        ),
    ]
