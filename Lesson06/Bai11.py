def enter_data():
    while True:
        n = input("Nhập một số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhấp sô không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")

"""
Hàm enter_data kiểm tra số nhập vào:
- Nếu đúng số nguyên dương sẽ in ra 'Đã nhập số dương' và trả về kết quả n.
- Nếu không phải số nguyên dương thì in ra 'Đã nhấp sô không dương. Chương trình sẽ tiếp tục!' và chạy lại chương trình.
- Nếu không phải số Nguyên thì in ra 'Dữ liệu đã nhập không phải số nguyên' và chạy lại chương trình.
"""