from django.urls import include, path
from bankApi.api import views
from bankApi.api.views import BankDetailAPIView,BankListApiView
from django.conf.urls import url

app_name='bankApi'

urlpatterns=[
path('',views.index,name='list'),
url(r'(?P<name>[\w|\W]+)/(?P<city>[\w|\W]+)/$',BankListApiView.as_view(),name='list'),
url(r'(?P<ifsc>[\w|\W]+)/$',BankDetailAPIView.as_view(),name='detail'),
]