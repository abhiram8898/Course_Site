# Generated by Django 4.1.7 on 2023-04-05 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sil_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category_id',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
