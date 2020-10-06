
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.
class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SingleUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer