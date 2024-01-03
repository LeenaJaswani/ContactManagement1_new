# yourapp/management/commands/load_json_data.py

import json
from django.core.management.base import BaseCommand
from contacts.models import UserInfo

class Command(BaseCommand):
    help = 'Load data from a JSON file into UserInfo'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='C:/Users/leena/Downloads/RandomData.json')

    def handle(self, *args, **options):
        json_file_path = options['json_file']

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        for item in data:
            UserInfo.objects.create(
                Name=item['Name'],
                EmailAddress=item['EmailAddress'],
				ContactNumber=item['ContactNumber'],
				HomeAddress=item['HomeAddress'],
                Birthday=item['Birthday'],
				Nickname=item['Nickname']
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded data from {json_file_path}'))
