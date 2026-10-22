# Bài học và mức bằng chứng

| ID | Nguyên tắc | Cơ sở | Điều kiện/giới hạn |
|---|---|---|---|
| L01 | Tách chỉ dẫn thiết kế khỏi kết quả thực địa | Audit bản PRO 5.0 cũ có chỉ dẫn, không có dữ liệu dạy | Đã kiểm tra loại nguồn; chưa chứng minh hiệu quả |
| L02 | Mã phải truy ngược nguồn/mức/trang | Yêu cầu người dùng và nguồn S3 | Quy tắc phòng ngừa; cần thẩm định từng mã lúc soạn |
| L03 | NLS cần hành vi HS và đánh giá | Yêu cầu người dùng và hướng dẫn tích hợp S3 | GV dùng slide không đủ bằng chứng năng lực HS |
| L04 | Năm nhóm AI không phải năm mức chính thức | So sánh bản cũ với UNESCO S4 | Đã xác minh khác biệt cấu trúc; ánh xạ trong skill là đề xuất |
| L05 | Văn bản phụ thuộc năm học | Nguồn S6 nhận diện hướng dẫn 2026 | Đã phát hiện nguồn mới; phụ lục gốc chưa được thẩm định |
| L06 | Không tự thông qua khi thiếu nguồn trọng tâm | Thiết kế quality gate | Quy tắc nội bộ, chưa phải chuẩn công nhận của Bộ |
| L07 | Không AI vẫn có thể là giáo án tốt | Yêu cầu không ép AI và thiết kế rubric | Cần minh chứng lý do; không thưởng dùng công cụ |
| L08 | Thiết bị dự phòng có giới hạn minh chứng | Phân tích tác vụ thực hành số | Mô phỏng giấy không chứng minh thao tác trên hệ thống số |

Những điểm có bằng chứng chỉ chứng minh audit hoặc hành vi trên tình huống đã chạy. Thêm bài học thực tế sau khi có giáo án, dữ liệu quan sát, phản hồi và điều kiện áp dụng. Xem tests/results.md và success-patterns.md để biết mức kiểm chứng của bản phát hành.


## Bài học mới từ thử nghiệm phát hành

L09: Chỉ dẫn “hỏi tối thiểu” còn có thể bị hiểu là xin thêm trường tùy chọn (TC13 đầu). L10: gắn nhãn giả định chưa đủ khi giả định quyết định cả chủ đề bài (TC16 đầu). Siết rõ chỉ hỏi phần cốt lõi còn thiếu, không tự chọn bài, tiếp tục phần tổ chức độc lập. Hai ca chạy lại bằng ngữ cảnh mới đáp ứng tiêu chí, bằng chứng trong tests/actual và tests/initial. Đây là cải thiện hành vi trên hai ca, chưa chứng minh khái quát cho mọi câu hỏi.
