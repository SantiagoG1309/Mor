# Generated by Django 4.2.7 on 2025-03-27 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_assigned_category_alter_user_role_technician'),
    ]

    operations = [
        migrations.AddField(
            model_name='technician',
            name='last_login_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
