Quy trình làm việc với UML qua Git:

1. Tạo nhánh mới (Branch)
   Tuyệt đối không thao tác trực tiếp trên nhánh main. Khi cần thêm sơ đồ mới hoặc cập nhật sơ đồ cũ, phải tạo một nhánh làm việc riêng.
   Lệnh thực thi: git checkout -b update-auth-class-diagram

2. Chỉnh sửa (Edit)
   Mở các file .puml nằm trong thư mục docs/. Cập nhật cấu trúc class hoặc sequence bằng cú pháp text của PlantUML.

3. Ghi nhận thay đổi (Commit)
   Sau khi chỉnh sửa xong, phải lưu lại phiên bản thay đổi với một thông điệp (commit message) rõ ràng, giải thích ngắn gọn mình vừa làm gì để team dễ dàng nắm bắt.
   Lệnh thực thi: git add docs/class-diagram.pumlgit commit -m "docs: cập nhật phương thức login vào class diagram"

4. Đẩy nhánh lên GitHub (Push)
   Đưa nhánh làm việc chứa các thay đổi ở máy tính cá nhân lên (GitHub).
   Lệnh thực thi:git push origin update-auth-class-diagram

5. Yêu cầu Hợp nhất (Pull Request)
   Tạo một Pull Request (PR) từ nhánh của bản thân vào nhánh main. Viết mô tả ngắn gọn về những thay đổi kiến trúc bạn vừa thực hiện trong file UML.

6. Đánh giá & Hợp nhất (Review & Merge)
   - Review: Các thành viên khác sẽ vào xem PR, sử dụng tính năng Diff của Git để xem chi tiết những dòng mã .puml nào đã bị xóa hoặc thêm mới.
   - Merge: Sau khi team thống nhất sơ đồ đã hợp lý, PR sẽ được phê duyệt và Merge vào nhánh main.
