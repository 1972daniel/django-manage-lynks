# Generated by Django 3.2.4 on 2023-11-09 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.plan'),
        ),
    ]