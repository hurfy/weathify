from django.urls   import path
from weather.views import main_page, page_not_found


urlpatterns = [
    path('', main_page)
]
