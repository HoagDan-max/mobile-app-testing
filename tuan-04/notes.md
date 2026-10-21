# Ghi chú Quá trình thực hiện Tuần 4

## 1. Mục đích
Dự án được chuyển đổi từ việc kiểm thử Web (Selenium) sang kiểm thử Ứng dụng Di động (Appium) theo đúng lộ trình của môn học. Bài tập Tuần 4 yêu cầu thiết lập thành công môi trường và chạy thử một kịch bản "Smoke Test" cơ bản để kiểm tra việc mở ứng dụng.

## 2. Những thay đổi đã thực hiện
*   **Đổi tên kho mã:** Đổi tên repository trên GitHub từ `selenium-automation-project` thành `mobile-app-testing` để phản ánh đúng mục tiêu mới.
*   **Cập nhật thư viện:** Xóa `selenium` khỏi `requirements.txt` và thay bằng `Appium-Python-Client` và `pytest`.
*   **Tối ưu thiết bị:** Thay vì dùng Máy ảo (AVD) của Android Studio gây nặng máy, team quyết định sử dụng cấu hình cắm cáp kết nối trực tiếp với thiết bị thật (Samsung A12). Điều này giúp giảm tải phần cứng máy tính và tăng tốc độ chạy test.

## 3. Cấu trúc bài test Tuần 4 (`test_smoke.py`)
Code kiểm thử được thiết kế với 2 phần chính:
1.  **Hàm Fixture (`@pytest.fixture def driver`):** Sử dụng `UiAutomator2Options` để khai báo các thông số kết nối (`Desired Capabilities`) bao gồm: Tên nền tảng (Android), mã thiết bị (UDID), và đường dẫn tuyệt đối bằng module `os` tới file APK.
2.  **Hàm Test (`test_smoke_app_has_login_field`):** Áp dụng `WebDriverWait` và `expected_conditions` để tìm kiếm phần tử có `ACCESSIBILITY_ID` là `test-Username`. Dùng hàm `assert` để xác nhận phần tử này có hiển thị trên màn hình máy thật hay không.

## 4. Cách chạy bài test
1. Bật điện thoại Android, cắm cáp vào máy tính.
2. Bật Appium Server bằng cách mở một Terminal mới và gõ lệnh: `appium`.
3. Mở một Terminal khác, kích hoạt môi trường ảo: `.\.venv\Scripts\activate.bat`.
4. Chạy lệnh: `pytest tuan-04\test_smoke.py -v`.
5. Quan sát ứng dụng tự động mở trên điện thoại và báo kết quả `PASSED` màu xanh trên Terminal.