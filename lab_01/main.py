def get_orders():

    orders = []

    while True:
            try:
                count = int(input("Введите количество заказов: "))
                if count <= 0:
                    print("Количество не может быть отрицательным или равным нулю!")
                    continue
                break
            except ValueError:
                print("Ошибка! Введите количество заказов!")

    for i in range(count):
        while True:
            try:
                price = float(input(f"Введите стоимость заказа №{i + 1}: "))
                if price < 0:
                    print("Цена не может быть отрицательной!")
                    continue
                break
            except ValueError:
                print("Ошибка! Введите цену товара!")
            
        orders.append(price)

    return orders

def analyze_orders(orders):
    
    total_amount = sum(orders)
    average_cost = total_amount/ len(orders)
    max_order = max(orders)
    above_average_cost = sum(1 for cost in orders if cost > average_cost)
    return total_amount, average_cost, max_order, above_average_cost 

def calculate_discount(cost, threshold = 5000, discount_percent = 0.10):

    if cost > threshold:
        discount = cost * discount_percent
        total = cost - discount
        return discount, total

    return 0.0, cost 
   
def main():
    orders = get_orders()
    if not orders:
         print("Список заказов пуст!")
         return

    total, avg, max_val, above_avg = analyze_orders(orders)

    print('\n' + "=" * 40)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА ЗАКАЗОВ")
    print(f"1.Общая сумма заказов: {total:.2f}руб.")
    print(f"2.Средняя стоимость заказа: {avg:.2f}руб.")
    print(f"3. Максимальный заказ: {max_val:.2f}руб.")
    print(f"4. Заказов со стоимостью выше средней: {above_avg}.")
    print("\n" + "=" * 40)

    for idx, cost in enumerate(orders, start=1):
         discount, final_cost  = calculate_discount(cost)
         if discount > 0:
              print(f"Заказ №{idx}: {cost:.2f} руб. -> Скидка: {discount:.2f} руб. -> К оплате: {final_cost :.2f} руб.")
         else:
            print(f"Заказ  №{idx}:  {cost:.2f} руб. -> Без скидки")
    print("\n" + "=" * 40)
         

if __name__ == "__main__":
    main()