# Báo cáo PRO 5.0 – bản skill 1.0.0

Ngày 22/10/2026. Tên skill: `lesson-planning-nls-ai`.

## A. Executive Summary

Đã tạo bộ skill thực tế, lưu vào Skills, dựng repository theo cấu trúc có thể dùng lại, có bộ nguồn, mẫu, QA và kiểm thử có đầu ra. Kế thừa 10 tệp PRO 5.0 cũ được đọc thực sự; không tự nhận đã truy cập toàn bộ lịch sử. Không có feedback giáo viên sau dạy hay bằng chứng hiệu quả học sinh để tổng hợp thành thành tích.

Đã sửa lỗi validator thực chạy và hai hành vi chưa đạt trong forward test. 24/24 unittest cuối và 17/17 tình huống hành vi cuối đạt sau sửa; chi tiết/giới hạn trong [kết quả](../tests/results.md). Điểm QA của một bài vượt 85 vẫn không được thông qua khi HG4 unknown.

Chưa hoàn thiện registry mã NLS có nguồn từng chỉ báo, đối chiếu toàn bộ YCCĐ từng môn, kiểm thử lớp học và xuất Word/PDF. Đã nhận diện hướng dẫn AI Việt Nam 2026, nhưng chưa thẩm định toàn bộ phụ lục gốc. Đã ghi giới hạn trong sổ nguồn; không tự chọn giấy phép.

## B. Skill Architecture

`SKILL.md` điều phối; `agents/openai.yaml` là metadata giao diện; 13 references cho nguồn, chương trình, phân tích, NLS, AI, sư phạm, hoạt động, đánh giá, phân hóa, an toàn, QA, đầu ra và sổ nguồn; 5 assets; 1 script kiểm tra. Metadata description kích hoạt cho soạn/sửa/kiểm định giáo án, NLS/AI và học liệu liên quan.

Chỉ đọc tài liệu cần theo tác vụ; mọi reference/asset liên kết trực tiếp từ SKILL.md. Gói không đòi khóa API, dùng được với nguồn cục bộ; offline không thể xác minh văn bản mới. Xem [kiến trúc](architecture.md), [bản đồ tệp](file-map.md), [audit](audit.md).

## C. Knowledge Consolidation

Quyết định: không hỏi lựa chọn tự giải quyết; giả định có nhãn; hỏi một câu chỉ chứa đầu vào cốt lõi còn thiếu; không tự chọn chủ đề; làm tiếp phần độc lập. SGK/PPCT người dùng quyết định đúng bài/phân phối, văn bản chính thức quyết định chuẩn; không âm thầm ghi đè nguồn mâu thuẫn.

NLS: mã → biểu hiện → nhiệm vụ → hành vi HS → minh chứng → đánh giá; thêm nguồn/mức/trang. Không có căn cứ thì để mã trống. AI: năm nhóm nội bộ, không gán thành năm mức chính thức; học sinh tự nghĩ, kiểm chứng và quyết định. Công nghệ chỉ hỗ trợ GV không tự chứng minh năng lực HS.

Tách yêu cầu người dùng, rủi ro dự đoán, lỗi xác nhận và kết quả thử nghiệm. F01–F15 là phòng ngừa; F16 được audit thấy ở cách gọi nhóm AI; V01 là lỗi validator thực chạy; F18/F19 phát hiện qua đầu ra thử và đã chạy lại. Chưa có thành công thực địa. Xem [bài học](lessons-learned.md), [lỗi](failure-patterns.md), [feedback](feedback-log.md), [thành công có bằng chứng](success-patterns.md).

## D. Quality Assurance

Thang nội bộ 100 điểm: chính xác 25, mục tiêu 15, hoạt động 20, đánh giá/phân hóa 15, NLS/AI 15, an toàn 10; ngưỡng 85 và HG1–HG5 đều pass. Unknown không pass. Thang này không phải chuẩn Bộ GDĐT.

Tự động: ban đầu 22/23 đạt, một lỗi regex metadata đã sửa; bổ sung test thư mục ID do Skills chuẩn hóa, cuối 24/24 đạt. Validator gói, quick_validate thực chạy đạt. Thủ công: 17 ca khác nhau, 19 lượt; lần đầu 15 đạt/2 chưa đạt, sau sửa và chạy lại 17 đạt/0 lỗi mở theo tiêu chí. Đầu ra cũ và mới đều giữ lại.

Kiểm tra nguồn/đáp án/thời lượng, liên kết cục bộ và các mẫu khóa bí mật thông dụng. Không tìm thấy token/khóa theo các mẫu được quét; đây không phải kiểm toán bảo mật toàn diện. Không có hồ sơ học sinh thật trong ví dụ. Chưa kiểm nghiệm dạy học, OCR SGK scan, hoặc xuất giáo án Word/PDF. Xem [test cases](../tests/test-cases.md) và [log kết quả](../tests/results.md).

## E. GitHub Deployment

Repository: https://github.com/trantuantn/Tro_Ly_Soan_Giao_An_NLS-AI

Nhánh: https://github.com/trantuantn/Tro_Ly_Soan_Giao_An_NLS-AI/tree/feat/pro5-lesson-planning-nls-ai-skill

Repository ban đầu trống, default main; tài khoản kết nối có quyền push. Đã khởi tạo README trên main, commit `715c75a51b888d0e63892617ad6665368ea91e1a`, rồi tạo nhánh feature. Bộ đầy đủ nằm trên nhánh feature để xem xét; không tuyên bố đã hợp nhất vào main. Không ghi đè dữ liệu hiện có.

Danh sách thêm/sửa tại [file-map](file-map.md). SHA chứa chính báo cáo này được xác minh qua remote ref ở bước cuối và gửi trong phản hồi; không chèn SHA tự tham chiếu vào cùng commit. Báo cáo này mô tả nội dung phát hành; trạng thái remote sau ghi và URL PR được xác nhận trong phản hồi cuối.

## F. Next Improvements

v1.1: đối chiếu phụ lục chương trình và NLS/AI gốc, nhập registry có nguồn, bổ sung feedback giáo viên thật và kiểm thử Word/PDF. v2.0: đánh giá giáo viên độc lập nhiều môn/cấp học, fixture được phép dùng, đo tác động bằng dữ liệu thật và quản lý nguồn theo phiên bản. Không công bố tỷ lệ cải thiện trước khi có minh chứng. Xem [roadmap](roadmap.md).
