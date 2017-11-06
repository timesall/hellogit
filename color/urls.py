from django.conf.urls import url
from .views import index,mingMing,getTest,getTestName#noName

urlpatterns = [url(r'^index/',index),
               #url(r'^(\w+)',noName),
               url(r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,4})',mingMing),
               url(r'getTest/',getTest),
               url(r'getTestName/(?P<date>\d{4})/',getTestName)
               ]