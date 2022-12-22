from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import PreliminaryDataEntryForm
from .models import Makam, Usul, Piece
import json
import ast  # ajax ile gelen dictionary'i parse'lamak için
from django.db.models import Q

# Create your views here.

pseudo_context = {}


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
            makam=json.loads(request.POST.get('selected_makams')),
            usul=json.loads(request.POST.get('selected_usuls')),
            form=json.loads(request.POST.get('selected_form')),
            subcomponents=json.loads(
                request.POST.get('selected_subcomponents')),
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


def FindPieceView(request):

    if request.method == 'POST':

        # query için verileri al
        eser_adi = request.POST.get('eser_adi')
        bestekar = request.POST.get('bestekar')
        yuzyil = request.POST.get('yuzyil')
        gufte_yazari = request.POST.get('gufte_yazari')
        gufte_vezin = request.POST.get('gufte_vezin')
        gufte_nazim_bicim = request.POST.get('gufte_nzmbcm')
        gufte_nazim_tur = request.POST.get('gufte_nzmtur')
        makam = json.loads(request.POST.get('selected_makams'))
        usul = json.loads(request.POST.get('selected_usuls'))
        form = json.loads(request.POST.get('selected_form'))
        subcomponents = json.loads(request.POST.get('selected_subcomponents'))

        print(type(makam))
        print(type(usul))
        print(type(subcomponents))

        pseudo_context['eser_adi'] = eser_adi
        pseudo_context['bestekar'] = bestekar
        pseudo_context['yuzyil'] = yuzyil
        pseudo_context['gufte_yazari'] = gufte_yazari
        pseudo_context['gufte_vezin'] = gufte_vezin
        pseudo_context['gufte_nazim_bicim'] = gufte_nazim_bicim
        pseudo_context['gufte_nazim_tur'] = gufte_nazim_tur
        pseudo_context['makam'] = makam
        pseudo_context['usul'] = usul
        pseudo_context['form'] = form
        pseudo_context['subcomponents'] = subcomponents

        # burada yukarıdaki verilere göre json query yap, gelenleri context ile queryresult'a yolla

        # return render(request, 'makam_app/query_results.html', context={'asdas':'asdasdas'})

        return JsonResponse({
            'success': True,
            'url': reverse("makam_app:QueryResultsView"),
        })

    else:
        preliminary_data_entry_form = PreliminaryDataEntryForm()

        context_dict = {
            'preliminary_data_entry_form': preliminary_data_entry_form,
            'mkm_json': json.dumps(list(Makam.objects.values())),
            'usl_json': json.dumps(list(Usul.objects.values())),
        }
        return render(request, 'makam_app/find_piece.html', context=context_dict)


def QueryResultsView(request):

    if request.method == 'POST':
        
        # buraya analiz için seçilen parçaların pk'ları gelecek, sonra o pk'ları filtre ile alıp analiz işlemini yapacağız
        # sonra da sonuçları yollayacağız 

        a = ast.literal_eval(request.POST.get('testdata'))
        b = json.loads(request.POST.get('selected_pieces'))

        return JsonResponse({
            'success': True,
            'url': reverse("makam_app:AnalysisView"),
        })

    all_pieces = Piece.objects.all()

    filter_dict = {}

    for (key, value) in pseudo_context.items():

        # key: arama parametresi başlığı
        # value: kullanıcının girdiği arama parametresi
        # buradaki keyler: eser_adi, bestekar, yuzyil, gufte_yazari, gufte_vezin, gufte_nazim_bicim, gufte_nazim_tur, form:
        if value and (type(value) is not list):

            # girilen valuelar için çalışıyor bu if, keyler yukarıda!

            my_input_value = pseudo_context[key]

            print(f"{key} : {my_input_value}")

            my_query_string = f"{key}__contains"

            filter_dict[my_query_string] = my_input_value

        # buradaki keyler: makam, usul, subcomponents:
        elif value and (type(value) is list):

            my_input_value = pseudo_context[key]

            if key == 'makam':

                print(f"{key} : {my_input_value}")

                my_query_string = f"makam__contains"

                filter_dict[my_query_string] = my_input_value

            elif key == 'usul':

                print(f"{key} : {my_input_value}")

                my_query_string = f"usul__contains"

                filter_dict[my_query_string] = my_input_value

            elif key == 'subcomponents':

                print(f"{key} : {my_input_value}")

                my_query_string = f"subcomponents__contains"

                filter_dict[my_query_string] = my_input_value

    print(filter_dict)

    pieces_found = all_pieces.filter(**filter_dict)

    pseudo_context.clear()
    filter_dict.clear()

    context_dict = {
        'pieces_found': pieces_found,
    }

    return render(request, 'makam_app/query_results.html', context=context_dict)


def AnalysisView(request):

    return render(request, 'makam_app/analysis.html')
