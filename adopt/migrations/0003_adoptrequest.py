# Generated by Django 2.2.4 on 2019-09-03 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0002_auto_20190901_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_ts', models.DateTimeField(auto_now_add=True)),
                ('adopter', models.CharField(help_text='Name of adopter', max_length=100)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt.Pet')),
            ],
        ),
    ]