# Dưới đây là phần thực hành và các câu lệnh chạy để làm bài test tuần 4
## Trước hết em kiểm tra các công cụ:
    *mở cmd, sử dụng lệnh python --version  start chrome    pip --version
    Đồng thời sử dụng github để upload
    Để đam bảo công cụ sử như python có đúng phiên bản, mở được trình duyệt chrome, xem pip đã có sẵn hay chưa
## Tiếp theo là Tạo một kho lưu trữ (repository) mới trên GitHub
    Vào GitHub, chọn New repository, đặt tên ___________.
    Nên chọn Add a README file khi tạo repository nếu muốn GitHub khởi tạo sẵn branch main và một commit ban đầu
    
    Từ bước này, Mở Terminal/Command Prompt trên máy tính, clone kho mã về và tạo cấu trúc nhánh
    cd C:\Users\ADMIN
    git clone <link-github-cua-ban>
    cd selenium-automation-project

    Kiểm tra Branch:
    git branch
    git status
    Nếu repository đã được khởi tạo với main, ta sẽ làm việc trên branch này trước khi tạo branch bài tập

    Tạo branch dành riêng cho Week 4
    git switch -c week-04
## Tạo thư mục và môi trường kiểm thử
    Sau khi chuyển sang branch week-04, tạo thư mục dành cho bài tập
    Cấu trúc thư mục sẽ có dạng
    selenium-automation-project/
    └── tuan-04/

    Tạo môi trường ảo Python
    python -m venv venv
    Lệnh này tạo môi trường ảo tên venv để tách các thư viện của bài tập khỏi môi trường Python chung trên máy

    Kích hoạt môi trường ảo, trên cmd:
    venv\Scripts\activate
    Khi thành công, đầu dòng lệnh sẽ có (venv): (venv) C:\Users\ADMIN\selenium-automation-project\tuan-04>

    Cài Selenium và pytest: Selenium: điều khiển trình duyệt để tự động kiểm thử, pytest: phát hiện và thực thi các hàm kiểm thử Python
    pip install selenium pytest
## Viết test và thực hiện kiểm thử
    Tạo file test_smoke.py
    Trong thư mục tuan-04, tạo file test_smoke.py và viết code:
    //
        from selenium import webdriver

        def test_smoke_the_internet():
            # Setup
            driver = webdriver.Chrome()

            try:
                # Act
                driver.get("https://the-internet.herokuapp.com/")

                # Assert
                actual_title = driver.title
                assert actual_title == "The Internet", (
                    f"Lỗi: Tiêu đề thực tế là '{actual_title}'"
                )

            finally:
                # Teardown
                driver.quit()
    //
    Chạy test:
    Đảm bảo CMD đang ở thư mục tuan-04 và môi trường ảo đã được kích hoạt
    pytest test_smoke.py
    Bài sẽ pass nếu không có lỗi được tìm thấy và ngược lại

## Chuẩn bị các file trước khi đưa lên GitHub
    Trong bài Week 4, bạn đã có các file:

    test_smoke.py
    Code Selenium và bài kiểm thử.

    README.md
    Mô tả bài tập, lý thuyết và nhật ký lỗi.

    notes.md
    Ghi chú bổ sung của bài Week 4.

    requirements.txt
    Danh sách thư viện cần cài đặt.

    .gitignore
    Bỏ qua các file và thư mục không cần đưa lên Git.

    Nội dung .gitignore bao gồm: venv/  __pycache__/    .pytest_cache/
    Vì đâu là các dự liệu nặng, quan trọng không nên đưa lên github
## Đưa bài lên GitHub
    Kiểm tra branch
    git branch
    git switch week-04

    Kiểm tra thay đổi
    git status
    Git có thể hiển thị file mới là Untracked files, hoặc file đã sửa là modified

    Nếu muốn đưa tất cả thay đổi phù hợp trong thư mục hiện tại vào staging
    git add .

    Kiểm tra staging
    git status

    Commit
    git commit -m

    Push lên GitHub
    git push origin week-04
    
