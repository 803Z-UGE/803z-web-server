from accounts.serializers import AskPasswordSerializer, TokenSerializer, UserSerializer, LoginSerializer, ResetPasswordSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class AccountViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @extend_schema(
        request=LoginSerializer,
        responses={200: TokenSerializer},
        operation_id='account_login',
        description='Login user and return authentication token.'
    )
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], serializer_class=LoginSerializer)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            User = get_user_model()
            try:
                user = User.objects.get(username=email)
                if user.check_password(password):
                    token, created = Token.objects.get_or_create(user=user)
                    # user.last_login = timezone.now()
                    # user.save(update_fields=['last_login'])
                    return Response({'token': token.key})
            except User.DoesNotExist:
                pass
            return Response({'error': 'Invalid credentials'}, status=400)
        return Response({'error': 'Invalid request'}, status=400)
    
    @extend_schema(
        responses={200: UserSerializer},
        operation_id='account_details',
    )
    @action(detail=False, methods=['get'])
    def signup(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @extend_schema(
        request=AskPasswordSerializer,
        responses={200: {'message': 'Password reset link sent'}, 404: {'error': 'User not found'}},
        operation_id='account_ask_password',
        description='Ask for password reset by sending a link to the user\'s email.'
    )
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], serializer_class=AskPasswordSerializer)
    def ask_password(self, request, *args, **kwargs):
        email = request.data.get('email')
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            # Here you would implement the logic to send a password reset email
            return Response({'message': 'Password reset link sent'}, status=200)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        
    @extend_schema(
        request=ResetPasswordSerializer,
        responses={200: {'message': 'Password has been reset'}, 404: {'error': 'User not found'}},
        operation_id='account_reset_password',
        description='Reset user password using the provided email token.'
    )
    @action(detail=False, methods=['post'], serializer_class=ResetPasswordSerializer)
    def reset_password(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
                # Here you would implement the logic to reset the password
                # TODO : do not forget to use a temporary token for security
                return Response({'message': 'Password has been reset'}, status=200)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response(serializer.errors, status=400)
    
    @extend_schema(
        responses={200: UserSerializer},
    )
    @action(detail=False, methods=['get'])
    def myself(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
