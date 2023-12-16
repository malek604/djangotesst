from django.contrib.auth.models import User




def sighnup(username,email,password):
    user=User.objects.create_user(username,email,password)
    user.save()

