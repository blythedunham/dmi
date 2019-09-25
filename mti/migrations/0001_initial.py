# Generated by Django 2.2.4 on 2019-09-24 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cheetah',
            fields=[
                ('bigcat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mti.BigCat')),
            ],
            bases=('mti.bigcat',),
        ),
        migrations.CreateModel(
            name='Lion',
            fields=[
                ('bigcat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mti.BigCat')),
                ('giraffes_hunted', models.IntegerField()),
            ],
            bases=('mti.bigcat',),
        ),
    ]