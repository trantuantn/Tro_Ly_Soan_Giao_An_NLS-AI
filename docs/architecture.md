# Kiến trúc và vai trò

Metadata name/description kích hoạt khi soạn/sửa/kiểm định giáo án hoặc tích hợp NLS/AI. SKILL.md điều phối tám bước; references cung cấp quyết định theo nhu cầu, assets cung cấp mẫu đầu ra. Không yêu cầu nạp mọi tài liệu mỗi lần. Mọi reference được liên kết trực tiếp từ SKILL.md; đường dẫn tương đối để sao chép nguyên thư mục qua môi trường khác.

Luồng: đọc nguồn → xác định YCCĐ → chọn mức tích hợp → thiết kế nhiệm vụ và minh chứng → phân hóa/dự phòng → tạo bài đầy đủ → tự sửa qua QA → bàn giao. Khi thiếu cốt lõi: hỏi gộp và tiếp tục phần độc lập. Khi nguồn cốt lõi chưa kiểm chứng: xuất bản dự thảo có giới hạn, không đánh dấu đạt.

| Reference | Quyết định nó hỗ trợ |
|---|---|
| curriculum, source-priority, sources | Căn cứ, phiên bản và mâu thuẫn |
| lesson-analysis | Mục tiêu, năng lực và minh chứng |
| nls-framework, ai-competence | Có cần tích hợp và đối chiếu thế nào |
| pedagogy, activity-design | Tổ chức việc GV–HS, sản phẩm và thời gian |
| assessment, differentiation | Chấm bằng gì, hỗ trợ ai, mở rộng thế nào |
| ai-safety | Độ tuổi, tài khoản, dữ liệu, sự cố |
| quality-gates, output-contract | Điều kiện được thông qua và hợp đồng bàn giao |

5 assets: lesson-plan-template, nls-mapping-template, ai-mapping-template, assessment-rubric, quality-checklist. Script validate_skill.py kiểm tra gói và schema QA, không phải bộ máy soạn giáo án hay chấm nội dung tự động.

Repo chứa tài liệu người dùng và kiểm thử bên ngoài skill. Bản skill cài trong Skills và bản repo phải cùng nội dung; sau sửa kiểm tra đồng bộ. Không có phụ thuộc API hoặc khóa bí mật, có thể dùng offline với nguồn sẵn có; không thể xác minh văn bản mới khi mất mạng.
