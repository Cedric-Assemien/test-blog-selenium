# Generated by Django 5.1.5 on 2025-02-10 12:35

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_contenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=tinymce.models.HTMLField(),
        ),
    ]
