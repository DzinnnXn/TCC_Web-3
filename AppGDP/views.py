from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import FormLogin, formCadastroUsuario, InventarioForm
from .models import Senai
from django.contrib.auth.models import User
from .models import Inventario
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def homepageDark(request):
    return render(request, 'homepageDark.html')

def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')

def faq(request):
    return render(request, 'faq.html')

def welcomeHomepage(request):
    return render(request, 'welcomeHomepage.html')

# Importar o modelo de itens (substitua Item pelo nome correto do seu modelo)


def itens(request):
    inventario = Inventario.objects.all()
    item_especifico = inventario.first()  # ou qualquer outro critério para escolher o item
   
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itens')  # Redireciona para a página de itens
    else:
        form = InventarioForm()
    
    return render(request, 'itens.html', {'form': form, 'inventario': inventario, 'item_especifico': item_especifico})



def adicionar_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para a rota inicial, independente de onde estava
    else:
        form = InventarioForm()
    
    # Se precisar listar todos os itens no modal de adição, inclua isso:
    inventario = Inventario.objects.all()
    
    return render(request, 'itens.html', {'form': form, 'inventario': inventario})



def cadastroUsuario(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = formCadastroUsuario(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['first_name']
            var_sobrenome = form.cleaned_data['last_name']
            var_usuario = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['password']

            user = User.objects.create_user(username=var_usuario, email=var_email, password=var_senha)
            user.first_name = var_nome
            user.last_name = var_sobrenome
            user.save()
            return redirect('/login')
            print('Cadastro realizado com sucesso')
    else:
        form = formCadastroUsuario()
        context['form'] = form
        print('Cadastro falhou')
    return render(request, 'cadastroUsuario.html', context)

def login(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():

            var_usuario = form.cleaned_data['user']
            var_senha = form.cleaned_data['password']
            
            user = authenticate(username=var_usuario, password=var_senha)

            if user is not None:
                auth_login(request, user)
                return redirect('/welcomeHomepage')  
            else:
                print('Login falhou')
    else:
        form = FormLogin()
        context['form'] = form
        return render(request, 'login.html', context)
    

def buscar_itens(request):
    context = {}
    query = request.GET.get('q')  # Pega o valor digitado no campo de busca
    if query:
        inventario = Inventario.objects.filter(num_inventario__icontains=query)
    else:
        inventario = Inventario.objects.all()

    context['inventario'] = inventario
    form = InventarioForm()
    context['form'] = form
    
    return render(request, 'itens.html', context)

def excluir_inventario(request):
    if request.method == 'POST':
        num_inventario = request.POST.get('num_inventario')
        print(f"Recebido num_inventario: {num_inventario}")  # Verificando o valor recebido

        # Excluir o item baseado no número de inventário
        try:
            item = Inventario.objects.get(num_inventario=num_inventario)
            item.delete()
            print(f"Item {num_inventario} excluído com sucesso")  # Log de sucesso
            return redirect('itens')  # Redirecionar após exclusão
        except Inventario.DoesNotExist:
            print(f"Item {num_inventario} não encontrado")  # Log de erro
            return HttpResponse("Item não encontrado.", status=404)
    return HttpResponse("Método não permitido.", status=405)

#def excluir_sala(request):
    # if request.method == 'POST':
         