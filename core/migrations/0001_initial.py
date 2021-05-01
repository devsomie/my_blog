# Generated by Django 3.2 on 2021-04-14 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='media/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('intro', models.TextField()),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]