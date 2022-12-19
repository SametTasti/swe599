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

    all_piece_data = Piece.objects.all()

    filter_dict = {}

    icontains_keyword = '__icontains'
    in_keyword = '__in'

    for key, value in pseudo_context.items():

        # girilen query verileri varsa ve tipleri liste değilse:
        if value and (type(value) is not list):
            filter_dict[key + icontains_keyword] = pseudo_context[key]

        elif value and (type(value) is list):
            if key == 'makam':

                number_of_inputted_makams = len(pseudo_context['makam'])

                # girilen makamları al, filter dicte loopla yolla, kolay
                for i in range(number_of_inputted_makams):
                    makam_indice_token = f'__{i}'

                    # db'deki parçaların makamlarının girilen inputta yer alıp almadığını kontrol et
                    filter_dict['makam' + makam_indice_token +
                                in_keyword] = pseudo_context['makam']

            elif key == 'usul':
                # girilen usulları al, usulda hangi veriler varsa onları filtera yolla

                number_of_inputted_usuls = len(pseudo_context['usul'])

                for i in range(number_of_inputted_usuls):

                    # query string oluştururken kullanılacak
                    usul_element_indice_token = f'__{i}'

                    # i'inci usul, 0. 1. 2. ... usuller
                    current_usul = pseudo_context['usul'][i]

                    for usul_property in current_usul:          # seçilen usuldeki alt elementler

                        current_usul_property = current_usul[usul_property]

                        current_property_token = f'__{usul_property}'

                        # usul propertylerine girilen değerler için:
                        if current_usul_property:

                            filter_dict['usul' + usul_element_indice_token + current_property_token +
                                        icontains_keyword] = pseudo_context['usul'][i][usul_property]

            elif key == 'subcomponents':

                number_of_inputted_subcomponents = len(
                    pseudo_context['subcomponents'])

                for i in range(number_of_inputted_subcomponents):

                    subcomponent_element_indice_token = f'__{i}'

                    current_subcomponent = pseudo_context['subcomponents'][i]

                    if current_subcomponent:

                        for subcomponent_property in current_subcomponent:

                            if subcomponent_property == 'subcomponent_isim':

                                current_property_token = f'__{subcomponent_property}'

                                filter_dict['subcomponents' + subcomponent_element_indice_token + current_property_token +
                                            icontains_keyword] = pseudo_context['subcomponents'][i]['subcomponent_isim']

                            elif subcomponent_property == 'cesni':

                                current_cesni_list = pseudo_context['subcomponents'][i]['cesni']

                                if len(current_cesni_list) > 0:

                                    for j in range(len(current_cesni_list)):

                                        cesni_row = current_cesni_list[j]

                                        cesni_row_element_indice_token = f'__{j}'

                                        for cesni_property in cesni_row:

                                            current_property_token = f'__{cesni_property}'

                                            element_value = cesni_row[cesni_property]

                                            if element_value:

                                                # print('subcomponents' + subcomponent_element_indice_token + '__cesni' + cesni_row_element_indice_token + current_property_token +
                                                #             icontains_keyword)

                                                print('subcomponents' + subcomponent_element_indice_token + '__cesni' + cesni_row_element_indice_token + current_property_token +
                                                      icontains_keyword)

                                                print(
                                                    pseudo_context['subcomponents'][i]['cesni'][j][cesni_property])

                                                filter_dict['subcomponents' + subcomponent_element_indice_token + '__cesni' + cesni_row_element_indice_token + current_property_token +
                                                            icontains_keyword] = pseudo_context['subcomponents'][i]['cesni'][j][cesni_property]

    print(filter_dict)

    pieces_found = all_piece_data.filter(**filter_dict)

    context_dict = {
        'pieces_found': pieces_found,
    }

    return render(request, 'makam_app/query_results.html', context=context_dict)
