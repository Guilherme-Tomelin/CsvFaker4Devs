from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
#from django.views.decorators.cache import never_cache

def index(request):
    return render(request, 'index.html')

def gerador_view(request):
    #funcao principal
    pass


#------------------------Validações de Formulário------------------------

def coletar_dados(request):
    if request.method == 'POST':
        linhas_tabela = {}

        for chave, valor in request.POST.items():
            if chave.startswith('nome_campo_usuario_'):
                index = chave.split('_')[-1]
                linhas_tabela[index] = {
                    'nome_campo': valor,
                    'campo_adicional': request.POST.get('valor.campoAdicional'),
                }
                print(f'Index: {index}, Dados: {linhas_tabela[index]}')

        nome_arquivo = request.POST.get('nome_arquivo')
        print(nome_arquivo)
        nlinhas = int(request.POST.get('nlinhas'))
        print(nlinhas)
        print()
        print()
        print()
        print("--------------------------------------------------------------------")
        print(linhas_tabela)
        # Aqui você pode usar a lógica adequada para gerar o CSV com os dados da tabela

        # Retorne o arquivo CSV como resposta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{nome_arquivo}.csv"'

        # Aqui você pode usar o módulo csv do Django para escrever os dados no objeto response
        writer = csv.writer(response)
        # Escreva os dados no CSV usando writer.writerow() ou writer.writerows()

        return response

#------------------------Lógica para Gerar Csv------------------------

def preenchimento_dados(nlinhas, categorias):

    dados_csv = []
    #n_campos = len(categorias)

    dados_csv.append(categorias) #Nome dos campos, primeira linha

    for linha in range(nlinhas):
        registro = [f"Nome{linha}",f"CPF{linha}",f"Idade{linha}",f"Cidade{linha}",f"Profissão{linha}"]
        dados_csv.append(registro)
    
    return dados_csv

def gera_csv(nlinhas, categorias):

    dados_csv = preenchimento_dados(nlinhas, categorias)

    nome_arquivo = 'dados.csv'
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(dados_csv)

    print(f'O arquivo {nome_arquivo} foi criado com sucesso.')
    print(dados_csv)

#------------------------Configuração de categorias------------------------

def adicionar_campo(request):
    if request.method == 'POST':
        tipoDado = request.POST.get('tipoDado')
        campoAdicional = request.POST.get('campoAdicional')

        tipoDado_map = {
            'informacoes_pessoais': 'Informações Pessoais',
            'informacoes_endereco': 'Informações de Endereço',
            'informacoes_profissionais': 'Informações Profissionais',
            'informacoes_educacao': 'Informações de Educação',
            'informacoes_financeiras': 'Informações Financeiras',
        }

        campos_tabela = request.session.get('campos_tabela', {})
        chave = len(campos_tabela) + 1
        campos_tabela[chave] = {
            'tipoDado': tipoDado_map.get(tipoDado, ''),
            'campoAdicional': campoAdicional
        }
        request.session['campos_tabela'] = campos_tabela
        return render(request, 'index.html', {'campos_tabela': campos_tabela})
    else:
        campos_tabela = request.session.get('campos_tabela', {})

    return render(request, 'index.html', {'campos_tabela': campos_tabela})


#------------------------Validações de Formulário------------------------
class ValidaFormulario:

    @staticmethod
    def valida_nlinhas(nlinhas):
        if nlinhas > 0:
            return True
        print("Insira um número maior do que 0.")
        return False

