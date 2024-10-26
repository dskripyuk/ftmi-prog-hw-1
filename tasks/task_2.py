
#def print_table():
    #pass

#def read_id(str_):
    #pass

#def check_bill_validity(str_):
    #pass

#def calculate_remaining(input_amount, amount_left):
    #pass


# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы

# Your code here(づ ᴗ _ᴗ)づ♡

print('| ID  | ProductName | Цена |',
      '|-----|-------------|------|',
      '| 001 | Батончик    | 70   |',
      '| 002 | Вода        | 45   |',
      '| 003 | Газировка   | 64   |',
      '| 004 | Булочки     | 33   |',sep='\n')
def check_product(id):
    if id in ["001", "002", "003", "004"]:
        return True
    else:
        return False
def check_bill(bill):
    if int(bill) in [10, 50, 100, 500]:
        return True
    else:
        return False
def check_change(bill, product_price):
    change = bill - product_price
    if change >= 0 and change <= 467:
        print(f"Ваша сдача: {change} тугриков")
        return True
    else:
        print("Сумма сдачи должна быть от 0 до 467 тугриков")
        return False

product_id = input("Введите ID желаемого товара: ")
if check_product(product_id):
    product_price = 0
    switcher = {"001": 70,"002": 45,"003": 64,"004": 33}
    product_price = switcher[product_id]
    print(f"Внесите {product_price} тугриков")
    bill =input("Введите номинал купюры: ")
    while not check_bill(bill):
        print("Внесена фальшивая купюра")
        bill =input("Введите номинал купюры: ")
    total = 0
    while True:
        if not check_bill(bill):
            continue
        total += int(bill)
        if total >= product_price:
            if check_change(total, product_price):
                break
            else:
                print("Сумма сдачи должна быть от 0 до 467 тугриков")
                total = 0
        else:
            print(f"Осталось внести {product_price - total} тугриков")
        bill = input("Введите номинал купюры: ")
else:
    print("Товара с таким ID не существует")
