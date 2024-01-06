import random
import string

def generate_random_email():
    username_length = random.randint(6, 12)  # Độ dài ngẫu nhiên của tên người dùng (từ 6 đến 12 ký tự)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))  # Tạo tên người dùng ngẫu nhiên

    email = f"{username}@gmail.com"  # Kết hợp tên người dùng với domain @gmail.com
    return email

# Sử dụng hàm để tạo một địa chỉ email ngẫu nhiên và in ra
random_email = generate_random_email()
print(random_email)
