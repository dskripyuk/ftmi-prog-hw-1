
# Your code here (づ｡◕‿‿◕｡)づ
def validate_items(items):
    valid_items = {"меч", "лук", "топор", "щит", "зелье"}
    for item in items:
        if item not in valid_items:
            return False
    return True

choices = []
for i in range(3):
    while True:
        input_items = input(f"Введите предметы для авантюриста {i + 1}: ").strip().split()
        if validate_items(input_items):
            choices.append(set(input_items))
            break
        else:
            print("Неверный предмет, попробуйте снова")

common_items = choices[0] & choices[1] & choices[2]
print(len(common_items))

