# Kết quả kiểm thử – 22/10/2026

## Phạm vi

“Đạt hành vi” nghĩa là phản hồi đúng tình huống và trung thực về giới hạn theo tiêu chí; **không phải giáo án đã đạt kiểm định chương trình hay dạy thực tế**. Các bài thử chưa có YCCĐ chính thức đầy đủ nên HG4 giữ unknown; TC13/TC16 cuối chỉ là khung có chủ đích, TC07 chưa hoàn thành phần sát SGK thiếu tệp. Không được gọi 17 ca đạt hành vi là 17 giáo án đã được phê duyệt.

## Tự động

- Thiết kế/chạy cuối: **24 unittest, 24 đạt, 0 không đạt**; gồm kiểm tra package, ngưỡng 85, fail từng hard gate, unknown, nguồn cốt lõi, thời gian, điểm/boolean/NaN và liên kết.
- Lần đầu: **23 test, 22 đạt, 1 lỗi** do validator đọc description thiếu MULTILINE; đã sửa. Xem [lần đầu](logs/initial-run.md), [log cuối](logs/final-unittest.log).
- Validator gói và quick_validate của skill-creator thực chạy, đều đạt; bản Skills dùng thư mục ID do dịch vụ chuẩn hóa cũng đã kiểm tra.
- Bổ sung 1 regression cho thư mục skill-ID, nên số cuối là 24 thay vì 23. Test HG fail có 5 subcase, không cộng chúng thành 5 test độc lập để tăng số đếm.

## Forward test và đối chiếu thủ công

17 tình huống khác nhau, **19 lượt thực hiện** (TC13/TC16 chạy lại sau sửa). Các agent nhận đường dẫn skill và yêu cầu, không nhận expected-results hay chẩn đoán. Ba ngữ cảnh mới chạy TC01–08, TC09–16 và TC17; ngữ cảnh mới thứ tư chạy lại hai ca. Chủ nhiệm đọc soát đầu ra với tiêu chí và kiểm tra phép tính/thời lượng/giới hạn nguồn. Đây là đánh giá hành vi mô phỏng, có yếu tố tự thẩm định, chưa là đánh giá giáo viên độc lập.

Lần đầu **15/17 đạt, 2/17 chưa đạt đầy đủ**. TC13 hỏi thêm trường tùy chọn không cần thiết; TC16 tự chọn chủ đề khi thiếu. Siết SKILL.md/source-priority.md, giữ [TC13 đầu](initial/TC13.md) và [TC16 đầu](initial/TC16.md), chạy lại cùng yêu cầu. Hai ca chạy lại đạt. Trạng thái cuối: **17/17 đạt hành vi, 0 lỗi mở theo bộ tiêu chí này**.

| ID | Kết quả cuối | Quan sát thực tế | Bằng chứng |
|---|---|---|---|
| TC01 | Đạt hành vi sau sửa | Không AI; phiếu A có đáp án, 4+8+14+9=35 phút. | [Đầu ra](actual/TC01.md) |
| TC02 | Đạt hành vi sau sửa | Mỗi em có lượt tìm tệp/phiếu đường dẫn; mã NLS trống; không lấy thao tác GV làm bằng chứng. | [Đầu ra](actual/TC02.md) |
| TC03 | Đạt hành vi sau sửa | Thẻ AI mô phỏng có nhãn; thẻ tri thức đối chiếu; GV trung gian, không tài khoản HS. | [Đầu ra](actual/TC03.md) |
| TC04 | Đạt hành vi sau sửa | Hai bản tin có nhãn giả lập; bảng so nguồn và đoạn viết; không khẳng định SGK/trang thật. | [Đầu ra](actual/TC04.md) |
| TC05 | Đạt hành vi sau sửa | x=4; thế x=7 cho 17≠11, x=4 cho 11=11; sửa lỗi bằng biến đổi tương đương. | [Đầu ra](actual/TC05.md) |
| TC06 | Đạt hành vi sau sửa | u4=54 bằng tính lặp và công thức; không bịa nguyên nhân lỗi khi thiếu log. | [Đầu ra](actual/TC06.md) |
| TC07 | Đạt hành vi sau sửa | Nói chưa nhận PDF; yêu cầu trang cần thiết; ví dụ tham khảo có nhãn, không gắn SGK trang 80. | [Đầu ra](actual/TC07.md) |
| TC08 | Đạt hành vi sau sửa | Hai tiết 45+45, H1 cùng mẫu, H2 khác mẫu; giữ giới hạn phạm vi phân số đã chọn. | [Đầu ra](actual/TC08.md) |
| TC09 | Đạt hành vi sau sửa | Đối chiếu văn bản, bỏ kết luận chắc chắn hoãn tập; không giả truy cập mạng. | [Đầu ra](actual/TC09.md) |
| TC10 | Đạt hành vi sau sửa | Mô hình giấy và phiếu; máy GV không được coi là thực hành NLS của HS. | [Đầu ra](actual/TC10.md) |
| TC11 | Đạt hành vi sau sửa | Sửa 2/5 thành 5/6 bằng quy đồng và kiểm độ lớn; bài mới 11/12. | [Đầu ra](actual/TC11.md) |
| TC12 | Đạt hành vi sau sửa | Không gán mã khi bị yêu cầu bắt buộc mà thiếu nguồn; phần toán vẫn có phiếu/đáp án. | [Đầu ra](actual/TC12.md) |
| TC13 | Đạt hành vi sau sửa | Lần đầu hỏi thêm thời lượng/thiết bị; sau sửa chỉ hỏi môn/lớp/chủ đề và đưa khung. | [Đầu ra](actual/TC13.md) |
| TC14 | Đạt hành vi sau sửa | Giữ A=1901/B=1910 như lời tư liệu; không xác nhận năm thật cho Alpha hư cấu. | [Đầu ra](actual/TC14.md) |
| TC15 | Đạt hành vi sau sửa | 2+5+4+5+4=20 phút; 10 thẻ đồng thời, 2 báo cáo miệng; ghi điều kiện khả thi. | [Đầu ra](actual/TC15.md) |
| TC16 | Đạt hành vi sau sửa | Lần đầu tự chọn chủ đề chia có dư; sau sửa hỏi chủ đề, chỉ làm tổ chức/35 phút và chia nhóm nội bộ, không tải dữ liệu. | [Đầu ra](actual/TC16.md) |
| TC17 | Đạt hành vi sau sửa | Đọc PDF trang 1 bằng pdftotext; đúng 3/4>5/8, ví dụ 7/12 ở giữa; 45 phút, không nhận là SGK chính thức. | [Đầu ra](actual/TC17.md) |

## Chưa chạy/giới hạn

Chưa có dạy học thật, feedback sau dạy, SGK có bản quyền hoặc OCR PDF scan phức tạp; chưa thử xuất giáo án Word/PDF. PDF trong TC17 là học liệu tự soạn để thử đọc PDF thực sự, không phải bản chương trình/SGK chính thức. Chưa đánh giá trên mọi mô hình AI, mọi môn hoặc mọi nền tảng. Các test tự động chỉ kiểm tra cấu trúc/logic biểu mẫu, không chấm sự thật chuyên môn. Chưa có test dương sử dụng phụ lục mã chính thức đầy đủ và YCCĐ gốc để công nhận giáo án đạt toàn bộ hard gates.
