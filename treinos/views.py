from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Treino
import json


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')


@login_required
def index(request):
    return render(request, 'index.html')


@csrf_exempt
@login_required
def salvar_treino(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            treino = Treino(
                nome_completo=data['nomeCompleto'],
                sexo=data['sexo'],
                idade=data['idade'],
                identidade=data['identidade'],
                setor=data['setor'],
                flexoes=data['flexoes'],
                abdominais=data['abdominais'],
                corrida=data['corrida'],
                nivel_flexoes=data['nivelFlexoes'],
                nivel_abdominais=data['nivelAbdominais'],
                nivel_corrida=data['nivelCorrida']
            )
            treino.save()
            return JsonResponse({'status': 'success', 'message': 'Treino salvo com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)
