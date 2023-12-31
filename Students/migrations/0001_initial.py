# Generated by Django 4.2.7 on 2023-11-17 04:24

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=45)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.course')),
                ('Days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.days')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Image', models.ImageField(upload_to='images')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.course')),
                ('Days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.days')),
                ('task', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Days', chained_model_field='Days', on_delete=django.db.models.deletion.CASCADE, to='Students.task')),
            ],
        ),
    ]
