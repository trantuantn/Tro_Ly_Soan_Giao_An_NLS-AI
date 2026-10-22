# PRO 5.0 – Trợ lý soạn giáo án tích hợp NLS & AI

Bản phát hành skill **1.0.0**, tên hệ thống PRO 5.0. Hỗ trợ giáo viên tiểu học, THCS, THPT thiết kế và kiểm định kế hoạch bài dạy có mục tiêu, hoạt động GV–HS, sản phẩm, đánh giá, phân hóa và dự phòng.

**Giáo viên tổ chức – học sinh hoạt động – công nghệ hỗ trợ – AI đồng hành – con người kiểm chứng và quyết định.**

## Dùng nhanh

Mở [SKILL.md](skills/lesson-planning-nls-ai/SKILL.md), cho AI đọc và làm theo; chỉ đọc references cần cho nhiệm vụ. Với ứng dụng hỗ trợ Agent Skills, đặt nguyên thư mục `lesson-planning-nls-ai` vào vị trí Skills của ứng dụng; cách cài cụ thể tùy nền tảng. Đưa mã lên GitHub không tự cài skill vào mọi tài khoản ChatGPT.

Ví dụ yêu cầu:

> Dùng $lesson-planning-nls-ai soạn bài Toán lớp 4 về nhân phân số, 35 phút, theo học liệu tôi đính kèm. Lớp không có thiết bị cá nhân. Chỉ tích hợp NLS/AI nếu có ích; kèm phiếu, đáp án và tự kiểm định.

Nếu thiếu SGK/YCCĐ nguồn gốc, AI phải đánh dấu dự thảo và điểm cần đối chiếu. Không được tự nhận đúng nguyên văn SGK hay tạo mã NLS. Năm nhóm AI của PRO 5.0 là cách phân loại nội bộ, khác cấu trúc khung UNESCO và khung Việt Nam.

## Thành phần

| Đường dẫn | Vai trò |
|---|---|
| `skills/lesson-planning-nls-ai/SKILL.md` | Điều phối và quy tắc kích hoạt |
| `references/` trong skill | Nguồn, chương trình, phân tích, NLS, AI, sư phạm, an toàn, QA, hợp đồng đầu ra |
| `assets/` trong skill | 5 mẫu giáo án, ánh xạ NLS/AI, rubric và bảng kiểm |
| `scripts/validate_skill.py` trong skill | Kiểm tra cấu trúc, liên kết, biểu mẫu QA; không chấm chuyên môn |
| [docs/architecture.md](docs/architecture.md) | Thiết kế, bản đồ tệp và luồng quyết định |
| [docs/audit.md](docs/audit.md) | Nguồn kế thừa, giới hạn lịch sử và thay đổi |
| [docs/lessons-learned.md](docs/lessons-learned.md) | Nguyên tắc, điều kiện áp dụng, mức bằng chứng |
| [docs/failure-patterns.md](docs/failure-patterns.md) | Lỗi/rủi ro và cách phát hiện |
| [docs/feedback-log.md](docs/feedback-log.md) | Sổ feedback có nguồn, tách yêu cầu khỏi phản hồi thực địa |
| [docs/success-patterns.md](docs/success-patterns.md) | Thành công có bằng chứng, giới hạn suy luận |
| [tests/test-cases.md](tests/test-cases.md) | Tình huống, đầu vào và tiêu chí |
| [tests/results.md](tests/results.md) | Kết quả thực sự chạy và phần chưa chạy |
| [docs/report.md](docs/report.md) | Báo cáo phát hành, kiểm thử và triển khai |

## Kiểm tra tại máy

Python 3.10+; công cụ kiểm tra gói dùng thư viện chuẩn. Công cụ quick_validate của skill-creator là tùy chọn, cần PyYAML.

```bash
python skills/lesson-planning-nls-ai/scripts/validate_skill.py skills/lesson-planning-nls-ai
python -m unittest discover -s tests -v
```

Điểm QA nội bộ 100, ngưỡng 85 và cả 5 hard gate phải pass. Không dùng AI vẫn có thể đạt đủ điểm. Chưa đủ nguồn trọng tâm không được gắn nhãn đã kiểm định.

## Phạm vi đã xác minh

Nguồn được rà soát 22/10/2026, xem [sổ nguồn](skills/lesson-planning-nls-ai/references/sources.md). Chưa có registry đầy đủ mã NLS, chưa kiểm thử dạy thực tế và chưa xác minh xuất Word/PDF. Có test tự động và tình huống mô phỏng; không suy ra hiệu quả học sinh từ các test đó.

Chưa cấp giấy phép sử dụng lại; xem [LICENSE-STATUS.md](LICENSE-STATUS.md). Không đưa dữ liệu học sinh, khóa API hoặc học liệu có hạn chế quyền vào repository.
