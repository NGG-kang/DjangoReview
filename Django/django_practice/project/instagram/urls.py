from django.urls import path, re_path, register_converter
from . import views

class YearConverter:
    regex = r'\d+'

    def to_python(self,value):
        return int(value)

    def to_url(self, value):
        return str(value)

register_converter(YearConverter, 'year')
urlpatterns=[
    path('', views.post_list),
    path('archives/<year:year>/'),
    re_path(r'archives/(?P<year>\d+)/'),
]