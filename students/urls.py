from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    # Lớp
    path(
        'classrooms/',
        views.classroom_list,
        name='classroom_list',
    ),
    path(
        'classrooms/add/',
        views.classroom_create,
        name='classroom_create',
    ),
    path(
        'classrooms/<int:pk>/edit/',
        views.classroom_update,
        name='classroom_update',
    ),
    path(
        'classrooms/<int:pk>/delete/',
        views.classroom_delete,
        name='classroom_delete',
    ),

    # Sinh viên
    path(
        'students/',
        views.student_list,
        name='student_list',
    ),
    path(
        'students/add/',
        views.student_create,
        name='student_create',
    ),
    path(
        'students/<int:pk>/edit/',
        views.student_update,
        name='student_update',
    ),
    path(
        'students/<int:pk>/delete/',
        views.student_delete,
        name='student_delete',
    ),

    # Điểm
    path(
        'scores/',
        views.score_list,
        name='score_list',
    ),
    path(
        'scores/add/',
        views.score_create,
        name='score_create',
    ),
    path(
        'scores/<int:pk>/edit/',
        views.score_update,
        name='score_update',
    ),
    path(
        'scores/<int:pk>/delete/',
        views.score_delete,
        name='score_delete',
    ),
]