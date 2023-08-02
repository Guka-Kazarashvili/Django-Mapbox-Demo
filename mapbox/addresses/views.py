from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Address


class AddressView(CreateView):
    model = Address
    fields = [
        'address'
    ]
    template_name = 'home.html'
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['access_token'] = 'pk.eyJ1IjoiZ3Vra2EtIiwiYSI6ImNsa3RtMjNzMDAxd3UzZnIwZmlvN3d1cmgifQ.lEK2iW44G1IfkzcUQhIufA'
        context['addresses'] = Address.objects.all()
        return context
    

def delete_address(request, address_id):
    try:
        address = Address.objects.get(pk=address_id)
        address.delete()
    except Address.DoesNotExist:
        pass
    return redirect('home')