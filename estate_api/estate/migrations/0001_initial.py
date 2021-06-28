# Generated by Django 3.2.4 on 2021-06-28 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=32)),
                ('price', models.BigIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'property',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('label', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='StatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='estate.property')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='estate.status')),
            ],
            options={
                'db_table': 'status_history',
            },
        ),
    ]
