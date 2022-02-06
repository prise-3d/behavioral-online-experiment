# Generated by Django 3.2.12 on 2022-02-06 11:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('expe', '0013_auto_20220206_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpage',
            name='styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/classical_end.css', 'experiment/css/classical_end.css'), ('experiment/css/classical_main.css', 'experiment/css/classical_main.css'), ('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=98, null=True),
        ),
        migrations.AlterField(
            model_name='examplepage',
            name='styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/classical_end.css', 'experiment/css/classical_end.css'), ('experiment/css/classical_main.css', 'experiment/css/classical_main.css'), ('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=98, null=True),
        ),
        migrations.AlterField(
            model_name='informationpage',
            name='styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/classical_end.css', 'experiment/css/classical_end.css'), ('experiment/css/classical_main.css', 'experiment/css/classical_main.css'), ('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=98, null=True),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/classical_end.css', 'experiment/css/classical_end.css'), ('experiment/css/classical_main.css', 'experiment/css/classical_main.css'), ('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=98, null=True),
        ),
    ]
