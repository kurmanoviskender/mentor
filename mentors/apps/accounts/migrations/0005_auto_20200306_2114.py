# Generated by Django 3.0.3 on 2020-03-06 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200306_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teacher_user', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]