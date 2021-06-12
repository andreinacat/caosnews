from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Categoria,Noticia,Comentarios
from django.contrib.auth import authenticate,logout,login as login_aut
from django.contrib.auth.decorators import login_required

# Create your views here.
####SOLO FALTA FILTRO POR BUSQUEDA################
def index(request):
    categoria = Categoria.objects.all()
    noti_all = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[:3]
    noti_index = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[4:8]


    if User.is_authenticated:
        nombreu = request.user.username
        context = {"categorias":categoria,"noticias":noti_all,"noticias_index":noti_index,"nombre":nombreu,"flag":True}
        return render(request,"index.html",context)
    else:
        nombre =' '
        contexto = {"categorias":categoria,"noticias":noti_all,"noticias_index":noti_index,"nombre":nombre}
        return render(request,"index.html",contexto)

def categoria(request,id):
    cate_all = Categoria.objects.all()
    cate = Categoria.objects.get(nombre_catg=id)
    noti = Noticia.objects.filter(categoria=cate,publicar=True).order_by('-fecha_not') 
    context = {"cate":cate,"cate_all":cate_all,"noti_all":noti}
    return render(request,"Categoria.html",context)

def ingresar(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("name_user")
        contra = request.POST.get("pass_user")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            nombreu = request.user.username
            categorias = Categoria.objects.all()
            noti_all = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[:3]
            noti_index = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[4:8]
            contexto = {"categorias":categorias,"noticias":noti_all,"noticias_index":noti_index,"nombre":nombreu}
            return render(request,"index.html",contexto)
        else:
            mensaje="no existe usuario o contraseña incorrecta" + str(nombre) + " "+ str(contra)


    contexto={"mensaje":mensaje}
    return render(request,"ingresar.html",contexto)


def noticias(request,id):
    categoria = Categoria.objects.all()
    try:
        noti = Noticia.objects.get(nombre_not=id)
        context = {"noticia":noti,"categorias":categoria}
        return render(request, "noticia.html",context)
    except:
        context ={"noticia":"No existe esa Noticia","categorias":categoria}
        return render(request,"Noticia.html",context)


####SOLO FALTA FILTRO POR BUSQUEDA################
def contactanos(request):
    categoria = Categoria.objects.all()
    context = {"categorias":categoria}
    if request.POST:
        nombre_1 = request.POST.get("txtnombre")
        apellido_1 = request.POST.get("txtapellido")
        mail = request.POST.get("txtmail")
        comentario = request.POST.get("contacto")
        
        come = Comentarios(
            nombre_c = nombre_1,
            apellido_c = apellido_1,
            mail_c = mail,
            coment = comentario
        )
        come.save()
    return  render(request,"Contacto.html",context)
    
def galeria(request):
    return render(request,"galeria.html")
####SOLO FALTA FILTRO POR BUSQUEDA################
def nosotros(request):
    categoria = Categoria.objects.all()
    context = {"categorias":categoria}
    return render(request,"Nosotros.html",context)
####SOLO FALTA FILTRO POR BUSQUEDA################
def registrar(request):
    categoria = Categoria.objects.all()
    context = {"categorias":categoria}
    if request.POST:
        user = request.POST.get("txtuser")
        try:
            us = User.objects.get(username=user)
            mensaje = "Usuario existente."
            context = {"categorias":categoria,"mensaje":mensaje}
            
        except:
            nombre = request.POST.get("txtnombre")
            apell = request.POST.get("txtapellido")
            mail = request.POST.get("txtmail")
            pass1 = request.POST.get("txtpass1")
            us = User()
            us.username = user
            us.first_name = nombre
            us.last_name = apell
            us.email = mail 
            us.set_password(pass1)
            us.save()            
    return render(request,"Registro.html",context)

def enviar_noti(request):
    
    cate_all = Categoria.objects.all()
    context = {"categorias": cate_all,"flag":False}
    if User.is_authenticated:
        nombre_us = request.user.username
        context = {"categorias":categoria,"usuario":nombre_us,"flag":True}
        return render(request,"Agregar_noticia.html",context)
    elif request.POST:
        titulo = request.POST.get("txttitulo")
        redacta = request.POST.get("txtnoticia")
        img = request.FILES.get("img_noti")
        cate = request.POST.get("txtcategoria")
        obj_cate = Categoria.objects.get(nombre_catg=cate)

        noti = Noticia(
            nombre_not = titulo,
            redac = redacta,
            img_not = img,
            categoria = obj_cate
        )
        noti.save()
        return render(request,"Agregar_noticia.html",context)
    
    