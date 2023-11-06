from django.contrib import admin
from django.urls import path, include
from .views import *
from django.http import HttpResponse


# direct, simple way
def yes_view(request):
    return HttpResponse('Yes!')


def no_view(request):
    return HttpResponse('No!')


urlpatterns = [
    path('', output_index_list_view, name='output_list'),
    path('yes/', yes_view, name='yeslxg'),  # for test
    path('no/', no_view, name='nolxg'),  # for test
    path('input/', input_index_view, name='input'),

    # path('delete/', delete_index_list_view, name='delete'),
    path('lxg/', delete_index_list_view, name='delete'),  # lxg as an editor for special function
    path('delete_click_times/', delete_index_list_ordered_by_click_times_view, name='delete_click_times'),
    path('delete_date_created/', delete_index_list_ordered_by_date_created_view, name='delete_date_created'),
    path('delete_last_click_date/', delete_index_list_ordered_by_last_click_date_view, name='delete_last_click_date'),
    path('delete_key_words/', delete_index_list_ordered_by_key_words_view, name='delete_key_words'),

    path('record_click/<int:index_id>/', record_click, name='record_click'),
    path('delete_selected_rows/', delete_selected_rows, name='delete_selected_rows'),

]
