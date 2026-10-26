# Tuần 6 - Appium trên PRODUCTS

Kiểm thử sắp xếp sản phẩm, thao tác giỏ hàng, kéo thả, cuộn/chụp màn hình và menu của SauceLabs Sample App trên Android Emulator.

## Điều kiện chạy

- Emulator Android đang chạy và xuất hiện trong `adb devices`.
- Appium Server đang chạy tại `http://127.0.0.1:4723` và đã cài UiAutomator2 driver.
- SauceLabs Sample App 2.7.1 đã cài trên emulator.
- Đã cài dependency: `python -m pip install -r requirements.txt`.

## Chạy

Từ thư mục gốc repository:

```powershell
python -m pytest -v tuan-06/test_products.py
```

Ảnh cuối mỗi test, ảnh màn hình sau khi cuộn và ảnh tiêu đề sản phẩm được lưu trong `tuan-06/anh/`.

## Phạm vi

- A1: explicit waits, accessibility id, popup sort và kiểm tra sắp xếp.
- A2: thêm/xóa sản phẩm, kéo thả native bằng `mobile: dragGesture`, xử lý `NoSuchElementException`.
- A3: `mobile: scrollGesture`, lưu screenshot màn hình và element đang hiển thị.
- A4: Appium Remote WebDriver session, menu và logout.

Upload file và Firebug không áp dụng cho màn PRODUCTS của ứng dụng Android mẫu; thao tác được kiểm thử ở đây là cuộn danh sách và chụp ảnh UI native.