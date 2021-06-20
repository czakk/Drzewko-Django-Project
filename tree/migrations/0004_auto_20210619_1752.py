# Generated by Django 3.1.6 on 2021-06-19 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20210618_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tree',
            name='title',
            field=models.CharField(default='My Branches', max_length=150),
        ),
        migrations.AlterField(
            model_name='tree',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, unique_for_date='published'),
        ),
    ]