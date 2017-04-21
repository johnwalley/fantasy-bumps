from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Club(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Rower(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Crew(models.Model):
    boat = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    club = models.ForeignKey(Club)
    GENDER_CHOICES = (
        ('female', 'female'),
        ('male', 'male'),
    )
    gender = models.CharField(
        max_length=200,
        choices=GENDER_CHOICES
    )
    cox = models.ForeignKey(Rower, related_name="cox", null=True, default=None)
    stroke = models.ForeignKey(Rower, related_name="stroke", null=True, default=None)
    seven = models.ForeignKey(Rower, related_name="seven", null=True, default=None)
    six = models.ForeignKey(Rower, related_name="six", null=True, default=None)
    five = models.ForeignKey(Rower, related_name="five", null=True, default=None)
    four = models.ForeignKey(Rower, related_name="four", null=True, default=None)
    three = models.ForeignKey(Rower, related_name="three", null=True, default=None)
    two = models.ForeignKey(Rower, related_name="two", null=True, default=None)
    bow = models.ForeignKey(Rower, related_name="bow", null=True, default=None)
    result_1 = models.IntegerField(null=True)
    result_2 = models.IntegerField(null=True)
    result_3 = models.IntegerField(null=True)
    result_4 = models.IntegerField(null=True)

    def __str__(self):
        return str(self.club) + " " + self.boat


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cox = models.ForeignKey(Rower, related_name="profile_cox", null=True, default=None)
    stroke = models.ForeignKey(Rower, related_name="profile_stroke", null=True, default=None)
    seven = models.ForeignKey(Rower, related_name="profile_seven", null=True, default=None)
    six = models.ForeignKey(Rower, related_name="profile_six", null=True, default=None)
    five = models.ForeignKey(Rower, related_name="profile_five", null=True, default=None)
    four = models.ForeignKey(Rower, related_name="profile_four", null=True, default=None)
    three = models.ForeignKey(Rower, related_name="profile_three", null=True, default=None)
    two = models.ForeignKey(Rower, related_name="profile_two", null=True, default=None)
    bow = models.ForeignKey(Rower, related_name="profile_bow", null=True, default=None)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
