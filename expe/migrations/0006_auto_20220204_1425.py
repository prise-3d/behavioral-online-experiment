# Generated by Django 3.2.12 on 2022-02-04 14:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('expe', '0005_auto_20220204_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplepage',
            name='javascripts',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/js/example.js', 'experiment/js/example.js')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='examplepage',
            name='styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/example.css', 'experiment/css/example.css')], max_length=26, null=True),
        ),
    ]