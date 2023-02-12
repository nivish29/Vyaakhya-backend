# Generated by Django 4.1.6 on 2023-02-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0002_alter_finduser_whatsapp_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="finduser",
            name="instagram_url",
        ),
        migrations.AddField(
            model_name="finduser",
            name="instagram_username",
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]