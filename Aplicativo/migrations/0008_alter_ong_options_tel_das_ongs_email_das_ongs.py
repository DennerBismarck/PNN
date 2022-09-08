# Generated by Django 4.1 on 2022-09-08 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicativo', '0007_ong'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ong',
            options={'verbose_name': 'ONG'},
        ),
        migrations.CreateModel(
            name='TEL_DAS_ONGS',
            fields=[
                ('ton_telefone', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('ton_ong_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Aplicativo.ong')),
            ],
            options={
                'verbose_name': 'Telefone da ONG',
                'verbose_name_plural': 'Telefone das ONGs',
                'unique_together': {('ton_telefone', 'ton_ong_id')},
            },
        ),
        migrations.CreateModel(
            name='EMAIL_DAS_ONGS',
            fields=[
                ('emo_email', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('emo_ong_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Aplicativo.ong')),
            ],
            options={
                'verbose_name': 'E-mail da ONG',
                'verbose_name_plural': 'E-mail das ONGs',
                'unique_together': {('emo_email', 'emo_ong_id')},
            },
        ),
    ]
