from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['POST'])
def registroUsuario(request):
  data = JSONParser().parse(request)
  info = "los datos que llegaron desde el front son: "+data['nomUsu']+" "+data['apeUsu']+" "+data['edadUsu'] +" " +data['corUsu']+" "+data['fecUsu']
  print(info)
  return HttpResponse("hola todos")

 