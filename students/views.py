from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from .models import Classroom, Student, Score
from .forms import ClassroomForm, StudentForm, ScoreForm


def home(request):
    context = {
        'classroom_count': Classroom.objects.count(),
        'student_count': Student.objects.count(),
        'score_count': Score.objects.count(),
    }

    return render(
        request,
        'students/home.html',
        context
    )


# =========================
# QUẢN LÝ LỚP
# =========================

def classroom_list(request):
    classrooms = Classroom.objects.all()

    return render(
        request,
        'students/classroom_list.html',
        {
            'classrooms': classrooms
        }
    )


def classroom_create(request):
    form = ClassroomForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()

        return redirect(
            'classroom_list'
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form,
            'title': 'Thêm lớp học',
            'back_url': 'classroom_list',
        }
    )


def classroom_update(request, pk):
    classroom = get_object_or_404(
        Classroom,
        pk=pk
    )

    form = ClassroomForm(
        request.POST or None,
        instance=classroom
    )

    if form.is_valid():
        form.save()

        return redirect(
            'classroom_list'
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form,
            'title': 'Cập nhật lớp học',
            'back_url': 'classroom_list',
        }
    )


def classroom_delete(request, pk):
    classroom = get_object_or_404(
        Classroom,
        pk=pk
    )

    if request.method == 'POST':
        classroom.delete()

        return redirect(
            'classroom_list'
        )

    return render(
        request,
        'students/confirm_delete.html',
        {
            'object': classroom,
            'title': 'Xóa lớp học',
            'back_url': 'classroom_list',
        }
    )


# =========================
# QUẢN LÝ SINH VIÊN
# =========================

def student_list(request):
    students = Student.objects.select_related(
        'classroom'
    ).all()

    return render(
        request,
        'students/student_list.html',
        {
            'students': students
        }
    )


def student_create(request):
    form = StudentForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()

        return redirect(
            'student_list'
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form,
            'title': 'Thêm sinh viên',
            'back_url': 'student_list',
        }
    )


def student_update(request, pk):
    student = get_object_or_404(
        Student,
        pk=pk
    )

    form = StudentForm(
        request.POST or None,
        instance=student
    )

    if form.is_valid():
        form.save()

        return redirect(
            'student_list'
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form,
            'title': 'Cập nhật sinh viên',
            'back_url': 'student_list',
        }
    )


def student_delete(request, pk):
    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == 'POST':
        student.delete()

        return redirect(
            'student_list'
        )

    return render(
        request,
        'students/confirm_delete.html',
        {
            'object': student,
            'title': 'Xóa sinh viên',
            'back_url': 'student_list',
        }
    )


# =========================
# QUẢN LÝ ĐIỂM
# =========================

def score_list(request):
    scores = Score.objects.select_related(
        'student'
    ).all()

    return render(
        request,
        'students/score_list.html',
        {
            'scores': scores
        }
    )


def score_create(request):
    form = ScoreForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Đã lưu điểm thành công.")

        return redirect(
            'score_list'
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form,
            'title': 'Thêm điểm',
            'back_url': 'score_list',
        }
    )


def score_update(request, pk):
    score = get_object_or_404(
        Score,
        pk=pk
    )

    form = ScoreForm(
        request.POST or None,
        instance=score
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Đã lưu điểm thành công.")

        return redirect(
            'score_list'
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form,
            'title': 'Cập nhật điểm',
            'back_url': 'score_list',
        }
    )


def score_delete(request, pk):
    score = get_object_or_404(
        Score,
        pk=pk
    )

    if request.method == 'POST':
        score.delete()
        messages.success(request, "Đã xóa điểm thành công.")

        return redirect(
            'score_list'
        )

    return render(
        request,
        'students/confirm_delete.html',
        {
            'object': score,
            'title': 'Xóa điểm',
            'back_url': 'score_list',
        }
    )