# Ejemplo ilustrativo (no propietario)
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

class AuthExampleView(View):
    def post(self, request):
        username = request.POST.get("username")
        if not username:
            messages.error(request, "Usuario requerido")
            return redirect("login")
        messages.success(request, f"Hola, {username}")
        return redirect("home")
