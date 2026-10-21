# Kịch bản Kiểm thử Đăng nhập (Tuần 5)
**Ứng dụng:** SauceLabs Sample App (Swag Labs)

## Test Case 1: Đăng nhập thành công
*   **Dữ liệu đầu vào:** Username = `standard_user`, Password = `secret_sauce`
*   **Các bước thực hiện:**
    1. Mở ứng dụng.
    2. Nhập `standard_user` vào ô Username.
    3. Nhập `secret_sauce` vào ô Password.
    4. Bấm nút LOGIN.
*   **Kết quả mong đợi:** Đăng nhập thành công, chuyển sang màn hình danh sách sản phẩm (có chữ "PRODUCTS").

## Test Case 2: Đăng nhập thất bại do sai mật khẩu
*   **Dữ liệu đầu vào:** Username = `standard_user`, Password = `sai_mat_khau_roi`
*   **Các bước thực hiện:**
    1. Mở ứng dụng.
    2. Nhập `standard_user` vào ô Username.
    3. Nhập `sai_mat_khau_roi` vào ô Password.
    4. Bấm nút LOGIN.
*   **Kết quả mong đợi:** Vẫn ở màn hình đăng nhập, hệ thống hiển thị thông báo lỗi (chứa chữ "do not match").

## Test Case 3: Đăng nhập thất bại do tài khoản bị khóa
*   **Dữ liệu đầu vào:** Username = `locked_out_user`, Password = `secret_sauce`
*   **Các bước thực hiện:**
    1. Mở ứng dụng.
    2. Nhập `locked_out_user` vào ô Username.
    3. Nhập `secret_sauce` vào ô Password.
    4. Bấm nút LOGIN.
*   **Kết quả mong đợi:** Vẫn ở màn hình đăng nhập, hệ thống hiển thị thông báo lỗi (chứa chữ "locked out").