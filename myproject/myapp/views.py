from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Seller, Ticket, SoldTicket
from .serializers import UserSignupSerializer, SellerSignupSerializer, TicketSerializer, SoldTicketSerializer

class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Signup successful',
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SellerSignupView(generics.CreateAPIView):
    serializer_class = SellerSignupSerializer
    def post(self, request, *args, **kwargs):
        return Response({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)

class UserSigninView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({'error': 'Please provide both email and password'}, status=400)
        
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Signin successful',
                    'token': str(refresh.access_token),
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    }
                })
            return Response({'error': 'Invalid password'}, status=400)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

class SellerSigninView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) and user.is_seller:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Signin successful',
                    'token': str(refresh.access_token)
                })
            return Response({'error': 'Invalid credentials'}, status=400)
        except User.DoesNotExist:
            return Response({'error': 'Seller not found'}, status=404)

class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    def get_queryset(self):
        return Ticket.objects.all()
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.seller)

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

class BuyTicketView(generics.CreateAPIView):
    serializer_class = SoldTicketSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        return Response({'message': 'Ticket purchased successfully.'}, status=status.HTTP_201_CREATED)

