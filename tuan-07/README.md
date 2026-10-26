# Tuần 7 - Appium: chi tiết, trạng thái, thanh toán và bố cục

Kiểm thử ứng dụng Sauce Labs Sample App 2.7.1 trên Android Emulator theo bốn nội dung A1–A4.

## Điều kiện chạy

- Emulator đang hoạt động và xuất hiện trong `adb devices`.
- Appium Server đang chạy tại `http://127.0.0.1:4723`, có UiAutomator2 driver.
- Đã cài Sauce Labs Sample App 2.7.1 (`com.swaglabsmobileapp`) trên emulator.
- Đã cài dependency từ thư mục gốc: `python -m pip install -r requirements.txt`.

Chạy từ thư mục gốc repository:

```powershell
python -m pytest -v tuan-07/test_app.py
```

Ảnh cuối mỗi test được lưu trong `tuan-07/anh/`.

## Phạm vi

- **A1:** Mở chi tiết sản phẩm, cuộn trang, kiểm tra native package/activity và quay lại bằng `back()`. Wait lúc chuyển màn hình bỏ qua stale element tạm thời.
- **A2:** Tạo trạng thái giỏ hàng, chạy `RESET APP STATE`, xác nhận giỏ trống, rồi terminate/activate ứng dụng. Capability `noReset=False` được đặt tường minh; sau khi mở lại, ứng dụng có thể yêu cầu đăng nhập lại.
- **A3:** Dùng `pytest.mark.parametrize` kiểm tra dữ liệu checkout hợp lệ và các trường bắt buộc; trường được `clear()` trước khi nhập, đóng bàn phím nếu đang mở.
- **A4:** Dùng XPath/accessibility id, kích thước và tọa độ phần tử để xác nhận chuyển đổi grid/list và quay lại grid.
- Native app không có browser cookie endpoint; test kiểm tra giới hạn này được đánh dấu `xfail` với lý do cụ thể.
