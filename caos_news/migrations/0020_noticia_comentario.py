# Generated by Django 3.2.2 on 2021-06-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caos_news', '0019_noticia_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='comentario',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
