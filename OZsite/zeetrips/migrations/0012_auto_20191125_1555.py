# Generated by Django 2.2.7 on 2019-11-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeetrips', '0011_auto_20191125_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vistrip',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]