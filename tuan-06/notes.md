# Ghi chú Tuần 6

## Nội dung thực hành

- Dùng explicit wait để đồng bộ với màn hình và popup; xác định phần tử qua accessibility id.
- Mở/đóng popup sort, sắp xếp giá tăng dần và kiểm tra thứ tự hiển thị.
- Thêm, xóa và kéo sản phẩm vào Cart; xác nhận trạng thái bằng UI.
- Cuộn danh sách bằng UiAutomator2 `mobile: scrollGesture`, lưu ảnh toàn màn hình và ảnh element.
- Kiểm tra Appium Remote WebDriver session, mở menu và đăng xuất.

## Kết quả

Đã chạy `python -m pytest -v tuan-06/test_products.py` trên Android Emulator: **5 passed**. Ảnh cuối mỗi test, ảnh màn hình sau khi cuộn và ảnh tiêu đề sản phẩm được lưu tự động trong `anh/`.