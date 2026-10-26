# Test cases Tuần 7 - Swag Labs Android

## Môi trường

- App: Sauce Labs Sample App 2.7.1 (`com.swaglabsmobileapp`)
- Thiết bị: Android Emulator
- Appium Server, UiAutomator2, Appium-Python-Client và pytest
- Tài khoản: `standard_user` / `secret_sauce`

| Mã | Chức năng | Thao tác | Kết quả mong đợi |
| --- | --- | --- | --- |
| A1 | Chi tiết sản phẩm và quay lại | Mở Backpack, kiểm tra description/package/activity, cuộn trang chi tiết, gọi `back()`. | Chi tiết Backpack hiển thị; trở lại PRODUCTS và tên sản phẩm đúng. |
| A2.1 | Reset trạng thái | Thêm Backpack, mở menu và chọn RESET APP STATE; vào Cart. | Giỏ trống và không còn nút REMOVE. |
| A2.2 | Vòng đời ứng dụng | Terminate rồi activate app trong cùng session `noReset=False`. | App mở lại màn PRODUCTS hoặc đăng nhập; đăng nhập lại nếu cần. |
| A2.3 | Cookie trong native context | Gọi endpoint cookie WebDriver. | Endpoint không được Appium native hỗ trợ; test được đánh dấu xfail theo `UnknownMethodException`. |
| A3.1 | Thiếu First Name | Để trống First Name và tiếp tục checkout. | Hiển thị lỗi `First Name is required`. |
| A3.2 | Thiếu Last Name | Để trống Last Name và tiếp tục checkout. | Hiển thị lỗi `Last Name is required`. |
| A3.3 | Thiếu Postal Code | Để trống Postal Code và tiếp tục checkout. | Hiển thị lỗi `Postal Code is required`. |
| A3.4 | Thông tin hợp lệ | Nhập đủ thông tin và tiếp tục checkout. | Chuyển tới bước overview có Backpack và nút FINISH. |
| A4 | Grid/list | Đo tọa độ/kích thước card, toggle sang list, rồi trở lại grid. | Grid có hai card đầu ở hai cột; list có card rộng hơn và cùng cột; toggle về grid thành công. |

Test checkout chạy với bốn bộ dữ liệu bằng `pytest.mark.parametrize`. Mỗi test tạo session mới, đăng nhập và lưu screenshot cuối test trong `anh/`.
