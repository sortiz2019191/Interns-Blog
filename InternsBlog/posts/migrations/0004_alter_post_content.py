# Generated by Django 3.2.7 on 2021-10-05 06:38

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]
