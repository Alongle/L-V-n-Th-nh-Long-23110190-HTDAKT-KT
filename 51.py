# =========================
# Bài 1: Quản lý Sách
# =========================
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print("Tên sách:", self.title)
        print("Tác giả:", self.author)
        print("Năm xuất bản:", self.year)
        print("----------------------")


# =========================
# Bài 2: Tài khoản Ngân hàng
# =========================
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Nạp", amount, "thành công")
        else:
            print("Số tiền không hợp lệ")

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print("Rút", amount, "thành công")
        else:
            print("Không đủ tiền hoặc số tiền không hợp lệ")

    def get_balance(self):
        return self.__balance


# =========================
# Bài 3: Kế thừa
# =========================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Tên:", self.name)
        print("Tuổi:", self.age)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(self.name, "đang học Python OOP")

    def display_student(self):
        self.display_info()
        print("Mã sinh viên:", self.student_id)
        print("----------------------")


# =========================
# Bài 4: Phương tiện giao thông
# =========================
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Hãng:", self.brand)
        print("Model:", self.model)
        print("Năm sản xuất:", self.year)


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print("Số cửa:", self.num_doors)
        print("----------------------")


class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print("Loại xe:", self.type)
        print("----------------------")


# =========================
# Chương trình chính
# =========================

print("===== QUẢN LÝ SÁCH =====")
book1 = Book("Con đường đến đại học Thanh Hoa", "Nguyễn Quốc Khánh", 1936)
book2 = Book("Nguyễn Khánh lưu lạc xứ sở Nemchuazabeth", "Alongle", 2005)

book1.display_info()
book2.display_info()


print("\n===== TÀI KHOẢN NGÂN HÀNG =====")
acc1 = BankAccount("363636")

acc1.deposit(360)
acc1.withdraw(360)

print("Số tài khoản:", acc1.get_account_number())
print("Số dư:", acc1.get_balance())


print("\n===== THÔNG TIN SINH VIÊN =====")
student1 = Student("Nguyễn Quốc Khánh", 36, "SV036")

student1.display_student()
student1.study()


print("\n===== PHƯƠNG TIỆN GIAO THÔNG =====")

car1 = Car("Toyota", "Camry", 2020, 4)
bike1 = Bike("Giant", "ATX", 2022, "Mountain")

car1.display_info()
bike1.display_info()