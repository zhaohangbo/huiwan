from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

@python_2_unicode_compatible  # only if you need to support Python 2
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    GENDER   = (
                (0,'female'),
                (1,'male'),
                )
    gender   = models.CharField(max_length=10, choices=GENDER)
    is_player= models.BooleanField(default=True)
    is_match_maker = models.BooleanField(default=False)
    # picture = models.ImageField(upload_to='profile_images', blank=True)
    email    = models.CharField(max_length=50)
    mobile   = models.CharField(max_length=20)

    def __str__(self):
        if is_player:
            if gender == 1:
                res += "boy player "
            else:
                res += "girl player "
        if is_match_maker:
            res += "and "
            if gender == 1:
                res += "boy match maker: "
            else:
                res += "girl mathc maker: "
        else:
            res += ": "
        res +=self.username 
        return res 

    def __unicode__(self):
        return self.username

@python_2_unicode_compatible  # only if you need to support Python 2
class Role(models.Model):
    ROLE_TYPES = (
                    ('match_maker' , 'match_maker'),
                    ('player', 'player'),
                 )
    role_type = models.CharField(max_length=20, choices=ROLE_TYPES, default='match_maker')

    def __unicode__(self):
        return self.role_type 
    def __str__(self):
        return self.role_type 
