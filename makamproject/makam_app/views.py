from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .forms import PreliminaryDataEntryForm
from .models import Makam, Usul, Piece
from django.templatetags.static import static
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import datetime
import json

pseudo_context = {}
selected_pieces_for_analysis = []


def HomeView(request):

    return render(request, 'makam_app/home.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'makam_app/signup.html'


class UserPieceView(LoginRequiredMixin, ListView):
    model = Piece
    template_name = 'makam_app/profile.html'
    paginate_by = 5

    def get_queryset(self):
        return Piece.objects.filter(creator=self.request.user).all()


@login_required
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
            creator=request.user,
            created_date=datetime.date.today(),
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


@login_required
def EditPieceView(request, pk):

    piece_to_be_edited = get_object_or_404(Piece, pk=pk)

    if request.method == 'POST':

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

        print(piece_to_be_edited)
        print(eser_adi,bestekar, yuzyil, gufte_yazari, gufte_vezin, gufte_nazim_bicim, gufte_nazim_tur, makam, usul, form, subcomponents)

        return JsonResponse({
            'success': True,
            'url': reverse("makam_app:profile"),
        })

    else:
        preliminary_data_entry_form = PreliminaryDataEntryForm()

        edit_piece_eser_adi = piece_to_be_edited.eser_adi
        edit_piece_bestekar = piece_to_be_edited.bestekar
        edit_piece_yuzyil = piece_to_be_edited.yuzyil
        edit_piece_gufte_yazari = piece_to_be_edited.gufte_yazari
        edit_piece_gufte_vezin = piece_to_be_edited.gufte_vezin
        edit_piece_gufte_nazim_bicim = piece_to_be_edited.gufte_nazim_bicim
        edit_piece_gufte_nazim_tur = piece_to_be_edited.gufte_nazim_tur
        edit_piece_makam = json.dumps(piece_to_be_edited.makam)
        edit_piece_usul = json.dumps(piece_to_be_edited.usul)
        edit_piece_form = piece_to_be_edited.form
        edit_piece_subcomponents = json.dumps(piece_to_be_edited.subcomponents)
        edit_piece_creator = piece_to_be_edited.creator
        edit_piece_created_date = piece_to_be_edited.created_date

    context_dict = {
        'preliminary_data_entry_form': preliminary_data_entry_form,
        'piece_to_be_edited':piece_to_be_edited,
        'edit_piece_eser_adi': edit_piece_eser_adi,
        'edit_piece_bestekar': edit_piece_bestekar,
        'edit_piece_yuzyil': edit_piece_yuzyil,
        'edit_piece_gufte_yazari': edit_piece_gufte_yazari,
        'edit_piece_gufte_vezin': edit_piece_gufte_vezin,
        'edit_piece_gufte_nazim_bicim': edit_piece_gufte_nazim_bicim,
        'edit_piece_gufte_nazim_tur': edit_piece_gufte_nazim_tur,
        'edit_piece_makam': edit_piece_makam,
        'edit_piece_usul': edit_piece_usul,
        'edit_piece_form': edit_piece_form,
        'edit_piece_subcomponents': edit_piece_subcomponents,
        'edit_piece_creator': edit_piece_creator,
        'edit_piece_created_date': edit_piece_created_date,
        'mkm_json': json.dumps(list(Makam.objects.values())),
        'usl_json': json.dumps(list(Usul.objects.values())),
    }

    return render(request, 'makam_app/edit_piece.html', context=context_dict)


@login_required
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


@login_required
def QueryResultsView(request):

    if request.method == 'POST':

        # buraya analiz için seçilen parçaların pk'ları gelecek, sonra o pk'ları filtre ile alıp analiz işlemini yapacağız
        # sonra da sonuçları yollayacağız

        selected_piece_pks = json.loads(request.POST.get('selected_pieces'))

        if len(selected_piece_pks) > 0:

            for my_pk in selected_piece_pks:

                my_piece = Piece.objects.get(pk=my_pk)

                if my_piece not in selected_pieces_for_analysis:
                    selected_pieces_for_analysis.append(my_piece)

            return JsonResponse({
                'success': True,
                'url': reverse("makam_app:AnalysisView"),
            })

        else:

            return JsonResponse({
                'success': False,
                'url': reverse("makam_app:QueryResultView"),
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

    pieces_found = all_pieces.filter(**filter_dict)

    pseudo_context.clear()
    selected_pieces_for_analysis.clear()
    filter_dict.clear()

    context_dict = {
        'pieces_found': pieces_found,
    }

    return render(request, 'makam_app/query_results.html', context=context_dict)


class AnalyzedPiece:

    piece_name = ""
    analyzed_subcomponents = []

    def __init__(self, piece_name, analyzed_subcomponents):
        self.piece_name = piece_name
        self.analyzed_subcomponents = analyzed_subcomponents


class AnalyzedSubcomponent:

    subcomponent_name = ""
    analyzed_cesnis_list = []

    def __init__(self, subcomponent_name, analyzed_cesnis_list):
        self.subcomponent_name = subcomponent_name
        self.analyzed_cesnis_list = analyzed_cesnis_list


class AnalyzedCesni:

    cesni_name = ""
    cesnis_usul = ""
    cesnis_length_in_256 = 0.0
    percentage_in_usul = 0.0

    def __init__(self, cesni_name, cesnis_usul, cesnis_length_in_256, percentage_in_usul):
        self.cesni_name = cesni_name
        self.cesnis_usul = cesnis_usul
        self.cesnis_length_in_256 = cesnis_length_in_256
        self.percentage_in_usul = percentage_in_usul


class AnalyzedByCommonSubcomponent:

    subcomponent_name = ""
    analyzed_cesnis_list = []

    def __init__(self, subcomponent_name, analyzed_cesnis_list):
        self.subcomponent_name = subcomponent_name
        self.analyzed_cesnis_list = analyzed_cesnis_list


@login_required
def AnalysisView(request):

    analyzed_piece_list = []

    for current_piece in selected_pieces_for_analysis:

        analyzed_subcomponent_list = []

        for subcomponent in current_piece.subcomponents:

            my_analyzed_cesni_list = []

            for cesni in subcomponent['cesni']:

                cesni_isim = cesni['cesni_isim']
                cesnis_usul_isim = cesni['ait_oldugu_usul']
                cesnis_usul_cesit = 0
                cesnis_usul_adet = 0
                cesnis_usul_olcu = 0
                cesnis_usul_length = 0
                usul_scale_multiplier_256 = 0

                for usul in current_piece.usul:

                    if cesni['ait_oldugu_usul'] == usul['isim']:

                        cesnis_usul_cesit = int(usul['cesit'])
                        cesnis_usul_adet = int(usul['adet'])
                        cesnis_usul_olcu = int(usul['olcu'])
                        usul_scale_multiplier_256 = 256 / cesnis_usul_cesit
                        cesnis_usul_length = cesnis_usul_adet * \
                            usul_scale_multiplier_256 * cesnis_usul_olcu
                        # print(cesnis_usul_length)

                cesni_toplam_length_in_256 = 0

                if cesni['olcu_sayisi']:
                    cesni_olcu_sayisi = cesni['olcu_sayisi']
                    cesni_olcu_to_256_length = 1
                    if cesnis_usul_cesit > 0:
                        cesni_olcu_to_256_length = (
                            256 / cesnis_usul_cesit) * float(cesni_olcu_sayisi) * cesnis_usul_adet

                    cesni_toplam_length_in_256 += cesni_olcu_to_256_length
                    # print(cesni_olcu_to_256_length)

                if cesni['dortluk_sayisi']:
                    cesni_dortluk_sayisi = cesni['dortluk_sayisi']
                    cesni_dortluk_to_256_length = (
                        256 / 4) * float(cesni_dortluk_sayisi)
                    cesni_toplam_length_in_256 += cesni_dortluk_to_256_length
                    # print(cesni_dortluk_to_256_length)

                if cesni['sekizlik_sayisi']:
                    cesni_sekizlik_sayisi = cesni['sekizlik_sayisi']
                    cesni_sekizlik_to_256_length = (
                        256 / 8) * float(cesni_sekizlik_sayisi)
                    cesni_toplam_length_in_256 += cesni_sekizlik_to_256_length
                    # print(cesni_sekizlik_to_256_length)

                if cesni['onaltilik_sayisi']:
                    cesni_onaltilik_sayisi = cesni['onaltilik_sayisi']
                    cesni_onaltilik_to_256_length = (
                        256 / 16) * float(cesni_onaltilik_sayisi)
                    cesni_toplam_length_in_256 += cesni_onaltilik_to_256_length
                    # print(cesni_onaltilik_to_256_length)

                cesni_usul_percentage = 0
                if cesnis_usul_length > 0:
                    cesni_usul_percentage = (
                        cesni_toplam_length_in_256 / cesnis_usul_length) * 100
                analyzed_cesni = AnalyzedCesni(cesni_name=cesni_isim, cesnis_usul=cesnis_usul_isim,
                                               cesnis_length_in_256=cesni_toplam_length_in_256, percentage_in_usul=cesni_usul_percentage)

                my_analyzed_cesni_list.append(analyzed_cesni)

                # print(analyzed_cesni.cesni_name)
                # print(analyzed_cesni.cesnis_usul)
                # print(analyzed_cesni.cesnis_length_in_256)
                # print(analyzed_cesni.percentage_in_usul)

            my_analyzed_subcomponent = AnalyzedSubcomponent(
                subcomponent_name=subcomponent['subcomponent_isim'], analyzed_cesnis_list=my_analyzed_cesni_list)

            analyzed_subcomponent_list.append(my_analyzed_subcomponent)

        my_analyzed_piece = AnalyzedPiece(
            piece_name=current_piece.eser_adi, analyzed_subcomponents=analyzed_subcomponent_list)

        analyzed_piece_list.append(my_analyzed_piece)

    # contexte yollamak için veriyi formatla

    cleaned_piece_list = []

    for my_piece in analyzed_piece_list:

        analyzed_data_dict = {}

        analyzed_data_dict['parca_ismi'] = my_piece.piece_name

        analyzed_subcomponent_list = []

        for my_subcomponent in my_piece.analyzed_subcomponents:

            analyzed_subcomponent_dict = {}

            analyzed_cesni_list = []

            for my_cesni in my_subcomponent.analyzed_cesnis_list:

                analyzed_cesni_data_dict = {}

                analyzed_cesni_data_dict['cesni_ismi'] = my_cesni.cesni_name
                analyzed_cesni_data_dict['cesni_usul'] = my_cesni.cesnis_usul
                analyzed_cesni_data_dict['cesni_sure_256'] = my_cesni.cesnis_length_in_256
                analyzed_cesni_data_dict['cesni_oran'] = my_cesni.percentage_in_usul

                analyzed_cesni_list.append(analyzed_cesni_data_dict)

            analyzed_subcomponent_dict['bilesen_ismi'] = my_subcomponent.subcomponent_name
            analyzed_subcomponent_dict['bilesen_cesniler'] = analyzed_cesni_list

            analyzed_subcomponent_list.append(analyzed_subcomponent_dict)

        analyzed_data_dict['bilesenler'] = analyzed_subcomponent_list

        cleaned_piece_list.append(analyzed_data_dict)

    context = {
        'pieces': json.dumps(cleaned_piece_list),
    }

    return render(request, 'makam_app/analysis.html', context=context)
