from django.shortcuts import render
#from django.http import HttpResponse as response
from .models import Curso
# Create your views here.


def home(request):
   #cursosListados = Curso.objects.all() # Para listar todos los datos
   #cursosListados = Curso.objects.all()[:5] # Para listar los datos de la pocicion 0 a la 5 ([:5])(si no le pasamos parametro a la primer posicion por defecto es la 0)
   #cursosListados = Curso.objects.all()[5:] # Para listar los datos de la posicion 5 hasta el final
   #cursosListados = Curso.objects.all()[2:6] # Para listar los datos de la posicion 2 a la 6
   #cursosListados = Curso.objects.all().order_by("nombre") # Para ordenar por nombre ascendente (por defecto es ascendente)
   #cursosListados = Curso.objects.all().order_by("nombre","creditos") # Para ordenar por nombre ascendente y pasarle un segundo parametro por si los nombres se repiten
   #cursosListados = Curso.objects.all().order_by("-nombre") # Para ordenar por nombre descendente con el signo -
   #cursosListados = Curso.objects.filter(nombre = "Historia") # filtrar por un nombre especifico
   #cursosListados = Curso.objects.filter(creditos = 5) # filtramos por creditos
   #cursosListados = Curso.objects.filter(nombre ="Historia",creditos=1) # filtrar por dos parametros, si alguno de los dos no coinciden no devuelve nada
   #cursosListados = Curso.objects.filter(creditos__gte=4) #Para filtrar solo los creditos mayores o igual a 4
   #cursosListados = Curso.objects.filter(creditos__lte=4) #Para filtrar solo los creditos menosres o igual a 4
   #cursosListados = Curso.objects.filter(nombre__startswith="Q") #Filtramos nombres que empiecen con alguna letra especifica (tener en cuenta que si el nombre es con Q mayuscula y le ponemos q minuscula no la encuentra)
   #cursosListados = Curso.objects.filter(nombre__contains="l") #Filtramos por nombre que contenga la letra que le pasamos (tener en cuenta las mayusculas y minusculas)
   cursosListados = Curso.objects.all()
   
   
   return render(request,"gestionCursos.html",{"cursos":cursosListados})
