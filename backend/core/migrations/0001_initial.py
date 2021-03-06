# Generated by Django 3.2.9 on 2021-12-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='sub-título')),
            ],
            options={
                'verbose_name': 'artigo',
                'verbose_name_plural': 'artigos',
                'ordering': ('title',),
            },
        ),
    ]
