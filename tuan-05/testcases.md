Test Cases Tuần 5 - Chức năng Đăng nhập

TC01 - Đăng nhập thành công

Bước thực hiện:

    1. Mở trang `https://the-internet.herokuapp.com/login`.

    2. Nhập username `tomsmith`.

    3. Nhập password `SuperSecretPassword!`.

    4. Nhấn nút Login.

Kết quả mong đợi: Hiển thị thông báo `You logged into a secure area!`.

TC02 - Đăng nhập sai mật khẩu

Bước thực hiện:

    1. Mở trang `https://the-internet.herokuapp.com/login`.

    2. Nhập username `tomsmith`.

    3. Nhập password `WrongPass`.

    4. Nhấn nút Login.

Kết quả mong đợi: Hiển thị thông báo `Your password is invalid!`.

TC03 - Để trống thông tin đăng nhập

Bước thực hiện:

    1. Mở trang `https://the-internet.herokuapp.com/login`.

    2. Để trống username và password.

    3. Nhấn nút Login.

Kết quả mong đợi: Hiển thị thông báo `Your username is invalid!`.

