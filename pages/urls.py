from django.urls import path
from .views import HomePageView, AboutPageView

ROOT_URLCONF = 'pages.urls'

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('about/', AboutPageView.as_view(), name='about'),
]