# Generated by Django 3.0.8 on 2020-09-11 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_pledge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='supporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporter_pledges', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
