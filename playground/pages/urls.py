from django.urls import path
from .views import PageList, PageDetail, PageCreate, PageUpdate, PageDelete
pages_patterns = ([
    path('',PageList.as_view(),name="list"),
    path('<int:pk>/<slug:slug>',PageDetail.as_view(), name="detail"),
    path('create/',PageCreate.as_view(), name="create"),
    path('update/<int:pk>/',PageUpdate.as_view(),name="update"),
    path('delete/<int:pk>',PageDelete.as_view(),name="delete")
], 'pages')#Se hace de esta forma paras no agregar "page" en cada name, en el html se llamaria pages:detail, modificar en el url general
    

