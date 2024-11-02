from django.urls import path
from mypage import views

urlpatterns = [
    path('',views.index, name='index'),
    path('creative.html',views.creative),
    path('peer1.html',views.peer1),
    path('peer2.html',views.peer2),
    path('peer3.html', views.peer3),
    path('index.html',views.index, name='index_html'),
    path('checkscreative.html',views.room),
    path('test.html', views.test),
    path('test-creative.html', views.test_creative)
]
