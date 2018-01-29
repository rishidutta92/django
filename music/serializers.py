from resource import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class meta:
        mdoel = Album
        fields = '__all__'