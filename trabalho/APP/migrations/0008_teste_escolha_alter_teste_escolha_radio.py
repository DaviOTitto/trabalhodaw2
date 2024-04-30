# Generated by Django 5.0.3 on 2024-04-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0007_alter_teste_boolean'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='escolha',
            field=models.CharField(choices=[('1', 'Opção 1'), ('2', 'Opção 2'), ('3', 'Opção 3'), ('4', 'Opção 4')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teste',
            name='escolha_radio',
            field=models.CharField(choices=[('1', 'Opção 1'), ('2', 'Opção 2'), ('3', 'Opção 3'), ('4', 'Opção 4')], verbose_name='escolharadio'),
        ),
    ]
