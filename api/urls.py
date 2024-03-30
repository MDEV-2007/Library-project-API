from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListView,BookCreateView,BookDetailView,BookDeleteView,BookUpdateView,BookViewset


router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    # path('', BookAPIView.as_view()),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteView.as_view()),
    path('books/<int:pk>/update/', BookUpdateView.as_view()),
    path('books/create/', BookCreateView.as_view(), name='create'),

]


urlpatterns = urlpatterns + router.urls