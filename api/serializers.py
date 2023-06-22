from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

from api.models import Student, Booking, Instructor, School, Calendar, ClassType, Address, Language, Qualification


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    group = serializers.SlugRelatedField(slug_field='name', queryset=Group.objects.all(), write_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'password', 'email', 'first_name', 'last_name', 'group'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        group_name = validated_data.pop('group')

        try:
            group = Group.objects.get(name=group_name)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Invalid group name')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        user.groups.add(group)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise serializers.ValidationError('Invalid username or password')

        data['user'] = user
        return data


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('user', 'photo', 'sports', 'languages', 'qualifications', 'q_expiration')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('owner', 'name', 'picture', 'address', 'instructors', 'phone')


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('instructor', 'school', 'start', 'end')


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Student
        fields = ('user', 'name', 'birth_date', 'phone')


class BookingSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    students = StudentSerializer(many=True, read_only=True)
    instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ('client', 'instructor', 'students', 'start', 'class_type', 'client_notes',
                  'instructor_notes', 'status')


class ClientSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    booked_classes = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'students', 'booked_classes')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = ('school', 'name', 'sport', 'num_students', 'num_hours', 'class_price', 'fees_description',
                  'total_price', 'available_start', 'available_end')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'street', 'number', 'postal_code')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('language',)


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('name', 'description')
