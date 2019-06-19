from django.urls import path
from app.views import file_content, file_list
from django.urls import register_converter
import datetime
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value.date()


register_converter(DateConverter, 'ymd')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<ymd:date>/', file_list, name='file_list'),
    path('files/<str:name>/', file_content, name='file_content'),
]
