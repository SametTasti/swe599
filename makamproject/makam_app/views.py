from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import PreliminaryDataEntryForm
from .models import Makam, Usul, Piece
import json
import ast  # ajax ile gelen dictionary'i parse'lamak için

# Create your views here.


def HomeView(request):
    return render(request, 'makam_app/home.html')


def CreatePieceView(request):

    if request.method == 'POST':

        newPiece = Piece(
            eser_adi=request.POST.get('eser_adi'),
            bestekar=request.POST.get('bestekar'),
            yuzyil=request.POST.get('yuzyil'),
            gufte_yazari=request.POST.get('gufte_yazari'),
            gufte_vezin=request.POST.get('gufte_vezin'),
            gufte_nazim_bicim=request.POST.get('gufte_nzmbcm'),
            gufte_nazim_tur=request.POST.get('gufte_nzmtur'),
            makam=request.POST.get('selected_makams'),
            usul=request.POST.get('selected_usuls'),
            form=request.POST.get('selected_form'),
            subcomponents=request.POST.get('selected_subcomponents'),
        )

        newPiece.save()

        return JsonResponse({
            'success': True,
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
