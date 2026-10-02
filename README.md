\# Hệ thống Quản lý Sinh viên



\## 1. Giới thiệu



Hệ thống Quản lý Sinh viên được xây dựng nhằm hỗ trợ quản lý thông tin lớp học, sinh viên và điểm số.



\## 2. Chức năng chính



\- Quản lý lớp học.

\- Thêm, sửa, xóa lớp học.

\- Quản lý sinh viên.

\- Thêm, sửa, xóa sinh viên.

\- Quản lý điểm số.

\- Thêm, sửa, xóa điểm số.



\## 3. Công nghệ sử dụng



\- Python

\- Django

\- MySQL

\- HTML, CSS, Bootstrap

\- Docker và Docker Compose

\- Nginx

\- Prometheus

\- Grafana

\- Loki

\- Promtail



\## 4. Cơ sở dữ liệu



Hệ thống sử dụng MySQL để lưu trữ dữ liệu.



Các bảng nghiệp vụ chính:



\- `students\_classroom`: lưu thông tin lớp học.

\- `students\_student`: lưu thông tin sinh viên.

\- `students\_score`: lưu thông tin điểm số.



\## 5. Triển khai hệ thống



Hệ thống được triển khai bằng Docker Compose với các dịch vụ:



\- Django

\- MySQL

\- phpMyAdmin

\- Nginx

\- Prometheus

\- Grafana

\- Loki

\- Promtail



Khởi động hệ thống:



```bash

docker compose up -d --build

```



Kiểm tra các container:



```bash

docker compose ps

```



\## 6. Truy cập hệ thống



Website:



```text

https://localhost:8443

```



phpMyAdmin:



```text

http://localhost:8081

```



Prometheus:



```text

http://localhost:9090

```



Grafana:



```text

http://localhost:3000

```



\## 7. Giám sát hệ thống



Prometheus được sử dụng để thu thập dữ liệu giám sát từ ứng dụng Django.



Grafana được sử dụng để trực quan hóa:



\- Trạng thái hoạt động của Django.

\- Lưu lượng yêu cầu HTTP.

\- Tốc độ phản hồi HTTP.



Loki và Promtail được sử dụng để thu thập và truy vấn log của các container.



Các truy vấn LogQL đã sử dụng:



```text

{container="qlsv\_django"}

```



```text

{container="qlsv\_django"} |= "GET"

```



```text

{container="qlsv\_django"} |= "ERROR"

```



\## 8. Bảo mật



Hệ thống áp dụng một số biện pháp bảo mật:



\- Sử dụng HTTPS với chứng chỉ self-signed trong môi trường thực hành.

\- Nginx tự động chuyển hướng từ HTTP sang HTTPS.

\- Sử dụng các HTTP Security Header.

\- Sử dụng Content Security Policy.

\- Cookie phiên và cookie CSRF chỉ được truyền qua HTTPS.

\- Django sử dụng cơ chế bảo vệ CSRF.



\## 9. Ghi chú



Chứng chỉ HTTPS được sử dụng là chứng chỉ self-signed phục vụ mục đích học tập và thực hành. Vì vậy trình duyệt có thể hiển thị cảnh báo chứng chỉ khi truy cập lần đầu.

\## 10. Kiểm tra hệ thống



Kiểm tra trạng thái các dịch vụ:



```bash

docker compose ps

```



Kiểm tra cấu hình Nginx:



```bash

docker compose exec nginx nginx -t

```



Kiểm tra chuyển hướng HTTP sang HTTPS:



```bash

curl.exe -I http://localhost:8080

```



Kiểm tra HTTPS và các HTTP Security Header:



```bash

curl.exe -k -I https://localhost:8443

```



Kiểm tra cấu hình triển khai Django:



```bash

docker compose exec django python manage.py check --deploy

```

