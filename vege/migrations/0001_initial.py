# Generated by Django 5.1.4 on 2025-01-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_desc', models.TextField()),
                ('receipe_image', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
