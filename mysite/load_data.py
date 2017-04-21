import sys
import os
import csv
import django

# Full path and name to your csv file
csv_filepathname = "./fantasybumps/2016 bumps entries.csv"

# Full path to your django project directory
your_djangoproject_home = "./"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

django.setup()

from fantasybumps.models import Crew
from fantasybumps.models import Club
from fantasybumps.models import Rower

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != u'\ufeffBoat':
        club, created = Club.objects.get_or_create(name=row[1])

        crew, created = Crew.objects.get_or_create(
            boat=row[0], club=club, name=row[2], gender=row[3])

        cox, created = Rower.objects.get_or_create(name=row[4])
        crew.cox = cox

        rower, created = Rower.objects.get_or_create(name=row[5])
        crew.stroke = rower

        rower, created = Rower.objects.get_or_create(name=row[6])
        crew.seven = rower

        rower, created = Rower.objects.get_or_create(name=row[7])
        crew.six = rower

        rower, created = Rower.objects.get_or_create(name=row[8])
        crew.five = rower

        rower, created = Rower.objects.get_or_create(name=row[9])
        crew.four = rower

        rower, created = Rower.objects.get_or_create(name=row[10])
        crew.three = rower

        rower, created = Rower.objects.get_or_create(name=row[11])
        crew.two = rower

        bow, created = Rower.objects.get_or_create(name=row[12])
        crew.bow = bow

        crew.save()
