from django.db import models

class Informacao(models.Model):
    TIPO_INFORMACAO_CHOICES = (
        ('informacoes_pessoais', 'Informações Pessoais'),
        ('informacoes_endereco', 'Informações Endereço'),
        ('informacoes_profissionais', 'Informações Profissionais'),
        ('informacoes_educacao', 'Informações de Educação'),
        ('informacoes_financeiras', 'Informações Financeiras'),
    )

    tipo_informacao = models.CharField(max_length=100, choices=TIPO_INFORMACAO_CHOICES, null = False, blank = False)
    categoria = models.CharField(max_length=200, null = False, blank = False)

    def __str__(self):
        return f"Tipo de Informação: {self.get_tipo_informacao_display()} | Categoria: {self.categoria}"
