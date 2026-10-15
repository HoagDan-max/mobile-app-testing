# Báo cáo Tuần 4 - Smoke Test

## 1. Trả lời câu hỏi lý thuyết

### Câu 1: Một script Selenium gồm những bước nào, và mỗi bước ứng với dòng nào trong bài kiểm thử?

* **Setup (Khởi tạo):** Khởi động trình duyệt. Tương ứng với dòng `driver = webdriver.Chrome()`.
* **Act (Hành động):** Thực hiện hành động trên trang web. Tương ứng với dòng `driver.get("https://the-internet.herokuapp.com/")`.
* **Assert (Kiểm chứng):** Kiểm tra kết quả thực tế có đúng với kết quả mong đợi hay không. Tương ứng với dòng `assert actual_title == "The Internet"`.
* **Teardown (Dọn dẹp):** Đóng trình duyệt và giải phóng tài nguyên. Tương ứng với dòng `driver.quit()`.

### Câu 2: pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên nào?

* Pytest tự động tìm kiếm các file có tên bắt đầu bằng `test_*.py` hoặc kết thúc bằng `*_test.py`.
* Bên trong các file đó, pytest sẽ thực thi các hàm có tên bắt đầu bằng `test_`.
* Pytest cũng có thể phát hiện các class có tên bắt đầu bằng `Test` và các phương thức kiểm thử bên trong class đó.

## 2. Nhật ký lỗi cài đặt (Troubleshooting Log)

### Lỗi gặp phải

Trong quá trình thực hành, em đã cố tình sửa câu lệnh assert từ:

`assert actual_title == "The Internet"`

thành:

`assert actual_title == "The Internet123"`

Kết quả, pytest báo lỗi:

`AssertionError: Lỗi: Tiêu đề thực tế là 'The Internet'`

Pytest xác định kết quả thực tế là `The Internet`, trong khi kết quả mong đợi là `The Internet123`, nên bài kiểm thử bị `FAILED`.

### Cách khắc phục

Em kiểm tra lại kết quả thực tế của trang web và nhận thấy tiêu đề chính xác là `The Internet`. Sau đó, em sửa câu lệnh assert trở lại:

`assert actual_title == "The Internet"`

và chạy lại:

`pytest test_smoke.py`

Kết quả cuối cùng:

`1 passed`