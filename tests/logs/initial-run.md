# Lần chạy đầu – 22/10/2026

Validator báo `Description is absent or too short`; unittest thực chạy 23, đạt 22, lỗi 1 (`test_package`).

Nguyên nhân: regex đọc description có `^` sau dòng name nhưng thiếu cờ MULTILINE; YAML đầu vào hợp lệ, lỗi thuộc validator. Sửa bộ đọc regex để nhận khóa ở đầu dòng, giữ nguyên mô tả skill. `test_package` là regression cho cấu trúc có name trước description và folded scalar. Kết quả sau sửa xem final-unittest.log.
