# Generated by Django 4.2.3 on 2023-07-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_informacao', models.CharField(choices=[('informacoes_pessoais', 'Informações Pessoais'), ('informacoes_endereco', 'Informações Endereço'), ('informacoes_profissionais', 'Informações Profissionais'), ('informacoes_educacao', 'Informações de Educação'), ('informacoes_financeiras', 'Informações Financeiras')], max_length=100)),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
    ]