# Tuần 5 - Kiểm thử đăng nhập bằng Appium

Các bài kiểm thử tự động chức năng đăng nhập của SauceLabs Sample App trên Android Emulator bằng Python, Appium và pytest.

## Chuẩn bị

- Android Emulator đang chạy và được `adb devices` nhận diện.
- Appium Server đang chạy tại `http://127.0.0.1:4723`.
- UiAutomator2 driver đã được cài cho Appium.
- APK `Android.SauceLabs.Mobile.Sample.app.2.7.1.apk` đã được cài trên emulator.
- Cài các thư viện Python trong môi trường ảo bằng `python -m pip install -r requirements.txt`.

## Chạy test

Đứng tại thư mục gốc repository và chạy:

```powershell
python -m pytest -v tuan-05/test_login.py
```

Ba ca kiểm thử gồm đăng nhập hợp lệ, mật khẩu sai và bỏ trống tên đăng nhập. Mỗi lần chạy lưu screenshot vào `tuan-05/anh/`.

## Nội dung bài nộp

- `testcases.md`: dữ liệu, thao tác và kết quả mong đợi của từng ca.
- `test_login.py`: mã Appium có chú thích tiếng Việt.
- `anh/`: ảnh màn hình kết quả từng ca.
- `notes.md`: ghi chú quá trình thực hiện tuần 5.
