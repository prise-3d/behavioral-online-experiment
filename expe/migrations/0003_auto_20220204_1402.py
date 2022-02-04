# Generated by Django 3.2.12 on 2022-02-04 14:02

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('expe', '0002_rename_url_experiment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplepage',
            name='javascripts',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('static/experiment/js/example.js', 'example.js')], max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='examplepage',
            name='styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('static/experiment/css/example.css', 'example.css')], max_length=33, null=True),
        ),
    ]