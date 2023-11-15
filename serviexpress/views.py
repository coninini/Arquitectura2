from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request,'serviexpress/index.html',context)

def servicios(request):
    context={}
    return render(request,'serviexpress/servicios.html',context)

def reserva(request):
    context={}
    return render(request,'serviexpress/reserva.html',context)

def cuenta(request):
    context={}
    return render(request,'serviexpress/cuenta.html',context)

def contacto(request):
    context={}
    return render(request,'serviexpress/contacto.html',context)

def tipoUsuario(request):
    context={}
    return render(request,'serviexpress/tipoUsuario.html',context)

def registro_cli(request):
    context={}
    return render(request,'serviexpress/registro_cli.html',context)

def servicio1(request):
    context={}
    return render(request,'serviexpress/servicio1.html',context)

def servicio2(request):
    context={}
    return render(request,'serviexpress/servicio2.html',context)

def servicio3(request):
    context={}
    return render(request,'serviexpress/servicio3.html',context)

def servicio4(request):
    context={}
    return render(request,'serviexpress/servicio4.html',context)

def servicio5(request):
    context={}
    return render(request,'serviexpress/servicio5.html',context)

def servicio6(request):
    context={}
    return render(request,'serviexpress/servicio6.html',context)

def registro_pro(request):
    context={}
    return render(request,'serviexpress/registro_pro.html',context)

def registro_emp(request):
    context={}
    return render(request,'serviexpress/registro_emp.html',context)

def confirmacion_res(request):
    context={}
    return render(request,'serviexpress/confirmacion_res.html',context)
