# Generated by Django 3.2.3 on 2021-10-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=250)),
                ('PublicationDate', models.DateTimeField(default='')),
                ('body', models.TextField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='image/')),
            ],
        ),
    ]
