from django.contrib import admin

from .models import Classroom, Student, Score


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'course',
    )

    search_fields = (
        'name',
        'course',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_code',
        'full_name',
        'date_of_birth',
        'email',
        'classroom',
    )

    search_fields = (
        'student_code',
        'full_name',
        'email',
    )

    list_filter = (
        'classroom',
    )


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'score',
    )

    search_fields = (
        'student__student_code',
        'student__full_name',
        'subject',
    )

    list_filter = (
        'subject',
    )