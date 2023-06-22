from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

from api.models import Student, Booking


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


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'birth_date', 'phone')


class ClientBookingSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Booking
        fields = ('instructor', 'students', 'start', 'class_type', 'client_notes', 'status')


class ClientProfileSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    booked_classes = ClientBookingSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'students', 'booked_classes')
