# Generated by Django 3.2.10 on 2023-07-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('emailadd', models.EmailField(blank=True, max_length=254, null=True)),
                ('query', models.CharField(blank=True, max_length=100, null=True)),
                ('phnnum', models.IntegerField(blank=True, null=True)),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
