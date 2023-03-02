from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# def pagina_inicial(request):
#     return HttpResponse("Pronto para investir!")
# *** As três funções abaixo (contato, minha_historia e equipe) foram usadas apenas para ensinar.
# o software final não usa elas, então poderíamos deletá-las. Optei por deixá-las, assim como as 
# páginas html equipe.html e minha_historia.html
# def contato(request):
#     return HttpResponse("Telefone: (21) 2543-5678 Email: contato@consultoria.com.br Whatsapp: (21) 99876-5678")

# def minha_historia(request):
#     return render(request,"investimentos/minha_historia.html")

# def equipe(request):
#     pessoas = {"nome":"Eduardo Melo", "setor": "finanças", "experiencia": "senior"}
#     return render(request, "investimentos/equipe.html", pessoas)

# def investimento_registrado(request):
#     investimento = {
#             "tipo_investimento": request.POST.get("TipoInvestimento")
#     }
#     return render(request, "investimentos/investimento_registrado.html", investimento)
# def novo_investimento(request):
#     return render(request, "investimentos/novo_investimento.html")

# def relatorio(request):
#     return render(request,"investimentos/relatorio.html")

def investimentos(request):
    dados = {
       "dados":Investimento.objects.all()
       }
    return render(request, "investimentos/investimentos.html", context=dados)

def detalhe(request, id_investimento):
    dados = {
    'dados':Investimento.objects.get(pk=id_investimento)
    }
    return render(request, "investimentos/detalhe.html", context=dados)

@login_required
def criar(request):
    if request.method == "POST":
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect("investimentos")
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            "formulario":investimento_form
        }
        return render(request, "investimentos/novo_investimento.html", context=formulario)

@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento) # busco na tabela Investimento o objeto que tenha a primary key / pk = id do item)
    # Caso 1: pessoa está acessando a página "novo_investimento/1" pela primeira vez (só visualizando) -> GET. Buscando dados. Nesse caso, popularei o formulário com as informações referentes ao investimento escolhido (id) e retornarei para a tela o formulário já preenchido
    if request.method == "GET":
        formulario = InvestimentoForm(instance=investimento) # criamos um formulário com os dados já preenchidos através da instância "investimento", que identifica e traz as informações do item desejado via "id_investimento"
        return render(request, "investimentos/novo_investimento.html", {"formulario":formulario}) #direcionará para a página "novo_investimento" e mostrará o formulário já preenchido com as informações do item escolhido
    # Caso 2: pessoa editou alguma informação no formulário e aperta o botão submit para atualizar o banco de dados -> POST. Enviando dados. 
    else: 
        formulario = InvestimentoForm(request.POST, instance=investimento) # Criaremos o formulário com os dados editados pelo usuário. Para editarmos um item no banco de dados sem criar um novo, usamos a propriedade instance, remetendo ao item investimento já identificado antes via id_investimento
        if formulario.is_valid(): # conferiremos se o formulário é válido (função padrão do Django)
            formulario.save() # se for válido, salvaremos no banco de dados
        return redirect("investimentos") # após salvar no banco de dados, usuário é redirecionado para a página "investimentos" (olhar em urls.py, esse é o "name" da nossa página inicial)
   
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento) # busco na tabela Investimento o objeto através da pk (primary key - id). Eu poderia usar outro parâmetro como data=..., valor=..., etc..
    # Por padrão, quando eu acesso uma página, estou fazendo a requisição GET. Quando eu envio dados através de uma página, estou fazendo a requisição POST. Ao confirmar uma exclusão, estou enviando um POST. Nessa parte, o script validará se é POST ou GET
    if request.method == "POST":
        investimento.delete() # aqui eu excluo o item do banco de dados
        return redirect("investimentos") # redireciono a pessoa para a página inicial
    return render(request, "investimentos/confirmar_exclusao.html", {"item": investimento}) # nesse caso, a pessoa está fazendo uma requisição GET (visualização) e, por isso, vamos redirecioná-la à página de confirmação da exclusão. O dicionário com o item recebendo "investimento" é um padrão do Django.
