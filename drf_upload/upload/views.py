from .models import UploadImageTest
from .serializers import EnterpriseModelSerializer, BasicModelSerializer, PremiumModelSerializer, CustomNoImageModelSerializer, CustomModelSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

class ListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BasicModelSerializer

    def get_queryset(self):
        if str(self.request.user.status) == 'Premium':
            self.serializer_class = PremiumModelSerializer
        elif str(self.request.user.status) == 'Enterprise':
            self.serializer_class = EnterpriseModelSerializer
        elif str(self.request.user.status) == 'Basic':
            self.serializer_class = BasicModelSerializer
        else:
            if (self.request.user.status.image_presence) == True:
                self.serializer_class = CustomModelSerializer
            else:
                self.serializer_class = CustomNoImageModelSerializer
        user = self.request.user
        return UploadImageTest.objects.filter(username=user)


class PostView(ListCreateAPIView):
    model = UploadImageTest
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if str(self.request.user.status) == 'Premium':
            return PremiumModelSerializer
        else:
            return CustomModelSerializer


    def get_queryset(self):
        user = self.request.user
        return UploadImageTest.objects.filter(id=0)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=400)
        image = UploadImageTest.objects.create(
            username=request.user,
            image=request.data['image'])

        if str(self.request.user.status) == 'Premium':
            result = PremiumModelSerializer(image)
        elif str(self.request.user.status) == 'Basic':
            result = BasicModelSerializer(image)
        elif str(self.request.user.status) == 'Enterprise':
            result = EnterpriseModelSerializer(image)
        else:
            if (self.request.user.status.image_presence) == True:
                result = CustomModelSerializer(image,context={"thumbnail_size":self.request.user.status.thumbnail_size})
            else:
                result = CustomNoImageModelSerializer(image,context={"thumbnail_size":self.request.user.status.thumbnail_size})
        return Response((result.data), status=201)




