from .models import UploadImageTest
from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

class BasicModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('thumbnail200',)

    thumbnail200 = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )


class PremiumModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('thumbnail200', 'thumbnail400', 'image')

    # A thumbnail image, sorl options and read-only
    thumbnail200 = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    thumbnail400 = HyperlinkedSorlImageField(
        '400x400',
        options={"crop": "center"},
        source='image',
        read_only=True
    )


class EnterpriseModelSerializer(serializers.HyperlinkedModelSerializer):
    image_binary = serializers.CharField(source='get_binary')

    class Meta:
        model = UploadImageTest
        fields = ('thumbnail200', 'thumbnail400', 'image', 'image_binary')

    thumbnail200 = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    thumbnail400 = HyperlinkedSorlImageField(
        '400x400',
        options={"crop": "center"},
        source='image',
        read_only=True
    )


class CustomModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UploadImageTest
        fields = ('thumbnail', 'image')

    thumbnail = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )


class CustomNoImageModelSerializer(serializers.HyperlinkedModelSerializer):
    size_of_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = UploadImageTest
        fields = ('thumbnail', 'size_of_thumbnail')

    def get_size_of_thumbnail(self, obj):
        if "thumbnail_size" in self.context:
            size = str(self.context["thumbnail_size"])
            self.size_of_thumbnail = size + "x" + size
            return self.size_of_thumbnail

    thumbnail = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )

