# Generated by Django 4.1.1 on 2022-11-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='comments_received',
            field=models.ManyToManyField(related_name='comments_received', to='app.comment'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='comments_sent',
            field=models.ManyToManyField(related_name='comments_sent', to='app.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
