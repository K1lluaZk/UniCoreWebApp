from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contactForm(request):
    return render(request, "contactform.html")

def contact(request):
    if request.method == "POST":
        asunto = request.POST.get("txtAsunto", "")
        mensaje = request.POST.get("txtMensaje", "") + " / Email: " + request.POST.get("txtEmail", "")
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["correopara"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "successFulContact.html")
    return render(request, "contactForm.html")



