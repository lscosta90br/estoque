# Generated by Django 2.0.5 on 2018-07-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insumoapp', '0003_entradaproduto_saidaproduto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradaproduto',
            name='codigo',
            field=models.BigAutoField(default=1000000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='saidaproduto',
            name='codigo',
            field=models.BigAutoField(default=2000000, primary_key=True, serialize=False),
        ),
    ]
