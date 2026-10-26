# Ghi chú Tuần 5

## Điều đã thực hiện

- Dùng Appium Server, UiAutomator2 và Android Emulator Android 12 để tự động kiểm thử ứng dụng SauceLabs Sample App.
- Xác định các trường và nút đăng nhập qua accessibility id, sau đó dùng explicit wait để chờ giao diện sẵn sàng.
- Viết ba ca pytest độc lập: đăng nhập hợp lệ, mật khẩu sai và bỏ trống tên đăng nhập.
- Mỗi ca lưu ảnh màn hình vào thư mục `anh/` trước khi đóng phiên Appium.

## Kết quả chạy

Chạy `python -m pytest -v tuan-05/test_login.py` tại thư mục gốc repository: **3 passed**.

Ảnh kết quả gồm `test_login_with_valid_credentials.png`, `test_login_with_invalid_password.png` và `test_login_without_username.png`.

## Ghi chú môi trường

Appium-Python-Client cần được cài trong đúng môi trường ảo dùng để chạy pytest. Trước khi chạy, cần mở emulator, xác nhận thiết bị bằng `adb devices`, khởi động Appium Server tại `127.0.0.1:4723` và cài UiAutomator2 driver.
