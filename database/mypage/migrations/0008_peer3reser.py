# Generated by Django 5.1.2 on 2024-10-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0007_delete_peerone'),
    ]

    operations = [
        migrations.CreateModel(
            name='peer3reser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_idpeer3', models.IntegerField()),
                ('namepeer3', models.CharField(max_length=100)),
                ('event_datepeer3', models.DateField()),
                ('start_timepeer3', models.TimeField(blank=True, null=True)),
                ('end_timepeer3', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
