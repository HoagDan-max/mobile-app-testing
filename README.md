# Dự án Kiểm thử Tự động Mobile App (Tuần 4 - Tuần 11)

Dự án này sử dụng Appium để viết các kịch bản kiểm thử tự động cho ứng dụng Android giả lập/thiết bị thật.

## 📱 Thông tin dự án
- **Ứng dụng:** SauceLabs Sample App (`com.swaglabsmobileapp`)
- **Nền tảng:** Android (Thiết bị thật hoặc AVD)
- **Công cụ:** Appium Server, Python, pytest, UiAutomator2 Driver

## 🚀 Hướng dẫn cài đặt cho thành viên nhóm
**1. Tải ứng dụng (APK)**
- Tải file `Android.SauceLabs.Mobile.Sample.app.2.7.1.apk` và đặt trực tiếp vào thư mục gốc của dự án.

**2. Cài đặt Python & Thư viện**
- Mở Terminal ở thư mục gốc, gõ:
```bash
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt

Đảm bảo máy tính đã cài Node.js, sau đó gõ:

    npm install -g appium
    appium driver install uiautomator2