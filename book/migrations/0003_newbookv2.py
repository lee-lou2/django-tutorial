# Generated by Django 4.1.7 on 2023-03-09 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_newbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewBookV2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='제목', max_length=100)),
            ],
            options={
                'db_table': 'new_book_v2',
            },
        ),
    ]
