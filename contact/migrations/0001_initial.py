# Generated by Django 4.2.6 on 2023-11-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=255)),
                ('person', models.CharField(choices=[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5'), ('f', '6'), ('g', '7')], default='1', max_length=50)),
            ],
        ),
    ]
