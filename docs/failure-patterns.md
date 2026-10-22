# Mẫu lỗi và rủi ro

F16 được xác nhận trong audit tài liệu cũ; F17 là rủi ro được phát hiện qua cập nhật nguồn. F01–F15 là rủi ro phòng ngừa từ yêu cầu, không phải lỗi lớp học đã xảy ra.

| ID | Vấn đề | Dấu hiệu phát hiện | Khắc phục |
|---|---|---|---|
| F01 | Sai chương trình | So YCCĐ với văn bản đúng phiên bản | Đọc lại nguồn môn/lớp |
| F02 | Sai SGK | Trang/bài không có nguồn | Bỏ khẳng định, đối chiếu học liệu |
| F03 | Sai YCCĐ | Mục tiêu tự viết bị gọi là trích chuẩn | Tách YCCĐ và mục tiêu cụ thể |
| F04 | Mục tiêu không đo được | Chỉ nói hiểu/nắm | Đổi thành hành vi và tiêu chí |
| F05 | Thiếu sản phẩm | HS nghe hoặc hứng thú là đầu ra duy nhất | Thêm phiếu/câu giải thích quan sát được |
| F06 | Thời lượng bất khả thi | Tổng phút vượt tiết hoặc quên chuyển tiếp | Cắt mở rộng, giữ mục tiêu lõi |
| F07 | NLS hình thức | Chỉ GV thao tác | Thiết kế hành vi HS hoặc bỏ gán NLS |
| F08 | Bịa mã | Không có trang/mức/chỉ báo | Để mã trống, mô tả dự kiến |
| F09 | AI làm thay tư duy | HS nộp nguyên câu trả lời AI | Yêu cầu tự làm, giải thích và quyết định |
| F10 | Không kiểm chứng AI | Dùng chatbot thứ hai làm xác nhận duy nhất | Đối chiếu SGK/nguồn độc lập/phép tính |
| F11 | Thiếu phân hóa | Một nhiệm vụ đồng nhất không hỗ trợ | Chia bước, nhiệm vụ chuẩn và mở rộng |
| F12 | Thiếu đánh giá | Chỉ GV nhận xét | Thêm đáp án, tiêu chí, công cụ |
| F13 | Không phù hợp tuổi | Ép tài khoản chưa rà soát | GV trung gian, kiểm tra điều khoản |
| F14 | Không có thiết bị | Mọi HS phải có máy/mạng | Luân phiên hoặc phiếu, ghi giới hạn NLS |
| F15 | Lỗi Word/PDF | Font/toán/bảng bị cắt | Render xem từng trang trước bàn giao |
| F16 | Nhầm nhóm AI thành mức | Bản cũ đề mục năm mức phát triển | Đổi thành năm nhóm nội bộ, ghi nguồn đối chiếu |
| F17 | Nguồn cũ bị coi luôn hiện hành | Chỉ dùng khung thí điểm 2025 cho mọi năm | Kiểm tra lại hướng dẫn năm học |

Liên kết tình huống và hồi quy trong tests/regression-tests.md. Không diễn giải số dòng lỗi thành số sự cố thực tế.


## V01 – lỗi validator đã xác nhận và sửa

Lần chạy đầu regex đọc metadata thiếu cờ MULTILINE nên từ chối description YAML hợp lệ. 22/23 unittest đạt, 1 lỗi; sửa bộ đọc, giữ nguyên skill, chạy lại 23/23 đạt. Đây là lỗi công cụ kiểm tra, không phải lỗi giáo án. Log trước/sau trong tests/logs; hồi quy test_package.


## F18/F19 – thiếu đầu vào, phát hiện trong forward test

F18: TC13 hỏi gộp đúng ba trường cốt lõi nhưng còn xin thêm thời lượng/thiết bị không thiết yếu. F19: TC16 tự giả định chủ đề chia có dư để viết trọn bài khi chưa được nêu chủ đề. Hai ca đầu chưa đạt đầy đủ yêu cầu hành vi tối thiểu; dữ liệu ban đầu giữ trong tests/initial. Siết chỉ dẫn SKILL.md và source-priority.md, giữ nguyên đề thử, chạy lại bằng agent mới. Không phải lỗi lớp học; kết quả chạy lại trong tests/results.md.
