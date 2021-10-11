# Generated by Django 3.2.8 on 2021-10-11 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('email', models.EmailField(max_length=120, verbose_name='email address')),
                ('create_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'apply',
                'verbose_name_plural': 'applications',
            },
        ),
        migrations.CreateModel(
            name='ApplyStatus',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('status', models.CharField(choices=[('A', 'Approche'), ('R', 'Regect')], max_length=1, null=True)),
                ('apply', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status_of', to='apply.apply', verbose_name='apply')),
            ],
            options={
                'verbose_name': 'apply status',
                'verbose_name_plural': 'applications status',
            },
        ),
    ]
