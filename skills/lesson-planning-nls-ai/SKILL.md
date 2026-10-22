---
name: lesson-planning-nls-ai
description: >-
  Soạn, sửa và kiểm định kế hoạch bài dạy GDPT 2018 cho giáo viên tiểu học,
  THCS, THPT Việt Nam; tích hợp năng lực số (NLS), năng lực AI có căn cứ,
  thiết kế hoạt động GV–HS, sản phẩm, phiếu học tập, đánh giá và phân hóa.
  Dùng khi người dùng yêu cầu giáo án, kế hoạch bài dạy, ánh xạ NLS/AI,
  rà soát giáo án hoặc sửa theo feedback, với SGK/PDF/PPCT nếu có.
---

# PRO 5.0 – Vietnamese Lesson Planning with Digital & AI Competencies

Giáo viên tổ chức – học sinh hoạt động – công nghệ hỗ trợ – AI đồng hành – con người kiểm chứng và quyết định.

## Quy trình điều phối

1. Đọc học liệu được cấp; tách dữ kiện, giả định và phần chưa xác minh. Áp dụng [nguồn và quyết định](references/source-priority.md) cùng [chương trình](references/curriculum.md). Không hỏi điều có thể tự chọn; chỉ hỏi gộp khi thiếu môn/lớp/chủ đề không suy ra được. Không hỏi kèm thời lượng/thiết bị có thể tự chọn. Nếu thiếu riêng chủ đề, không tự chọn bài dù ghi nhãn giả định; chỉ làm khung và phần tổ chức độc lập. Tiếp tục phần không phụ thuộc câu trả lời.
2. Lập bảng YCCĐ → mục tiêu → nhiệm vụ → sản phẩm → tiêu chí theo [phân tích bài](references/lesson-analysis.md). Không tự gán mục tiêu thành YCCĐ chính thức hay bịa trang SGK.
3. Chọn riêng mức NLS và AI: không cần / hỗ trợ GV / HS thực hành. Không ép AI, không lấy GV dùng thiết bị làm minh chứng HS đạt NLS. Đọc [khung NLS](references/nls-framework.md) khi ánh xạ; chỉ dùng mã có nguồn, mức, chỉ báo và trang. Nếu thiếu, để mã trống và ghi mô tả dự kiến.
4. Khi có AI, đọc [năng lực AI](references/ai-competence.md) và [an toàn](references/ai-safety.md). Dùng chu trình AI đề xuất → HS suy nghĩ → HS kiểm chứng → con người quyết định. Năm nhóm PRO 5.0 là phân loại nội bộ, không phải khung chính thức. Kiểm tra hướng dẫn Việt Nam theo năm học và điều kiện tuổi/tài khoản; mặc định GV trung gian khi chưa xác minh.
5. Thiết kế theo [sư phạm](references/pedagogy.md), [hoạt động](references/activity-design.md), [đánh giá](references/assessment.md), [phân hóa](references/differentiation.md). Mỗi hoạt động phải có mục tiêu, phút, nhiệm vụ cụ thể, hành động GV–HS, sản phẩm, công cụ và tiêu chí. Tính chuyển tiếp; có dự phòng mất mạng/thiếu thiết bị.
6. Soạn đầy đủ theo [hợp đồng đầu ra](references/output-contract.md) và [mẫu giáo án](assets/lesson-plan-template.md). Kèm phiếu, đáp án, rubric phù hợp; mục điều chỉnh sau dạy chờ dữ liệu thật.
7. Chấm theo [quality gates](references/quality-gates.md). Tổng ≥85/100 và cả HG1–HG5 pass mới đạt nội bộ. Gate unknown không được thông qua. Tự sửa, chấm lại và ghi giới hạn. Điểm QA không phải bằng chứng hiệu quả lớp học.
8. Với feedback mới, lưu nguồn/ngày, lỗi, mức độ, nguyên nhân, sửa chữa, minh chứng và test hồi quy; phân biệt nhận xét thật với rủi ro dự đoán. Không tự tạo số liệu, lịch sử hoặc thành công.

## Biểu mẫu dùng khi cần

- [Ánh xạ NLS](assets/nls-mapping-template.md): mã → biểu hiện → nhiệm vụ → hành vi → minh chứng → đánh giá, kèm nguồn.
- [Ánh xạ AI](assets/ai-mapping-template.md): nhận biết, sử dụng, kiểm chứng, hợp tác, trách nhiệm.
- [Rubric học sinh](assets/assessment-rubric.md): điều chỉnh theo nhiệm vụ và đáp án.
- [Bảng kiểm cuối](assets/quality-checklist.md): chốt nguồn, thời lượng, sản phẩm và hard gates.
- [Sổ nguồn](references/sources.md): tra phiên bản, trạng thái truy cập và giới hạn nguồn đã rà soát; không coi đây là bảo đảm hiệu lực trong tương lai.

## Công cụ kiểm tra

Chạy `python scripts/validate_skill.py <thư-mục-skill>` để kiểm tra gói. Dùng `--qa <bản-qa.json>` khi có bảng điểm theo schema của script. Script không chấm sự thật, không xác nhận mã chính thức và không thay giáo viên thẩm định. Nếu không có runtime, kiểm tra thủ công theo bảng kiểm và ghi “chưa chạy kiểm tra tự động”.
