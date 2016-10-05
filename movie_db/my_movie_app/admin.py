from django.contrib import admin
from my_movie_app.models import Item, Rater, Data

# Register your models here.
admin.site.register([Item, Rater, Data])
