from django.urls import path
from mypage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creative.html', views.creative, name='creative'),
    path('peer1.html', views.peer1, name='peer1'),
    path('peer2.html', views.peer2, name='peer2'),
    path('peer3.html', views.peer3, name='peer3'),
    path('checkscreative.html', views.room, name='checkscreative'),
    path('test.html', views.test, name='test'),
    path('test-creative.html', views.test_creative, name='test_creative'),
]
