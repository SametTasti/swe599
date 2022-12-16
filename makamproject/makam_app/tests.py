from django.test import TestCase

# Create your tests here.

piece = {

    'eser_adi': 'gulnihal',
    'bestekar': 'ali',
    'yuzyil': 21,
    'gufte_yazari': 'veli',
    'gufte': 'gft',

    'makam': [
        'dorian',
        'phyrigian',
    ],

    'usul': [
        {
            'usul_ismi': 'semai',
            'mertebe_cesit': 2,
            'mertebe_adet': 8,
            'olcu_sayisi': 12,
        },
        {
            'usul_ismi': 'aksak',
            'mertebe_cesit': 2,
            'mertebe_adet': 8,
            'olcu_sayisi': 12,
        },
    ],

    'form': [
        {
            'alt_bilesen_ismi': 'bil1',
            'cesni': [
                {
                    'cesni_ismi': 'hicaz',
                    'perde': 'kaba',
                    'cesni_buyuklugu': 4,
                    'ait_oldugu_usul': 'aksak',
                },
                {
                    'cesni_ismi': 'rast',
                    'perde': 'kurdi',
                    'cesni_buyuklugu': 3,
                    'ait_oldugu_usul': 'aksak',
                }
            ],
        },
    ]
}
