# Generated by Django 4.0.5 on 2022-06-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_remove_problem_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
