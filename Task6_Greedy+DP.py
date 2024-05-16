# Greedy algorithm

def maximize_calories_within_budget(dishes, budget):
    """
    Функція, яка максимізує співвідношення калорій до вартості, не перевищуючи заданий бюджет.

    :param dishes: список страв, де кожна страва представлена словником {'name': str, 'calories': int, 'cost': int}
    :param budget: максимальний допустимий бюджет
    :return: список назв страв, які максимізують співвідношення калорій до вартості в межах бюджету
    """
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    for dish in dishes:
        dish['ratio'] = dish['calories'] / dish['cost']
    
    # Сортуємо страви за цим співвідношенням в порядку спадання
    dishes.sort(key=lambda x: x['ratio'], reverse=True)
    
    selected_dishes = []
    total_cost = 0
    
    # Додаємо страви до результату, поки не буде перевищено бюджет
    for dish in dishes:
        if total_cost + dish['cost'] <= budget:
            selected_dishes.append(dish['name'])
            total_cost += dish['cost']
        else:
            break
    
    return selected_dishes

# Приклад використання
dishes = [
    {'name': 'Страва 1', 'calories': 500, 'cost': 50},
    {'name': 'Страва 2', 'calories': 800, 'cost': 100},
    {'name': 'Страва 3', 'calories': 200, 'cost': 20},
    {'name': 'Страва 4', 'calories': 300, 'cost': 25},
    {'name': 'Страва 5', 'calories': 400, 'cost': 40},
]

budget = 100
result = maximize_calories_within_budget(dishes, budget)
print("Страви, які максимізують співвідношення калорій до вартості в межах бюджету:", result)



# Dynamic programming
def maximize_calories_dp(dishes, budget):
    """
    Функція, яка максимізує калорійність при заданому бюджеті за допомогою динамічного програмування.

    :param dishes: список страв, де кожна страва представлена словником {'name': str, 'calories': int, 'cost': int}
    :param budget: максимальний допустимий бюджет
    :return: список назв страв, які максимізують калорійність в межах бюджету
    """
    n = len(dishes)
    # Створення таблиці для зберігання максимальних калорій для кожного підбюджету
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці dp
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if dishes[i - 1]['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - dishes[i - 1]['cost']] + dishes[i - 1]['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних страв
    result = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(dishes[i - 1]['name'])
            w -= dishes[i - 1]['cost']

    result.reverse()
    return result

# Приклад використання
dishes = [
    {'name': 'Страва 1', 'calories': 500, 'cost': 50},
    {'name': 'Страва 2', 'calories': 800, 'cost': 100},
    {'name': 'Страва 3', 'calories': 200, 'cost': 20},
    {'name': 'Страва 4', 'calories': 300, 'cost': 25},
    {'name': 'Страва 5', 'calories': 400, 'cost': 40},
]

budget = 100
result = maximize_calories_dp(dishes, budget)
print("Страви, які максимізують калорійність в межах бюджету:", result)
