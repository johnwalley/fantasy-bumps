import sys
import os
import csv
import django

# Full path and name to your csv file
csv_filepathname = "./fantasybumps/ClubCrew_totals_-_ladies_data.csv"

# Full path to your django project directory
your_djangoproject_home = "./"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

django.setup()

from fantasybumps.models import Crew
from fantasybumps.models import Club

dataReader = csv.reader(open(csv_filepathname), delimiter='\t', quotechar='"')

def convert_club_name(name):
    if name == '99':
        return "Cambridge '99"
    elif name == 'Champs':
        return "Champion of the Thames"
    elif name == 'City':
        return "City of Cambridge"
    return name

def convert_crew_name(club, crew):
    number = crew.replace(club, '').replace('X-Press', '').replace('X-press', '').strip()

    if number.isdigit():
        return 'w' + number
    else:
        return 'w1'

results = dict()

for row in dataReader:
    if row[0] != 'Bump':
        club = convert_club_name(row[8])
        if club not in results:
            results[club] = dict()

        crew = convert_crew_name(row[8], row[9])

        if crew not in results[club]:
            results[club][crew] = dict()

        results[club][crew][row[11]] = int(row[23])


for club in results:
    for crew in results[club]:
        club_obj, created = Club.objects.get_or_create(name=club)

        crew_obj, created = Crew.objects.get_or_create(club=club_obj, boat=crew)

        print(crew_obj)

        crew_obj.result_1 = results[club][crew]['Tues']
        crew_obj.result_2 = results[club][crew]['Wed']
        crew_obj.result_3 = results[club][crew]['Thurs']
        crew_obj.result_4 = results[club][crew]['Fri']

        crew_obj.save()
