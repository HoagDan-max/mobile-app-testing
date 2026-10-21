# Hướng dẫn cài đặt Môi trường Kiểm thử Tự động Mobile (Appium)

Để chạy được bài kiểm thử trong dự án này, máy tính của bạn cần cài đặt 5 công cụ cốt lõi dưới đây.

## 1. Môi trường Python & Thư viện
*   **Python:** Cài đặt Python 3.10 trở lên.
*   **Thư viện:** Mở Terminal ở thư mục gốc của dự án và chạy các lệnh sau:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install Appium-Python-Client pytest
    ```

## 2. Java JDK (Môi trường nền cho Android)
*   **Tải xuống:** Tải **Java JDK 17** hoặc **JDK 21 LTS** từ trang `adoptium.net`.
*   **Cài đặt:** Chạy file cài đặt. Đảm bảo cấu hình biến môi trường `JAVA_HOME` trỏ về thư mục cài đặt JDK.

## 3. Android Studio (Công cụ SDK & Máy ảo)
*   **Tải xuống:** Truy cập `developer.android.com/studio` tải bản mới nhất.
*   **Cài đặt:** Trong quá trình cài đặt, bắt buộc tích chọn **Android Virtual Device**.
*   **Biến môi trường:** 
    *   Tạo biến System `ANDROID_HOME` trỏ tới: `C:\Users\<Tên_User>\AppData\Local\Android\Sdk`.
    *   Thêm vào biến `Path`: `C:\Users\<Tên_User>\AppData\Local\Android\Sdk\platform-tools`.

## 4. Appium Server (Lõi điều khiển)
*   **Cài Node.js:** Tải bản LTS từ `nodejs.org` và cài đặt.
*   **Cài Appium & Driver:** Mở một Terminal mới (chạy quyền Admin) và gõ:
    ```bash
    npm install -g appium
    appium driver install uiautomator2
    ```

## 5. File Ứng dụng & Thiết bị thật (Tùy chọn)
*   Tải file `Android.SauceLabs.Mobile.Sample.app.2.7.1.apk` và đặt vào thư mục gốc của dự án.
*   Nếu dùng máy thật (như Samsung A12): Bật chế độ Nhà phát triển (Developer Options) -> Bật **USB Debugging** -> Cắm cáp vào máy tính.
*   Mở Terminal gõ `adb devices` để lấy mã UDID của máy thật. Thay mã này vào biến `options.udid` trong code test.