import os.path


try:
    import cPickle as pickle
except:
    import pickle


from oauthlib.oauth2 import TokenExpiredError
from requests_oauthlib import OAuth2Session

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings as django_settings

# from huiwan.activities.models import Activity
# from huiwan.reviews.models import Review


class Profile(models.Model):
    user = models.OneToOneField(User)
    public_email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)

    class Meta:
        db_table = 'auth_profile'

    def get_url(self):
        url = self.url
        if "http://" not in self.url and "https://" not in self.url and len(self.url) > 0:
            url = "http://" + str(self.url)
        return url

    def get_picture(self):
        no_picture = django_settings.STATIC_URL + 'img/user.png'
        try:
            filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + self.user.username + '.jpg'
            picture_url = django_settings.MEDIA_URL + 'profile_pictures/' + self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                return no_picture
        except Exception, e:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username

    def get_reviews(self):
        user_reviews = []
        author_reviews = Review.objects.filter(author=self.user)
        co_author_reviews = Review.objects.filter(co_authors=self.user)
        for r in author_reviews: user_reviews.append(r)
        for r in co_author_reviews: user_reviews.append(r)
        user_reviews.sort(key=lambda r: r.last_update, reverse=True)
        return user_reviews

    """
    def get_followers(self):
        activities = Activity.objects.filter(to_user__pk=self.pk, activity_type=Activity.FOLLOW)
        followers = []
        for activity in activities:
            followers.append(activity.from_user)
        return followers

    def get_followers_count(self):
        followers_count = Activity.objects.filter(to_user__pk=self.pk, activity_type=Activity.FOLLOW).count()
        return followers_count

    def get_following(self):
        activities = Activity.objects.filter(from_user__pk=self.pk, activity_type=Activity.FOLLOW)
        following = []
        for activity in activities:
            following.append(activity.to_user)
        return following

    def get_following_count(self):
        following_count = Activity.objects.filter(from_user__pk=self.pk, activity_type=Activity.FOLLOW).count()
        return following_count
    """

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
