# Changelog

## 1.0.0 – 22/10/2026

- Tái cấu trúc lõi PRO 5.0 cũ thành lesson-planning-nls-ai; tách điều phối, references, assets và QA.
- Bổ sung ánh xạ NLS đến bước đánh giá, nguồn/mức/trang; không phát hành registry mã chưa xác minh.
- Chuẩn hóa năm nhóm AI thành phân loại nội bộ thay vì “năm mức”; cập nhật điểm kiểm tra khung AI Việt Nam năm 2026.
- Thay mặc định cũ 35–40 phút bằng giả định lập kế hoạch 35 phút tiểu học khi chưa có thông tin khác.
- Làm rõ ưu tiên học liệu người dùng không ghi đè quy định chính thức; nguồn cốt lõi unknown không qua hard gate.
- Thêm thang QA 100 điểm, test tự động và forward test có đầu vào/đầu ra lưu lại; kết quả chi tiết trong tests/results.md.
- Chưa kiểm nghiệm lớp học và xuất Word/PDF; chưa lựa chọn giấy phép.

- Sửa lỗi V01 bộ kiểm tra description YAML sau lần chạy đầu (22/23); chạy hồi quy sau sửa đạt 23/23. Thêm fixture PDF tự soạn để kiểm thử đọc học liệu; không coi là SGK chính thức.

- Sau forward test, siết câu hỏi tối thiểu: không xin kèm thiết bị/thời lượng khi thiếu môn/lớp/chủ đề; thiếu chủ đề không tự chọn một bài dù có nhãn giả định. Lưu đầu ra đầu TC13/TC16 và chạy lại bằng ngữ cảnh mới.

- Thích ứng validator với thư mục skill-ID do dịch vụ Skills tự chuẩn hóa; giữ kiểm tra tên chuẩn ở repository. Thêm hồi quy, tổng 24 unittest.
