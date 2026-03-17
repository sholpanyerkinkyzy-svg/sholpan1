# 1.
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


#2
import csv
with open('employees.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'department', 'salary']) # Тақырыбы
    writer.writerows([
        ['Ali', 'IT', 500000],
        ['Dana', 'HR', 300000],
        ['Arman', 'IT', 600000],
        ['Aruzhan', 'Marketing', 400000],
        ['Dias', 'IT', 450000]
    ])

employees = []
with open('employees.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['salary'] = int(row['salary'])
        employees.append(row)

total_sal = sum(e['salary'] for e in employees)
avg_salary = total_sal / len(employees)


dept_totals = {}
for e in employees:
    dept = e['department']
    if dept not in dept_totals:
        dept_totals[dept] = []
    dept_totals[dept].append(e['salary'])


dept_avg = {dept: sum(sols)/len(sols) for dept, sols in dept_totals.items()}
best_dept = max(dept_avg, key=dept_avg.get)


top_worker = max(employees, key=lambda x: x['salary'])
high_earners = [e for e in employees if e['salary'] > avg_salary]


with open('high_salary.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'department', 'salary'])
    writer.writeheader()
    writer.writerows(high_earners)

print("Талдау аяқталды. 'high_salary.csv' файлы жасалды.")


#3
import json
orders_data = [
    {
        "order_id": 1,
        "user": "Ali",
        "items": ["phone", "case"],
        "total": 300000
    },
    {
        "order_id": 2,
        "user": "Dana",
        "items": ["laptop"],
        "total": 800000
    },
    {
        "order_id": 3,
        "user": "Ali",
        "items": ["mouse", "keyboard"],
        "total": 70000
    }
]
with open("orders.json", "w", encoding="utf-8") as f:
        json.dump(orders_data, f, indent=4)

with open("orders.json", "r", encoding="utf-8") as f:
        orders = json.load(f)

total_revenue = 0
user_orders_count = {}
items_count = {}
total_items_sold = 0
max_price = 0
top_user = ""

for order in orders:
    user = order["user"]
    total_revenue += order["total"]
    user_orders_count[user] = user_orders_count.get(user, 0) + 1

for item in order['items']:
    total_items_sold += 1
    items_count[item] = items_count.get(item,0) +1

    if order["total"] > max_price:
        max_price = order["total"]
        top_user = user

        most_popular_item = max(items_count, key=items_count.get)
summary = {
    "total_revenue": total_revenue,
    "top_user": top_user,
    "most_popular_item": most_popular_item,
    "total_orders": len(orders)
}

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=4, ensure_ascii=False)











