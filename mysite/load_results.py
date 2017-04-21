import sys
import os
import csv
import django

# Full path and name to your csv file
csv_filepathname = "./fantasybumps/Bumps_Chart_-_men_data.csv"

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
        return 'm' + number
    else:
        return 'm1'

results = dict()

for row in dataReader:
    if row[0] != 'Club':
        club = convert_club_name(row[0])
        if club not in results:
            results[club] = dict()

        crew = convert_crew_name(row[0], row[1])

        if crew not in results[club]:
            results[club][crew] = dict()

        results[club][crew][row[2]] = int(row[4])


for club in results:
    for crew in results[club]:
        club_obj, created = Club.objects.get_or_create(name=club)

        crew_obj, created = Crew.objects.get_or_create(club=club_obj, boat=crew)

        print(crew_obj)

        crew_obj.result_1 = results[club][crew]['Tues'] - results[club][crew]['Wed']
        crew_obj.result_2 = results[club][crew]['Wed'] - results[club][crew]['Thurs']
        crew_obj.result_3 = results[club][crew]['Thurs'] - results[club][crew]['Fri']
        crew_obj.result_4 = results[club][crew]['Fri'] - results[club][crew]['Final']

        crew_obj.save()
