from django.contrib.auth import login, logout
from django.contrib.auth.models import Group, User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Instructor, School, Calendar, Booking, Student, ClassType, Address, Language, Qualification
from .serializers import UserRegistrationSerializer, GroupSerializer, LoginSerializer, ClientSerializer, \
    InstructorSerializer, SchoolSerializer, CalendarSerializer, BookingSerializer, StudentSerializer, UserSerializer, \
    ClassTypeSerializer, AddressSerializer, LanguageSerializer, QualificationSerializer


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
def client_view(request):
    user = request.user
    serializer = ClientSerializer(user)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def instructors_view(request):
    instructors = Instructor.objects.all()
    serializer = InstructorSerializer(instructors, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def schools_view(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calendar_view(request):
    calendar = Calendar.objects.all()
    serializer = CalendarSerializer(calendar, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_view(request):
    booking = Booking.objects.all()
    serializer = BookingSerializer(booking, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_view(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_view(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def class_type_view(request):
    class_types = ClassType.objects.all()
    serializer = ClassTypeSerializer(class_types, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def address_view(request):
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def language_view(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def qualification_view(request):
    qualifications = Qualification.objects.all()
    serializer = QualificationSerializer(qualifications, many=True)

    return Response(serializer.data)
