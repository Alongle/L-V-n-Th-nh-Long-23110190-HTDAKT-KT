# =========================
# Bài 1: Số lẻ từ 1 đến 20
# =========================
# Sử dụng if condition để lọc
odds = [x for x in range(1, 21) if x % 2 != 0]
print("Số lẻ:", odds)


# =========================
# Bài 2: Chuỗi "Hello" lặp 5 lần
# =========================
# Lặp với range()
hellos = ["Hello" for _ in range(5)]
print("Danh sách Hello:", hellos)


# =========================
# Bài 3: Số chia hết cho 3
# =========================
gen = (x for x in range(16) if x % 3 == 0)
print("Chia hết cho 3:", list(gen))


# =========================
# Bài 4: Dùng next()
# =========================
gen = (x for x in range(16) if x % 3 == 0)

first = next(gen)   # 0
second = next(gen)  # 3

print("Giá trị đầu:", first)
print("Giá trị thứ hai:", second)