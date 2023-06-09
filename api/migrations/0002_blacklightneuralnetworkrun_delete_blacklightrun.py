# Generated by Django 4.1.7 on 2023-03-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklightNeuralNetworkRun',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('model_path', models.CharField(blank=True, max_length=255, null=True)),
                ('result', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BlacklightRun',
        ),
    ]
