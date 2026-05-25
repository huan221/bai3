raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

# hàm xử lý số điện thoại
def process_phone(phone):
    phone = phone.replace("-", "").strip()
    
    if phone.isdigit():
        return "******" + phone[-4:]
    else:
        return "Invalid Format"

# hàm chuẩn hóa toàn bộ dữ liệu
def normalize_data(raw_data):
    employees = raw_data.split("|")
    result = []

    for emp in employees:
        parts = emp.split(";")

        emp_id = parts[0].strip().upper()
        name = parts[1].strip().title()
        phone = parts[2].strip()
        dept = parts[3].strip().upper()

        phone = process_phone(phone)

        result.append([emp_id, name, phone, dept])

    return result


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn (1-4): ")

    if choice == "1":
        print("Dữ liệu gốc:")
        print(raw_data)

    elif choice == "2":
        data = normalize_data(raw_data)

        print("\n{:<10} {:<20} {:<15} {:<10}".format("ID", "Họ tên", "SĐT", "Phòng"))
        print("-" * 60)

        for emp in data:
            print("{:<10} {:<20} {:<15} {:<10}".format(emp[0], emp[1], emp[2], emp[3]))

    elif choice == "3":
        search_id = input("Nhập mã nhân viên: ").strip().upper()
        data = normalize_data(raw_data)

        found = False

        for emp in data:
            if emp[0] == search_id:
                print("\nTìm thấy nhân viên:")
                print("ID:", emp[0])
                print("Họ tên:", emp[1])
                print("SĐT:", emp[2])
                print("Phòng:", emp[3])
                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")