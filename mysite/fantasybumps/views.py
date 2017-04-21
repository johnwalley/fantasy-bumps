from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import Crew
from .models import Rower
from .models import Profile


def get_points(rower_id):
    crew = Crew.objects.get(Q(stroke_id=rower_id) | Q(seven_id=rower_id) | Q(six_id=rower_id) | Q(
        five_id=rower_id) | Q(four_id=rower_id) | Q(three_id=rower_id) | Q(two_id=rower_id) | Q(bow_id=rower_id))
    return crew.result_1 + crew.result_2 + crew.result_3 + crew.result_4


def index(request):
    crew_list = Crew.objects.order_by('club')
    context = {'crew_list': crew_list}
    return render(request, 'fantasybumps/index.html', context)


def crew_detail(request, crew_id):
    crew = get_object_or_404(Crew, pk=crew_id)
    return render(request, 'fantasybumps/crew_detail.html', {'crew': crew})


def rower_detail(request, rower_id):
    rower = Rower.objects.get(id=rower_id)
    crew_list = list(rower.cox.all()) + list(rower.stroke.all()) + list(rower.seven.all()) + list(rower.six.all()) + list(
        rower.five.all()) + list(rower.four.all()) + list(rower.three.all()) + list(rower.two.all()) + list(rower.bow.all())
    return render(request, 'fantasybumps/rower_detail.html', {'rower': rower, 'crew_list': crew_list})


def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
        
    profile.points = 0

    crew = Crew.objects.get(cox_id=profile.cox.id)
    profile.points += crew.result_1 + crew.result_2 + crew.result_3 + crew.result_4

    profile.points += get_points(profile.stroke.id)
    profile.points += get_points(profile.seven.id)
    profile.points += get_points(profile.six.id)
    profile.points += get_points(profile.five.id)
    profile.points += get_points(profile.four.id)
    profile.points += get_points(profile.three.id)
    profile.points += get_points(profile.two.id)
    profile.points += get_points(profile.bow.id)

    return render(request, 'fantasybumps/profile_detail.html', {'profile': profile})


def table(request):
    profile_list = Profile.objects.order_by('user')

    for profile in profile_list:
        profile.points = 0

        crew = Crew.objects.get(cox_id=profile.cox.id)
        profile.points += crew.result_1 + crew.result_2 + crew.result_3 + crew.result_4

        profile.points += get_points(profile.stroke.id)
        profile.points += get_points(profile.seven.id)
        profile.points += get_points(profile.six.id)
        profile.points += get_points(profile.five.id)
        profile.points += get_points(profile.four.id)
        profile.points += get_points(profile.three.id)
        profile.points += get_points(profile.two.id)
        profile.points += get_points(profile.bow.id)

    context = {'profile_list': profile_list}
    return render(request, 'fantasybumps/table.html', context)
