# Generated by Django 3.2 on 2021-05-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20210421_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingevent',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trackingevent',
            name='code',
            field=models.CharField(max_length=35),
        ),
    ]