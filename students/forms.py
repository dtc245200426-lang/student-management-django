from django import forms

from .models import Classroom, Student, Score


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = [
            'name',
            'course',
        ]

        labels = {
            'name': 'Tên lớp',
            'course': 'Khóa học',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập tên lớp',
                }
            ),
            'course': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập khóa học',
                }
            ),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            'student_code',
            'full_name',
            'date_of_birth',
            'email',
            'classroom',
        ]

        labels = {
            'student_code': 'Mã sinh viên',
            'full_name': 'Họ và tên',
            'date_of_birth': 'Ngày sinh',
            'email': 'Email',
            'classroom': 'Lớp',
        }

        widgets = {
            'student_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập mã sinh viên',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập họ và tên',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập Email',
                }
            ),
            'classroom': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['classroom'].empty_label = '-- Chọn lớp --'


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score

        fields = [
            'student',
            'subject',
            'score',
        ]

        labels = {
            'student': 'Sinh viên',
            'subject': 'Môn học',
            'score': 'Điểm',
        }

        widgets = {
            'student': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập tên môn học',
                }
            ),
            'score': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nhập điểm từ 0 đến 10',
                    'min': '0',
                    'max': '10',
                    'step': '1',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['student'].empty_label = '-- Chọn sinh viên --'