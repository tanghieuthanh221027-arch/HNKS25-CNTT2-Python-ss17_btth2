import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def display_products():
    print("--- DANH SÁCH TEM NHÃN ---")
    template = "Mã: {id:<10} | Tên: {name:<20} | Giá: {price} VND | Rating: {rating}*"
    for product in product_list:
        data = product.split("-")
        if len(data) != 4:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")
            continue

        if not data[2].isdigit():
            print(f"Bỏ qua sản phẩm {data[0]} do dữ liệu không hợp lệ")
            continue

        product_info = {"id": data[0], "name": data[1], "price": f"{int(data[2]):,}", "rating": data[3]}
        print(template.format_map(product_info))

def sort_key(product):
    data = product.split("-")
    return (-float(data[3]), int(data[2]))

def sort_products():
    product_list.sort(key=sort_key)
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product}")

def calculate_total():
    prices = []
    for product in product_list:
        data = product.split("-")

        if len(data) != 4:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")
            continue

        if not data[2].isdigit():
            print(f"Bỏ qua sản phẩm {data[0]} do dữ liệu không hợp lệ")
            continue

        prices.append(int(data[2]))
    if len(prices) == 0:
        return 0
    return functools.reduce(lambda x, y: x + y, prices)


while True:
    print("============= E-COMMERCE ANALYTICS =============")
    print("1. Hiển thị tem nhãn sản phẩm")
    print("2. Sắp xếp sản phẩm thông minh")
    print("3. Tính tổng giá trị kho hàng")
    print("4. Đóng hệ thống")
    print("================================================")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        display_products()

    elif choice == "2":
        sort_products()

    elif choice == "3":
        print("--- TỔNG GIÁ TRỊ KHO ---")
        total = calculate_total()
        print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND")

    elif choice == "4":
        print("Đóng hệ thống thành công!")
        break
    else:
        print("Lựa chọn không hợp lệ")