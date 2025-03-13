from .models import Member
from .serializers import MemberSerializers
from rest_framework import generics

# Create your views here.
class MemberListCreate(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

class MemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers