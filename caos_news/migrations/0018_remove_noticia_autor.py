# Generated by Django 3.2.2 on 2021-06-15 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caos_news', '0017_noticia_publicar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='autor',
        ),
    ]
