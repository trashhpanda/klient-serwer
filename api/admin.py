from django.contrib import admin
# modele z aplikacji api
from .models import Student, Language, Qualification, Instructor, Address, School, ClassType, Calendar, Booking

# dostęp do modeli z panelu admina
admin.site.register(Student)
admin.site.register(Language)
admin.site.register(Qualification)
admin.site.register(Instructor)
admin.site.register(Address)
admin.site.register(School)
admin.site.register(ClassType)
admin.site.register(Calendar)
admin.site.register(Booking)
