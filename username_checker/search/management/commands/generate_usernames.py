from django.core.management.base import BaseCommand
from faker import Faker
from search.models import Username

class Command(BaseCommand):
    help = 'Generate fake usernames'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of usernames to create')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        created = 0

        for _ in range(count):
            name = fake.user_name()
            if not Username.objects.filter(name=name).exists():
                Username.objects.create(name=name)
                created += 1

        self.stdout.write(self.style.SUCCESS(f'{created} usernames created.'))
