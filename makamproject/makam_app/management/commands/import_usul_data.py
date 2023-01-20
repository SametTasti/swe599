from django.core.management.base import BaseCommand
from makam_app.models import Usul
import os


class Command(BaseCommand):
    help = 'Imports data from a text file and creates new objects in the MyModel model'

    def handle(self, *args, **options):

        # check if the model already has any objects
        if Usul.objects.exists():
            
            self.stdout.write(self.style.WARNING('The model already has data, no data will be imported'))
            return

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'usuller_utf8.txt')

        with open(file_path, 'r', encoding='utf-8') as f:

            for line in f:
                
                name = line.strip()

                # check if object already exists
                if Usul.objects.filter(name=name).exists():

                    self.stdout.write(self.style.WARNING(f'{name} already exists in the model, skipping'))
                    continue

                Usul.objects.create(name=name)
                
        self.stdout.write(self.style.SUCCESS('Successfully imported data from file'))
