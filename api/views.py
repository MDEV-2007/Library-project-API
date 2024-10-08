from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import status

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# class BookAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    
class BookCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class BookDetailView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
      
    
class BookDeleteView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

class BookUpdateView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        



class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

Hello eveyone