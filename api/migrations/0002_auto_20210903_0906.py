# Generated by Django 3.1.7 on 2021-09-03 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='car',
            name='rating_count',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.car')),
            ],
        ),
    ]
