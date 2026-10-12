# Ghi chú Tuần 4
Người thực hiện: Phạm Hồng Hoàng Đan

1. Điều đã học được
Em đã học được:
* Cách khởi tạo môi trường ảo (venv) để cô lập thư viện Python.
* Cách viết một kịch bản Smoke Test cơ bản để mở trang web và kiểm tra tiêu đề.
* Biết cách tạo file `.gitignore` để ngăn các thư mục hệ thống (`venv`, `__pycache__`, `.pytest_cache`) bị đẩy lên GitHub, giữ cho repository luôn sạch sẽ và chuyên nghiệp.
* Nắm vững luồng làm việc của Git: từ việc tạo nhánh `week-04`, commit code, tạo Pull Request, cho đến việc gộp (Merge) vào nhánh `main` và đồng bộ lại về máy cá nhân (fetch/pull).

2. Trả lời câu hỏi phần đọc
*Selenium - Một script gồm những bước nào?** 
  Một script chuẩn có 4 bước: (1) Setup: Khởi tạo trình duyệt qua WebDriver; (2) Act: Thực thi thao tác như mở URL; (3) Assert: Kiểm tra kết quả trả về; (4) Teardown: Đóng trình duyệt và giải phóng bộ nhớ.
*Pytest - Quy tắc nhận diện tự động là gì?** 
  Pytest sẽ tự động quét và chạy các file có tên bắt đầu bằng `test_*.py` hoặc kết thúc bằng `*_test.py`. Trong các file đó, nó sẽ thực thi các hàm có tên bắt đầu bằng `test_` và các lớp bắt đầu bằng `Test`.

3. Nhật ký sử dụng AI
* **Nội dung đã hỏi AI:** Nhờ giải thích cơ chế hoạt động phối hợp giữa Selenium và Pytest, đồng thời hỗ trợ rà soát các lệnh Git khi nộp bài.(sử dụng song song chatgpt/genmini)
* **Đánh giá câu trả lời:** AI trả lời chính xác, giải thích dễ hiểu và đưa ra các dòng lệnh Git hợp lý.
* **Điều hiểu thêm:** Mình hình dung rõ hơn về kiến trúc WebDriver: Selenium chỉ đóng vai trò là "tay và mắt" để tương tác với trình duyệt, hoàn toàn không biết phân biệt đúng sai. Pytest mới đóng vai trò là "bộ não" để điều phối, đánh giá (assert) kết quả và báo cáo Pass/Fail. Mình cũng rèn luyện được thói quen review code trước khi commit.