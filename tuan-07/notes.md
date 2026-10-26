# Ghi chú Tuần 7

## Nội dung thực hành

- Điều hướng vào chi tiết sản phẩm, kiểm tra activity/package native, cuộn và quay lại.
- Đợi UI qua các lần chuyển màn hình; cấu hình wait để bỏ qua `StaleElementReferenceException` tạm thời.
- Reset app state từ menu, xác nhận giỏ hàng được xóa, và kiểm tra terminate/activate với capability `noReset=False`; app có thể yêu cầu đăng nhập lại.
- Kiểm tra giới hạn cookie endpoint trong native app context bằng test `xfail` có nêu rõ nguyên nhân.
- Nhập và xóa dữ liệu checkout, ẩn bàn phím, parameterize ca hợp lệ/thiếu từng trường.
- Đo vị trí/kích thước card để xác nhận toggle grid và list.

## Kết quả

Đã chạy `python -m pytest -v tuan-07/test_app.py` trên Android Emulator: **7 passed, 1 xfailed**. Ca xfailed xác nhận native app không hỗ trợ browser cookie endpoint. Ảnh cuối mỗi test được lưu trong `anh/`.
