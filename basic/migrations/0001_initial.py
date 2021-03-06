# Generated by Django 2.2.4 on 2019-09-24 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnowGiraffe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tongue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
                ('giraffe', models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='basic.SnowGiraffe')),
            ],
        ),
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toe_count', models.IntegerField()),
                ('giraffe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.SnowGiraffe')),
            ],
        ),
    ]
