# Generated by Django 4.0.1 on 2022-01-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('lat', models.DecimalField(decimal_places=15, max_digits=15)),
                ('lng', models.DecimalField(decimal_places=15, max_digits=15)),
            ],
        ),
    ]
