from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FactureForm

# Create your views here.


def facture_image_view(request):

    if request.method == 'POST':
        form = FactureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = FactureForm()
    return render(request, 'facture/upload.html', {'form': form})


def success(request):
    return HttpResponse("Votre facture a été enregistrée")
