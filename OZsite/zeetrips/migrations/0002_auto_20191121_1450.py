# Generated by Django 2.2.7 on 2019-11-21 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zeetrips', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geboekt',
            options={'verbose_name': 'Visser', 'verbose_name_plural': 'Vissers'},
        ),
        migrations.RemoveField(
            model_name='geboekt',
            name='naam',
        ),
        migrations.AddField(
            model_name='geboekt',
            name='naam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
