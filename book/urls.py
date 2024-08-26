from django.urls import path
from .views import *

urlpatterns=[
    #function based view
    # path('',book_list,name='book_list'),
    #class based view
    path('',BookListG.as_view(),name='book_list'),
    # path('Add/',book_create,name='book_create'),
    path('Add/',BookCreate.as_view(),name='book_create'),
    path('AddForm/',book_create_from,name='book_create_form'),
    path('AddFormModel/',book_create_formmodel,name='book_create_formmodel'),
    path('Update/<int:id>',book_update,name='book_update'),
    path('Delete/<int:id>',book_delete,name='book_delete'),
    path('<int:id>',book_show,name='book_show'),]