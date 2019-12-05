# Generated by Django 3.0 on 2019-12-05 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.IntegerField(null=True)),
                ('total_visits', models.IntegerField(null=True)),
                ('first_joined', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('total_points',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=150)),
                ('cellphone', models.CharField(default='', max_length=20, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('active', models.BooleanField(default=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('full_name',),
            },
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_date', models.DateTimeField(null=True)),
                ('total_points', models.IntegerField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('exchange_date',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(default='', max_length=50)),
                ('ticket_date', models.DateField(null=True)),
                ('amount', models.FloatField(null=True)),
                ('total_points', models.IntegerField(null=True)),
                ('transaction_date', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
            options={
                'ordering': ('ticket_date',),
            },
        ),
    ]
