from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, GroupSerializer


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
