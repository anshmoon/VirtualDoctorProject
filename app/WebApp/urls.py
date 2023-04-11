from django.urls import path,include
from . import views
from . import views
urlpatterns=[
    path('',views.appindex,name='app-index'),
    path('trial',views.trial,name='trial'),
    path('heart/',views.heart,name='heart'),
    path('hresult/',views.heartDiseasesPredictionResult,name='hresult'),
    path('paper/',views.paper,name='paper')
   
   
]
