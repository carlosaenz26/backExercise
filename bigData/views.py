from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

#@api_view(['GET', 'POST', 'DELETE'])
def operaciones(request):
    suma=[{'id':1,'operacion':'suma'}]
    resta=[{'id':2,'operacion':'resta'}]
    operaciones={"operaciones":suma+resta}
    return JsonResponse(operaciones)

#@api_view(['GET', 'POST', 'DELETE'])
def suma(request):
    num1=request.GET.get('valor1', '')
    num2=request.GET.get('valor2', '')
    resultado=int(num1)+int(num2)
    return JsonResponse({'resultado':resultado})
    #return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

def resta(request):
    num1=request.GET.get('valor1', '')
    num2=request.GET.get('valor2', '')
    resultado=int(num1)-int(num2)
    return JsonResponse({'resultado':resultado})



