from django.contrib import admin
from django.urls import include, path


admin.site.site_header = 'QUẢN TRỊ HỆ THỐNG SINH VIÊN'
admin.site.site_title = 'Quản trị hệ thống'
admin.site.index_title = 'Quản lý dữ liệu'


urlpatterns = [
    # Endpoint để Prometheus thu thập metrics.
    path(
        '',
        include('django_prometheus.urls')
    ),

    # Trang quản trị Django.
    path(
        'quan-tri/',
        admin.site.urls
    ),

    # Website quản lý sinh viên.
    path(
        '',
        include('students.urls')
    ),
]