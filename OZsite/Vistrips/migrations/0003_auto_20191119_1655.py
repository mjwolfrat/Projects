# Generated by Django 2.2.7 on 2019-11-19 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leden', '0002_boot_plaatsen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(help_text='vul plaats van de haven in', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='boot',
            name='haven',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leden.Haven'),
        ),
    ]
