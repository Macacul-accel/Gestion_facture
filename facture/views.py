from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import FactureForm
from .models import Factures
from users.models import CustomUser

# Create your views here.

def facture_upload(request):

    if request.method == 'POST':
        form = FactureForm(request.POST, request.FILES)

        if form.is_valid():
            new_fact = form.save(commit=False)
            new_fact.user = request.user
            new_fact.save()
            fact_img_obj = form.instance
            return render(request, 'facture/success.html', 
                          {'form': form, 'fact_img_obj': fact_img_obj})
    else:
        form = FactureForm()
    return render(request, 'facture/upload.html', {'form': form})


def display_facture_view(request):
    if request.method == "GET":
        fct = Factures.objects.filter(user=request.user)
        return render(request, 'facture/factures_list.html',
                       {'fact_list': fct})

def delete_facture(request, pk):
    if request.method == "POST":
        fct = Factures.objects.get(pk=pk)
        fct.delete()
    return redirect('list')
