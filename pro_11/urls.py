from django.urls import path
from .import views
urlpatterns=[
    path('fun',views.fun,name='fun'),
    path('',views.fun_1,name='fun_1'),
    path('people_views',views.people_views,name='people_views'),
    path('people_edit/<int:id1>',views.people_edit,name='people_edit'),
    path('people_delete/<int:id1>',views.people_delete,name='people_delete'),
    path('search',views.search,name='search'),
    path('login',views.login,name='login'),
    path('user_home',views.user_home,name='user_home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('logt',views.logt,name='logt')

]
