# Generated by Django 2.1.1 on 2018-10-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=100)),
                ('to_email', models.EmailField(max_length=100)),
                ('email_subject', models.CharField(max_length=100)),
                ('email_body', models.TextField(max_length=500)),
            ],
        ),
    ]
