# Generated by Django 4.2.7 on 2023-11-17 06:17

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Image',
            new_name='Logo',
        ),
        migrations.AlterField(
            model_name='student',
            name='task',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Course', chained_model_field='Course', on_delete=django.db.models.deletion.CASCADE, to='Students.task'),
        ),
    ]
