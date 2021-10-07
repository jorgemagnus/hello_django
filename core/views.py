from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,calculo,valor1,valor2,operacao):
    if operacao==1:
        calculo=valor1+valor2
    elif operacao==2:
        calculo = valor1*valor2
    elif operacao==3:
        calculo = valor1/valor2
    elif operacao==4:
        calculo = valor1 - valor2
    return HttpResponse(f'<h1>o valor da operação é:{calculo}</h1>')