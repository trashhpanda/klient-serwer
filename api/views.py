from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, GroupSerializer, LoginSerializer, ClientProfileSerializer


@api_view(['POST'])
def user_registration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'username': serializer.data['username']}, status=201)
    print("henlo dis error:")
    print(serializer.errors)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_groups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'success': True, 'username': user.username})
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'success': True})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_profile_view(request):
    user = request.user
    serializer = ClientProfileSerializer(user)

    return Response(serializer.data)

