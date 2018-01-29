from django.http import Http404
from django.http import HttpResponse
# from rest_framework import viewsets , router, serializers
# from django.template import loader #lecture 15
from django.shortcuts import render, get_object_or_404
from .models import Album
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import AlbumSerializer
def index(request):
    all_albums = Album.objects.all()
    # lecture 15 remove# template = loader.get_template('music/index.html')
    #16rm# context = {'all_albums': all_albums,}
    return render(request, 'music/index.html',{'all_albums': all_albums})
    #lecture 13
    # html = ''
    # for album in all_albums:
    #     url = '/music/' + str(album.id)+'/'
    #     html +='<a href="'+ url +'">'+album.album_title +'</a><br>'
    #lecture 15 Remove
    # return HttpResponse(template.render(context, request))

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    #remove lecture 16 # return HttpResponse("<h2>Details for Album id:"+ str(album_id)+"</h2>")
    #remove 24
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

# lecture   21 remove by shortcut
    # album = get_object_or_404(Album, pk=album_id)
    # try:
    #     selected_song = album.song_set.get(pk=request.Post['song'])
    # except (KeyError, Song.DoesNotExist):
    #     return render(request, 'music/detail.html',{
    #         'album': album,
    #         'error_message': "You did not select a valid song",
    #         })
    # else:
    #     selected_song.is_favorite = True
    #     selected_song.save()
    return render(request,'music/detail.html', {'album': album})

# class Pollserializer(serializers.ModelSerializer):
#     choices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      

# class PollViewSet(viewsets.ModelViewSet):
#     model = Album
#     serializer_class = Pollserializer

class AlbumList(APIView):
    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self):
        pass