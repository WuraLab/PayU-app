# Generated by Django 3.0.8 on 2020-08-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200801_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_record',
            name='balance_to_pay',
            field=models.IntegerField(blank=True),
        ),
    ]