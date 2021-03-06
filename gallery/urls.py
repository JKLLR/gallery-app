from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name = 'home'),
    path('search/', views.search_results, name='search_results'),
    path('category/(<category_id>\d+)',views.category,name ='category'),
    path('location/(<location_id>\d+)',views.location,name ='location'),
    path('image/(<image_id>\d+)',views.image,name ='image'),
]        

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)