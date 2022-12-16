from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import PreliminaryDataEntryForm
from .models import Makam, Usul
import json
import ast  # ajax ile gelen dictionary'i parse'lamak için

# Create your views here.


def HomeView(request):
    return render(request, 'makam_app/home.html')


def CreatePieceView(request):

    if request.method == 'POST':

        preliminary_data_entry_form = PreliminaryDataEntryForm(request.POST)

        if preliminary_data_entry_form.is_valid():
            # print(preliminary_data_entry_form.cleaned_data)

            subcomponents = request.POST.get('selected_subcomponents')
            parsed_subcomponents = ast.literal_eval(subcomponents)
            usuls = request.POST.get('selected_usuls')
            parsed_usuls = ast.literal_eval(usuls)

            print(parsed_subcomponents)
            print(parsed_usuls)

            # burada piece objesi oluştur, modele kaydet

            return JsonResponse({
                'success': True,
                'url': reverse("makam_app:HomeView"),
            })

        else:
            return JsonResponse({
                'success': False,
                'url': reverse("makam_app:HomeView"),
            })

    else:
        preliminary_data_entry_form = PreliminaryDataEntryForm()

        context_dict = {
            'preliminary_data_entry_form': preliminary_data_entry_form,
            'mkm_json': json.dumps(list(Makam.objects.values())),
            'usl_json': json.dumps(list(Usul.objects.values())),
        }
        return render(request, 'makam_app/create_piece.html', context=context_dict)
