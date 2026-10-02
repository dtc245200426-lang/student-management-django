from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Classroom(models.Model):
    name = models.CharField(
        'Tên lớp',
        max_length=100,
        unique=True
    )

    course = models.CharField(
        'Khóa học',
        max_length=50
    )

    class Meta:
        verbose_name = 'Lớp học'
        verbose_name_plural = 'Lớp học'
        ordering = ['name']

    def __str__(self):
        return self.name


class Student(models.Model):
    student_code = models.CharField(
        'Mã sinh viên',
        max_length=20,
        unique=True
    )

    full_name = models.CharField(
        'Họ và tên',
        max_length=150
    )

    date_of_birth = models.DateField(
        'Ngày sinh'
    )

    email = models.EmailField(
        'Email'
    )

    classroom = models.ForeignKey(
        Classroom,
        verbose_name='Lớp',
        on_delete=models.CASCADE,
        related_name='students'
    )

    class Meta:
        verbose_name = 'Sinh viên'
        verbose_name_plural = 'Sinh viên'
        ordering = ['student_code']

    def __str__(self):
        return f'{self.student_code} - {self.full_name}'


class Score(models.Model):
    student = models.ForeignKey(
        Student,
        verbose_name='Sinh viên',
        on_delete=models.CASCADE,
        related_name='scores'
    )

    subject = models.CharField(
        'Môn học',
        max_length=100
    )

    score = models.PositiveSmallIntegerField(
        'Điểm',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        verbose_name = 'Điểm'
        verbose_name_plural = 'Điểm'
        ordering = ['student', 'subject']

    def __str__(self):
        return (
            f'{self.student.student_code} - '
            f'{self.subject}: {self.score}'
        )