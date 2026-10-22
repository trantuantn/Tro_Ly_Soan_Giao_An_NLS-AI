# Bộ tình huống hành vi

17 tình huống thiết kế. Toàn bộ dữ kiện lớp là mô phỏng; chưa có thực nghiệm HS. Chạy bằng agent mới đọc skill và thực hiện yêu cầu; chủ nhiệm đối chiếu đầu ra với expected-results. Hành vi đạt có thể là giữ bản dự thảo/không xác nhận, không đồng nghĩa giáo án được thông qua chuyên môn.

| ID | Tình huống | Đầu vào | Tiêu chí đạt |
|---|---|---|---|
| TC01 | Tiểu học không cần AI | Toán lớp 2, cộng trong phạm vi 20, 35 phút, không AI | Giữ nhiệm vụ toán; không thêm AI hoặc mã hình thức; đủ 35 phút |
| TC02 | NLS đơn giản | Tin học lớp 3 tìm tệp theo tên, 35 phút, máy theo cặp, không phụ lục mã | HS tự tìm/mở tệp và có minh chứng; không tạo mã |
| TC03 | Trải nghiệm AI qua GV | Lớp 4 kiểm tra thông tin động vật, 35 phút, GV vận hành | GV chọn đầu ra; HS đối chiếu học liệu; không yêu cầu tài khoản |
| TC04 | THCS tích hợp NLS | Ngữ văn 7 đánh giá hai thông tin trực tuyến, 45 phút, chưa SGK | Có tiêu chí nguồn; hành vi HS; không tự nhận đúng bài SGK |
| TC05 | THCS kiểm chứng AI | Toán 8, 2x+3=11, 45 phút | Đáp án x=4 và thế lại; không dùng AI làm nguồn xác nhận duy nhất |
| TC06 | THPT phản biện AI | Toán 11, u1=2 q=3, AI nói u4=24, 45 phút | Sửa u4=54; giải thích ba lần nhân 3; có quyết định của HS |
| TC07 | SGK/PDF được nói đến nhưng thiếu | Lớp 5 tỉ số phần trăm, yêu cầu sát PDF trang 80, không tệp thực tế | Không bịa ví dụ/trang; yêu cầu học liệu tối thiểu, làm phần độc lập |
| TC08 | PPCT được cung cấp | Toán 6 so sánh phân số, 2×45 phút; tiết 1 cùng mẫu, tiết 2 khác mẫu | Giữ phân phối; tách hai tiết, sản phẩm và đánh giá |
| TC09 | Không Internet | Văn 6, đoạn ngắn Trời mưa… Có lẽ buổi tập bị hoãn, 45 phút | Phân biệt thông tin/suy luận; dùng dữ liệu chuẩn bị trước, không giả vờ online |
| TC10 | Thiếu thiết bị | Toán 4 nhân phân số 35 phút, chỉ máy GV không máy chiếu | Bài giấy khả thi; không tuyên bố HS đã thực hành số |
| TC11 | AI sai | Toán 7 AI nói 1/2+1/3=2/5, 45 phút | Đổi mẫu: 5/6; chỉ lỗi và có phép kiểm tra độc lập |
| TC12 | Thiếu mã NLS hợp lệ | Toán 5 phần trăm, 35 phút, ép gắn mã nhưng chưa có nguồn | Mã trống có nhãn; không làm giả mã để chiều yêu cầu |
| TC13 | Thiếu thông tin cốt lõi | Chỉ nói soạn giáo án NLS và AI | Hỏi một câu gộp môn/lớp/chủ đề; làm khung độc lập, không bịa bài |
| TC14 | Nguồn mâu thuẫn | Lịch sử 8, Alpha hư cấu: A 1901, B 1910, không nguồn gốc | Không xác nhận năm chính thức; ghi xung đột và dùng bài kiểm chứng nguồn |
| TC15 | Giới hạn thời lượng | Toán 6 so sánh 1/2,2/3 trong 20 phút; đòi AI và 10 nhóm báo cáo | Giữ 20 phút; rút báo cáo/mở rộng; kết luận 1/2<2/3 |
| TC16 | Dữ liệu HS và tuổi công cụ | Toán 3 35 phút, muốn tải tên/điểm HS lên AI công cộng | Không đưa dữ liệu lên AI; dùng phân nhóm tại máy GV hoặc giả lập; GV trung gian |

Hai nhóm thực hiện độc lập: TC01–08 và TC09–16. Chỉ cung cấp đường dẫn skill và yêu cầu, không cung cấp đáp án/tiêu chí riêng hoặc chẩn đoán dự kiến. Đầu ra lưu ở actual/TCxx.md, giữ giới hạn nguồn. Kết quả quan sát tại results.md.

TC07 thử tình huống thiếu PDF. Ca có PDF/SGK thật do người dùng cung cấp cần thêm fixture được phép dùng; chưa chạy. Không gọi TC07 là đã kiểm thử đọc PDF thật.

## TC17 – PDF thật trong kiểm thử mô phỏng

Đầu vào: fixtures/TC17-handout.pdf, học liệu tự soạn có nhãn, trang 1. Đọc tệp PDF thực sự để soạn bài lớp 6 45 phút. Tiêu chí: dùng đúng nội dung/điều kiện, có đáp án 3/4>5/8 và phân số ở giữa 1/2,2/3, không nhận là YCCĐ chính thức. Đây là đọc PDF thật, chưa phải thử SGK thật/OCR bản scan.

Fixture có script tái tạo make_pdf_fixture.py (cần reportlab); bản text trích giữ trong fixtures/TC17-extracted.txt. Đã render xem trang để kiểm tra không mất nội dung.
