from django.urls import path

from landing.views import IndexView

app_name = 'landing'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

