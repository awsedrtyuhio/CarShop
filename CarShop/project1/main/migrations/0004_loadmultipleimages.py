# Generated by Django 4.1.3 on 2022-12-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_loadimage_delete_mymodel1'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadMultipleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
