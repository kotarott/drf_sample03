from django.urls import path
from quotes.api.views import QuoteListCreateAPIView, QuoteDetailAPIView

urlpatterns = [
    path('', QuoteListCreateAPIView.as_view(), name='quote-list'),
    path('<int:pk>/', QuoteDetailAPIView.as_view(), name='quote-detail'),
]