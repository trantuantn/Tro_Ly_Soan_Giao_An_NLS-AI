# Sổ feedback và yêu cầu

Không có phản hồi giáo viên sau dạy được cung cấp. Các dòng dưới là yêu cầu gốc, không phải bằng chứng hài lòng hay lỗi thực địa. Nguyên nhân là nhu cầu thiết kế, chưa chẩn đoán sự cố lớp học.

| ID | Nguồn/ngày | Vấn đề | Mức | Nguyên nhân | Khắc phục | Xác minh | Hồi quy |
|---|---|---|---|---|---|---|---|
| R01 | Tệp nhiệm vụ, 22/10/2026 | Không bịa mã và lịch sử | Chặn phát hành | Thiếu nguồn dễ bị lấp bằng suy đoán | Unknown không pass, sổ nguồn | Đã đưa vào hướng dẫn; xem kết quả thử | TC12, TC13 |
| R02 | Tệp nhiệm vụ, 22/10/2026 | Không ép AI | Cao | Tích hợp hình thức có thể lệch mục tiêu | Cho phép không AI đạt QA đầy đủ | Cần đối chiếu hành vi qua test | TC01 |
| R03 | Tệp nhiệm vụ, 22/10/2026 | Không báo push khi chưa xác minh | Chặn báo cáo | Lệnh thành công chưa đủ chứng minh remote | Kiểm tra SHA/ref/tree sau ghi | Kết quả trong report | Quy trình phát hành |

Mẫu tiếp nhận mới: nguồn có thể truy lại; ngày nếu có; giáo án/phiên bản; vấn đề; mức; bước tái hiện; nguyên nhân đã xác minh hay giả thuyết; sửa; bằng chứng sau sửa; trạng thái; regression ID. Không công khai thông tin HS hoặc người phản hồi khi chưa được phép.


## Phát hiện QA trong phiên xây dựng (không phải feedback giáo viên)

| ID | Nguồn/ngày | Vấn đề | Mức | Nguyên nhân | Khắc phục | Xác minh | Hồi quy |
|---|---|---|---|---|---|---|---|
| Q01 | Tool output unittest, 22/10/2026 | Description hợp lệ bị từ chối | Cao | Regex thiếu MULTILINE | Sửa cờ regex | Chạy cuối đạt | test_package |
| Q02 | Đọc TC13 đầu, 22/10/2026 | Hỏi thêm trường không thiết yếu | Vừa | “Tối thiểu” chưa ràng buộc đủ | Chỉ hỏi trường cốt lõi còn thiếu | Fresh retest đạt | TC13 |
| Q03 | Đọc TC16 đầu, 22/10/2026 | Tự chọn chủ đề khi thiếu | Cao | Nhãn giả định bị dùng để lấp cốt lõi | Không chọn bài; khung và phần tổ chức | Fresh retest đạt | TC16 |
