# Generated by Django 4.1.7 on 2023-03-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0002_invntor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invntor',
            name='exporter',
            field=models.CharField(max_length=1000, verbose_name='المورد له'),
        ),
        migrations.AlterField(
            model_name='invntor',
            name='name',
            field=models.CharField(max_length=500, verbose_name='اسم المنتج'),
        ),
        migrations.AlterField(
            model_name='invntor',
            name='quntity',
            field=models.IntegerField(verbose_name='الكميه المنصرفه'),
        ),
        migrations.AlterField(
            model_name='invntor',
            name='user',
            field=models.CharField(max_length=500, verbose_name='المنصرف له'),
        ),
    ]