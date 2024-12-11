
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Seller, Ticket, SoldTicket

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

class SellerSignupSerializer(serializers.ModelSerializer):
    user = UserSignupSerializer()
    class Meta:
        model = Seller
        fields = ('user', 'phone', 'works_at', 'position', 'line1', 'line2', 'district', 'state', 'pincode')
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['is_seller'] = True
        user = UserSignupSerializer().create(user_data)
        seller = Seller.objects.create(user=user, **validated_data)
        return seller

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class SoldTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldTicket
        fields = '__all__'