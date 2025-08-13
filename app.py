def hello():
    print("Hello, World!")  # Code đơn giản để SonarQube phân tích
    unused_var = 42  # Tạo một lỗi nhỏ để SonarQube phát hiện
if __name__ == "__main__":
    hello()