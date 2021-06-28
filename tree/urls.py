from django.urls import path


from . import views

app_name = 'tree'

urlpatterns = [
    path('', views.tree_list, name='tree_list'),
    path('<str:title>/<str:unique_id>/', views.tree_detail, name='tree_detail'),
    path('<str:title>/<str:unique_id>/edit/', views.tree_detail_edit, name='tree_detail_edit'),
    path('create/', views.create_tree, name='create_tree'),
]
