from django.contrib import auth
import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Categoria,Noticia,Comentarios
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required


# Create your views here.
def out_session(request):
    logout(request)
    categorias = Categoria.objects.all()
    noti_all = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[:3]
    noti_index = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[4:8]
    contexto = {"categorias":categorias,"noticias":noti_all,"noticias_index":noti_index}
    return render(request,"index.html",contexto)
########################################################################################################################
def busq_autor(request):
    users_n = User.objects.filter(groups=1)
    categoria = Categoria.objects.all()  
    context = {"categorias":categoria,"users":users_n}
    return  render(request,"autores.html",context)
@login_required(login_url='/Ingresar/')
def mis_news(request):
    user = User.objects.get(username=request.user.username)
    categoria = Categoria.objects.all()
    noti_all = Noticia.objects.filter(autor=user)
    contexto = {"categorias":categoria,"noticias":noti_all}
    return render(request,"mis_notis.html",contexto)
########################################################################################################################
def ingresar(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("name_user")
        contra = request.POST.get("pass_user")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login (request,us)
            nombreu = request.user.username
            categorias = Categoria.objects.all()
            noti_all = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[:3]
            noti_index = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[4:8]
            contexto = {"categorias":categorias,"noticias":noti_all,"noticias_index":noti_index,"nombre":nombreu}
            return render(request,"index.html",contexto)
        else:
            mensaje="No existe usuario o contraseña incorrecta."
    contexto={"mensaje":mensaje}
    return render(request,"ingresar.html",contexto)
########################################################################################################################
def index(request):
    categoria = Categoria.objects.all()  
    noti_all = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[:3]
    noti_index = Noticia.objects.filter(publicar=True).order_by('-fecha_not')[4:8]
    contexto = {"categorias":categoria,"noticias":noti_all,"noticias_index":noti_index}
    return render(request,"index.html",contexto) 
########################################################################################################################
def filtro_busqueda(request):
    categoria = Categoria.objects.all()
    noti_all = Noticia.objects.all()
    if request.POST:
        busqueda = request.POST.get("txtbusqueda")
        noti_all = Noticia.objects.filter(publicar=True,nombre_not__contains=busqueda)
        cantidad = Noticia.objects.filter(publicar=True,nombre_not__contains=busqueda).count()
    contexto = {"categorias":categoria,"noticias":noti_all,"cantidad":cantidad}
    return render(request, 'index.html',contexto)
########################################################################################################################
def categoria(request,id):
    cate_all = Categoria.objects.all()
    cate = Categoria.objects.get(nombre_catg=id)
    noti = Noticia.objects.filter(categoria=cate,publicar=True).order_by('-fecha_not') 
    context = {"cate":cate,"cate_all":cate_all,"noti_all":noti}
    return render(request,"Categoria.html",context)
########################################################################################################################
def noticias(request,id):
    categoria = Categoria.objects.all()
    try:
        noti = Noticia.objects.get(nombre_not=id)
        context = {"noticia":noti,"categorias":categoria}
        return render(request, "noticia.html",context)
    except:
        context ={"noticia":"No existe esa Noticia","categorias":categoria}
        return render(request,"Noticia.html",context)
########################################################################################################################
def contactanos(request):
    categoria = Categoria.objects.all()
    context = {"categorias":categoria}
    if request.POST:
        nombre_1 = request.POST.get("txtnombre")
        apellido_1 = request.POST.get("txtapellido")
        mail = request.POST.get("txtmail")
        comentario = request.POST.get("txtcoment")
        
        come = Comentarios(
            nombre_c = nombre_1,
            apellido_c = apellido_1,
            mail_c = mail,
            coment = comentario
        )
        come.save()
    return  render(request,"Contacto.html",context)
########################################################################################################################   
def galeria(request):
    return render(request,"galeria.html")
########################################################################################################################
def nosotros(request):
    categoria = Categoria.objects.all()
    context = {"categorias":categoria}
    return render(request,"Nosotros.html",context)
########################################################################################################################
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
            us.is_active = False
            us.save()            
    return render(request,"Registro.html",context)
########################################################################################################################
@login_required(login_url='/Ingresar/')
def enviar_noti(request): 
    mensaje=''
    if request.POST:
        titulo = request.POST.get("txttitulo")
        redacta = request.POST.get("txtnoticia")
        img = request.FILES.get("img_noti")
        cate = request.POST.get("txtcategoria")
        obj_cate = Categoria.objects.get(nombre_catg=cate)
        user = User.objects.get(username=request.user.username)
        try:
            noti = Noticia.objects.get(nombre_not=titulo)
            mensaje="El titulo ya Existe!!."
        except:
            noti = Noticia(
                nombre_not = titulo,
                redac = redacta,
                img_not = img,
                categoria = obj_cate,
                autor = user,
            )
            noti.save()
    cate_all = Categoria.objects.all()
    contexto = {"categorias": cate_all,"mensaje":mensaje}
    return render(request,"Agregar_noticia.html",contexto)

@login_required(login_url='/Ingresar/')
def b_modificar(request,id):
    try:
        noti = Noticia.objects.get(nombre_not=id)
        cate = Categoria.objects.all()
        context={"noticias":noti,"categorias":cate}
        return render(request,"modificar.html",context)
    except:
        mess= "No se encontro la noticia"
    cate = Categoria.objects.all()
    noti = Noticia.objects.all()
    context={"noticias":noti,"categorias":cate,"mensaje":mess}
    return render(request,"modificar.html",context)

@login_required(login_url='/Ingresar/')
def modificar(request):
    mensaje=''
    if request.POST:
        titulo = request.POST.get("titulo")
        redacta = request.POST.get("txtnoticia")
        img = request.FILES.get("img_noti")
        cate = request.POST.get("txtcategoria")
        obj_cate = Categoria.objects.get(nombre_catg=cate)
        try:
            noti = Noticia.objects.get(nombre_not=titulo)
            noti.redac = redacta
            noti.categoria= obj_cate
            if img is not None:
                noti.img_not = img
            noti.comentario ='En espera de Revision.'
            noti.save()
            mensaje="Noticia modificada con exito!!."
        except:
            mensaje="La noticia no pudo ser modificada."
    cate_all = Categoria.objects.all()
    noti_all = Noticia.objects.all()
    contexto={"noticias":noti_all,"categorias":cate_all,"mensaje":mensaje}
    return render(request,"mis_notis.html",contexto)