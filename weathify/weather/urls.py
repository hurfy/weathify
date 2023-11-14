from django.urls   import path
from weather.views import main_page


urlpatterns = [
    path('', main_page),
]
