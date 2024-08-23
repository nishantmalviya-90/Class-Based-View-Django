from api.models import Movie
from api.serializers import MovieSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetail(APIView): 
    def get(self, request,pk): 
        try: 
            movie=Movie.objects.get(pk=pk) 
        except Movie.DoesNotExist: 
            return Response({'msg':'Detail not found'},status=status.HTTP_404_NOT_FOUND) 
        serializer = MovieSerializer(movie) 
        return Response(serializer.data) 
    
    def put(self,request,pk): 
        movie=Movie.objects.get(pk=pk) 
        serializer = MovieSerializer(movie,data=request.data,partial=True) 
        if serializer.is_valid(): 
            serializer.save() 
            # return Response(serializer.data) 
            return Response({'msg':"Data updated successfully"})
        else: return Response(serializer.errors) 
    
    def delete(self,request,pk): 
        movie=Movie.objects.get(pk=pk) 
        movie.delete() 
        return Response({'msg':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)