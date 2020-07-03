from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from bankApi.models import Bank
from bankApi.api.serializer import BankSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

def index(request):
    return HttpResponse('Welcome:   ')
    
class BankDetailAPIView(RetrieveAPIView):
    queryset=Bank.objects.all()
    serializer_class=BankSerializer
    lookup_field='ifsc'
    lookup_url_kwarg="ifsc"

    def get(self,*args,**kwargs):
        uid=Bank.objects.filter(ifsc=self.kwargs['ifsc']).values('ifsc','bank_id','branch','address','city','district','state','name')
        print(uid)
        if uid:
            return Response({'ifsc':uid[0]['ifsc'],'bank_id':uid[0]['bank_id'],'branch':uid[0]['branch'],'address':uid[0]['address'],'city':uid[0]['city'],'district':uid[0]['district'],'state':uid[0]['state'],'name':uid[0]['name']},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'ifsc':'not found'},status=status.HTTP_202_ACCEPTED)

class BankListApiView(ListAPIView):
    serializer_class = BankSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    def get_queryset(self):
        name = self.kwargs['name']
        city = self.kwargs['city']
        queryset = self.model.objects.filter(name=name.upper(),city=city.upper())
        return queryset.order_by('-ifsc')