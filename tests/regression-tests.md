# Hồi quy

| Nhóm | Liên kết lỗi | Tình huống/test |
|---|---|---|
| TC01 | F07,F09 | Xem expected-results.md và actual/TC01.md |
| TC02 | F07,F08 | Xem expected-results.md và actual/TC02.md |
| TC03 | F10,F13 | Xem expected-results.md và actual/TC03.md |
| TC04 | F02,F07 | Xem expected-results.md và actual/TC04.md |
| TC05 | F09,F10 | Xem expected-results.md và actual/TC05.md |
| TC06 | F01,F10 | Xem expected-results.md và actual/TC06.md |
| TC07 | F02,F03 | Xem expected-results.md và actual/TC07.md |
| TC08 | F03,F06 | Xem expected-results.md và actual/TC08.md |
| TC09 | F10,F14 | Xem expected-results.md và actual/TC09.md |
| TC10 | F07,F14 | Xem expected-results.md và actual/TC10.md |
| TC11 | F01,F10 | Xem expected-results.md và actual/TC11.md |
| TC12 | F08 | Xem expected-results.md và actual/TC12.md |
| TC13 | F02,F03 | Xem expected-results.md và actual/TC13.md |
| TC14 | F01,F03 | Xem expected-results.md và actual/TC14.md |
| TC15 | F06,F09 | Xem expected-results.md và actual/TC15.md |
| TC16 | F13,F14 | Xem expected-results.md và actual/TC16.md |
| Validator mô tả YAML | V01, lỗi thực chạy | test_package; logs/initial-run.md |
| Chặn thông qua | HG1–HG5 fail/unknown | test_each_hard_gate_failure, test_unknown_not_pass |
| Nguồn cốt lõi | Unknown | test_core_source_blocks |
| Thời gian | F06 | test_overtime_blocks, test_undertime_blocks, test_negative_minutes_invalid |
| Biểu mẫu sai | Điểm, boolean, NaN, thiếu trường | test_validator.py |
| Cấu trúc gói | Link thoát thư mục, thiếu resource, sai name | test_escape_link, test_missing_resource, test_invalid_name |

Sau sửa chỉ dẫn hành vi, chạy lại ca chịu ảnh hưởng bằng ngữ cảnh mới. Test schema không thay cho việc chạy lại agent. Lỗi dự đoán không được nâng thành sự cố thực tế chỉ vì có test mang cùng tên.

TC17: đọc học liệu PDF được cung cấp; đối chiếu fixtures và đầu ra actual/TC17.md. Không thay thế kiểm thử OCR bản scan hoặc xuất giáo án PDF.

F18/F19: giữ tests/initial/TC13.md và TC16.md; đối chiếu với tests/actual sau khi sửa. Không hỏi kèm thông tin tùy chọn, không tự chọn chủ đề để viết bài khi thiếu.
