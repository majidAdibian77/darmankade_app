# Generated by Django 3.1.6 on 2021-02-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darmankade_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[(1, 'ارتوپدی'), (2, 'اورولوژی'), (3, 'پوست و مو'), (4, 'زنان و زایمان'), (5, 'داخلی'), (6, 'گوش، حلق و بینی'), (7, 'مغز و اعصاب')], max_length=50),
        ),
    ]
