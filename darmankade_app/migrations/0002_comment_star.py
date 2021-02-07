# Generated by Django 3.1.6 on 2021-02-07 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('darmankade_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.SmallIntegerField(default=0)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='darmankade_app.doctor')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='darmankade_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='commets', to='darmankade_app.doctor')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='commets', to='darmankade_app.patient')),
            ],
        ),
    ]