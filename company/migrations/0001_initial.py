# Generated by Django 4.1.7 on 2023-04-04 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('s_no', models.IntegerField(default=1)),
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employe',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.departments')),
            ],
        ),
    ]
