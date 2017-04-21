from django.contrib import admin

from .models import Club
from .models import Crew
from .models import Rower
from .models import Profile

admin.site.register(Club)
admin.site.register(Crew)
admin.site.register(Rower)
admin.site.register(Profile)
