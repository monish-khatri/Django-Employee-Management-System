from django.core.management.base import BaseCommand
import random
from employee.models import Team

# python manage.py seed --mode=clear
# python manage.py seed --mode=refresh --number=10
""" Clear all data and creates Teams """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")
        parser.add_argument('--number', type=int, help="Number Of Enteries")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'], options['number'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Teams instances")
    Team.objects.all().delete()


def create_team():
    """Creates an team object combining different elements from the list"""
    print("Creating team")
    name = ["CakePHP", "JS", "CRM", "CMS", "Sales","Magento","BDE","Oddo","HR"]

    team = Team(name=random.choice(name),status=1)
    team.save()
    print("{} team created.".format(team))

    return team

def run_seed(self, mode,number):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating N number teams
    for i in range(number):
        create_team()