# Generated by Django 3.1 on 2020-09-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
