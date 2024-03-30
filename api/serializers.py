from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','subtitle', 'author', 'price', 'isbn')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.replace(' ', '').replace('-', '').isalpha():
            raise ValidationError({'title': 'Kitobga kiritilgan malumot xato'})
        
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({'title': 'Kitob mualifi va salavhasi bir xil'})
        
        return data
    

    def validate_price(self, price):
        if price <= 0:
            raise ValidationError({'price': 'Kitob narxi xato kiritilgan'})
        return price