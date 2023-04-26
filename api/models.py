from django.db import models
from django.contrib.auth.models import User


# todo przerobić sport z wyboru w instruktorze na osobny model -> użycie w zajęciach lub w rezerwacji
# todo skończyć rezerwacje

class Student(models.Model):
    """
    Osoby biorące udział w zajęciach.
    """
    user = models.ForeignKey(
        User,
        related_name='students',
        on_delete=models.CASCADE
    )
    name = models.CharField()
    birth_date = models.DateField()
    phone = models.CharField(
        max_length=9,
        blank=True
    )


class Language(models.Model):
    """
    Języki prowadzenia zajęć.
    """
    język = models.CharField(unique=True)


class Qualification(models.Model):
    """
    Kwalifikacje instruktorskie.
    """
    name = models.CharField(unique=True)
    description = models.TextField()


class Instructor(models.Model):
    """
    Instruktorzy pracujący w szkółkach.
    """
    user = models.ForeignKey(
        User,
        unique=True,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(

    )
    SPORTS_CHOICES = [
        ("SKI", "Ski"),
        ("SNB", "Snowboard"),
        ("BTH", "Both")
    ]
    sports = models.CharField(
        max_length=3,
        choices=SPORTS_CHOICES,
        default="SKI"
    )
    languages = models.ManyToManyField(
        Language,
        related_name='instructors'
    )
    qualifications = models.ManyToManyField(
        Qualification,
        related_name='instructors'
    )
    q_expiration = models.DateField()
    commission = models.DecimalField(
        min=0,
        max=1,
        decimal_places=2
    )


class Address(models.Model):
    """
    Adresy szkółek narciarskich.
    """
    city = models.CharField()
    street = models.CharField()
    number = models.CharField()
    postal_code = models.CharField()


class School(models.Model):
    """
    Szkółki narciarskie.
    """
    owner = models.ForeignKey(
        User,
        unique=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        unique=True,
    )
    picture = models.ImageField(

    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )
    instructors = models.ManyToManyField(
        Instructor,
        related_name='schools'
    )
    phone = models.CharField(
        max_length=9,
    )


class ClassType(models.Model):
    """
    Rodzaje zajęć prowadzonych w szkółkach i ich ceny.
    """
    school = models.ForeignKey(
        School,
        unique=True,
        on_delete=models.CASCADE
    )
    name = models.CharField()
    students = models.IntegerField()
    hours = models.IntegerField()
    class_price = models.DecimalField(
        min=0,
        decimal_places=2
    )
    fees = models.TextField()
    total_price = models.DecimalField(
        min=0,
        decimal_places=2
    )


class Calendar(models.Model):
    """
    Dostępność instruktorów.
    """
    instructor = models.ForeignKey(
        Instructor,
        related_name='times',
        on_delete=models.CASCADE
    )
    school = models.ForeignKey(
        School,
        related_name='calendars',
        on_delete=models.CASCADE
    )
    start = models.DateTimeField()
    end = models.DateTimeField()


class Reservation(models.Model):
    """
    Zarezerwowane zajęcia.
    """
    client = models.ForeignKey(
        User,
        related_name='client_classes',
        on_delete=models.CASCADE
    )
    instructor = models.ForeignKey(
        Instructor,
        related_name='instructor_classes',
        on_delete=models.CASCADE
    )
    students = models.ManyToManyField(
        Student,
        related_name='student_classes'
    )
