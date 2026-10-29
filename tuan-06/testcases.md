# Test cases Tuần 6 - Swag Labs PRODUCTS

## Môi trường

- App: SauceLabs Sample App 2.7.1 (`com.swaglabsmobileapp`)
- Thiết bị: Android Emulator Android 12 (`emulator-5554`)
- Điều khiển: Appium Server, UiAutomator2, Appium-Python-Client và pytest
- Điều kiện trước: Appium Server tại `http://127.0.0.1:4723`, emulator online và app đã cài.
- Tài khoản: `standard_user` / `secret_sauce`

| Mã | Chức năng | Dữ liệu và thao tác | Kết quả mong đợi |
| --- | --- | --- | --- |
| A1 | Sắp xếp sản phẩm | Mở popup sort, đóng bằng Cancel, mở lại và chọn `Price (low to high)`. | Popup đóng/mở đúng; giá đầu tiên là `$7.99` và giá hiển thị theo thứ tự tăng dần. |
| A2.1 | Thêm/xóa giỏ hàng | Thêm Backpack, mở Cart, nhấn REMOVE. | Backpack xuất hiện trong Cart sau khi thêm; biến mất sau khi xóa; nút REMOVE không còn. |
| A2.2 | Kéo thả vào giỏ | Dùng `mobile: dragGesture` kéo `test-Drag Handle` vào `test-Cart drop zone`, mở Cart. | Backpack xuất hiện trong Cart. |
| A3 | Cuộn và chụp màn hình | Dùng `mobile: scrollGesture` cuộn danh sách; lưu ảnh màn hình và ảnh riêng tiêu đề sản phẩm. | Danh sách chuyển sang sản phẩm khác; hai ảnh được ghi vào `anh/`. |
| A4 | Remote session và menu | Kiểm tra session id, mở menu và chọn LOGOUT. | Session được khởi tạo; menu hiển thị; ứng dụng trở lại màn hình đăng nhập. |

Mỗi test mở một Appium session mới, đăng nhập trước khi thao tác và lưu screenshot kết quả. Test dùng explicit wait cho các trạng thái giao diện động.