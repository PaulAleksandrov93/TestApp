# Generated by Django 4.1.7 on 2023-05-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('url', models.CharField(max_length=255, verbose_name='Link')),
                ('position', models.PositiveBigIntegerField(default=1, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'menu items',
                'ordering': ('position',),
            },
        ),
    ]
