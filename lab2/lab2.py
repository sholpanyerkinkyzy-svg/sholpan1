# 1. Лог файлын жасау
with open("shop_logs.txt", "w", encoding="utf-8") as f1:
    f1.write("2026-02-01;user_1;LOGIN\n")
    f1.write("2026-02-01;user_2;LOGIN\n")
    f1.write("2026-02-01;user_1;BUY;120\n")
    f1.write("2026-02-01;user_3;LOGIN\n")
    f1.write("2026-02-01;user_2;BUY;300\n")
    f1.write("2026-02-01;user_1;BUY;50\n")
    f1.write("2026-02-01;user_2;LOGOUT\n")


unique_users = set()
total_buys = 0
total_revenue = 0
user_spending = {}


with open("shop_logs.txt", "r", encoding="utf-8") as logs:
    for line in logs:
        data = line.strip().split(';')
        user_id = data[1]
        action = data[2]

        unique_users.add(user_id)

        if action == 'BUY':
            price = int(data[3])
            total_buys += 1
            total_revenue += price

            if user_id in user_spending:
                user_spending[user_id] += price
            else:
                user_spending[user_id] = price


if total_buys > 0:
    average_check = total_revenue / total_buys
    top_spender = max(user_spending, key=user_spending.get)
    top_spender_amount = user_spending[top_spender]
else:
    average_check = 0
    top_spender = "Жоқ"
    top_spender_amount = 0


with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(f"Уникалды қолданушылар саны: {len(unique_users)}\n")
    f.write(f"Барлық сатып алулар саны: {total_buys}\n")
    f.write(f"Жалпы сатылым сомасы: {total_revenue}\n")
    f.write(f"Ең көп жұмсаған қолданушы: {top_spender} ({top_spender_amount} тг)\n")
    f.write(f"Орташа чек: {average_check:.2f}\n")

print("Есеп report.txt файлына сәтті жазылды ")