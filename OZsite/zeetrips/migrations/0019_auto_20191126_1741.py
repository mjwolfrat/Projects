# Generated by Django 2.2.7 on 2019-11-26 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('zeetrips', '0018_auto_20191126_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visplek',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID', primary_key=True, serialize=False),
        ),
    ]