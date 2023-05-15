from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """
    Osoby biorące udział w zajęciach.
    """
    user = models.ForeignKey(
        User,
        related_name='users_students',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50
    )
    birth_date = models.DateField()
    phone = models.CharField(
        max_length=9,
        blank=True
    )


class Language(models.Model):
    """
    Języki prowadzenia zajęć.
    """
    language = models.CharField(
        max_length=50,
        unique=True
    )


class Qualification(models.Model):
    """
    Kwalifikacje instruktorskie.
    """
    name = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.TextField()


class Instructor(models.Model):
    """
    Instruktorzy pracujący w szkółkach.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to='img/instructor/'
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
        related_name='instructors_speaking'
    )
    qualifications = models.ManyToManyField(
        Qualification,
        related_name='instructors_with'
    )
    q_expiration = models.DateField()
    commission = models.DecimalField(
        max_digits=3,
        decimal_places=2
    )


class Address(models.Model):
    """
    Adresy szkółek narciarskich.
    """
    city = models.CharField(
        max_length=50
    )
    street = models.CharField(
        max_length=50
    )
    number = models.CharField(
        max_length=10
    )
    postal_code = models.CharField(
        max_length=6
    )


class School(models.Model):
    """
    Szkółki narciarskie.
    """
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=150,
        unique=True
    )
    picture = models.ImageField(
        upload_to='img/school/'
    )
    address = models.ForeignKey(
        Address,
        related_name='schools_at_address',
        on_delete=models.CASCADE
    )
    instructors = models.ManyToManyField(
        Instructor,
        related_name='works_for_schools'
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
        related_name='offer',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=250
    )
    SPORT_CHOICES = [
        ("SKI", "Ski"),
        ("SNB", "Snowboard")
    ]
    sport = models.CharField(
        max_length=3,
        choices=SPORT_CHOICES,
        default="SKI"
    )
    num_students = models.IntegerField()
    num_hours = models.IntegerField()
    class_price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    fees_description = models.TextField()
    total_price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )


class Calendar(models.Model):
    """
    Dostępność instruktorów.
    """
    instructor = models.ForeignKey(
        Instructor,
        related_name='avaliable',
        on_delete=models.CASCADE
    )
    school = models.ForeignKey(
        School,
        related_name='schedule',
        on_delete=models.CASCADE
    )
    start = models.DateTimeField()
    end = models.DateTimeField()


class Booking(models.Model):
    """
    Zarezerwowane zajęcia.
    """
    client = models.ForeignKey(
        User,
        related_name='booked_classes',
        on_delete=models.CASCADE
    )
    instructor = models.ForeignKey(
        Instructor,
        related_name='teaching_classes',
        on_delete=models.CASCADE
    )
    students = models.ManyToManyField(
        Student,
        related_name='taking_classes'
    )
    start = models.DateTimeField()
    class_type = models.ForeignKey(
        ClassType,
        related_name='booked_like_this',
        on_delete=models.CASCADE
    )
    client_notes = models.TextField()
    instructor_notes = models.TextField()
    STATUS_CHOICES = [
        ("B", "Booked"),
        ("P", "Paid"),
        ("C", "Cancelled"),
        ("A", "Client absent"),
        ("X", "Complete")
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="B"
    )
