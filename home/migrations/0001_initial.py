# Generated by Django 3.1 on 2020-09-12 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Task'), (2, 'Improvement'), (3, 'New Feature'), (4, 'Bug')])),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('priority', models.CharField(choices=[('H', 1), ('HM', 2), ('M', 3), ('ML', 4), ('L', 5)], max_length=12)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('create_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
