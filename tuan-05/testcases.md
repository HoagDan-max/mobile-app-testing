# Test cases đăng nhập Appium

## Môi trường

- Ứng dụng: SauceLabs Sample App 2.7.1 (`com.swaglabsmobileapp`)
- Thiết bị: Android Emulator, Android 12 (`emulator-5554`)
- Công cụ: Appium Server, UiAutomator2, Appium-Python-Client và pytest
- Tiền điều kiện: Appium Server đang chạy tại `http://127.0.0.1:4723`, ứng dụng đã được cài trên emulator.

| Mã | Dữ liệu đầu vào | Các bước chính | Kết quả mong đợi |
| --- | --- | --- | --- |
| TC01 | Username `standard_user`, password `secret_sauce` | Nhập thông tin hợp lệ, nhấn LOGIN | Mở danh sách sản phẩm và hiển thị `Sauce Labs Backpack`. |
| TC02 | Username `standard_user`, password `wrong_password` | Nhập mật khẩu sai, nhấn LOGIN | Không đăng nhập; hiển thị `Username and password do not match any user in this service.` |
| TC03 | Username để trống, password `secret_sauce` | Để trống username, nhập password, nhấn LOGIN | Không đăng nhập; hiển thị `Username is required`. |

Mỗi ca tạo một phiên Appium riêng. Ảnh màn hình sau khi chạy được lưu trong thư mục `anh/` với tên tương ứng tên test.
