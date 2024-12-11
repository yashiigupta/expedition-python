
from django.urls import path
from .views import UserSignupView, SellerSignupView, UserSigninView, SellerSigninView, TicketListCreateView, TicketDetailView, BuyTicketView

urlpatterns = [
    # Authentication endpoints
    path('auth/signup/user', UserSignupView.as_view(), name='user-signup'),
    path('auth/signup/seller', SellerSignupView.as_view(), name='seller-signup'),
    path('auth/signin/user', UserSigninView.as_view(), name='user-signin'),
    path('auth/signin/seller', SellerSigninView.as_view(), name='seller-signin'),
    # Ticket endpoints
    path('available-tickets', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('available-tickets/<int:pk>', TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/buy/<int:id>', BuyTicketView.as_view(), name='buy-ticket'),  
]