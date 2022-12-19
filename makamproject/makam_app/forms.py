from django import forms

class PreliminaryDataEntryForm(forms.Form):
    eser_adi = forms.CharField()
    bestekar = forms.CharField()
    yuzyil = forms.IntegerField()
    gufte_yazari = forms.CharField()
    VEZIN_CHOICES = (
        ('', 'Yok'),
        ('1', 'Aruz'),
        ('2', 'Serbest'),
    )
    gufte_vezin = forms.ChoiceField(widget=forms.Select, choices= VEZIN_CHOICES)
    NZMBCM_CHOICES = (
        ('', 'Yok'),
        ('gazel', 'Gazel'),
        ('murabba', 'Murabba'),
        ('kaside', 'Kaside'),
    )
    gufte_nzmbcm = forms.ChoiceField(
        widget=forms.Select, choices=NZMBCM_CHOICES)
    NZMTUR_CHOICES = (
        ('', 'Yok'),
        ('munacat', 'Münacat'),
        ('naat', 'Naat'),
        ('tevhit', 'Tevhit'),
    )
    gufte_nzmtur = forms.ChoiceField(
        widget=forms.Select, choices=NZMTUR_CHOICES)
    