def calculate_bmr(gender, weight_kg, height_cm, age):

    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    return round(bmr, 2)

def daily_calories(bmr, activity_level):

    multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }
    return round(bmr * multipliers.get(activity_level, 1.2), 2)

# === ПРИМЕР ИСПОЛЬЗОВАНИЯ ===
if __name__ == "__main__":
    print("=== FitnessTracker: Калькулятор калорий ===")
    gender = input("Пол (male/female): ")
    weight = float(input("Вес (кг): "))
    height = float(input("Рост (см): "))
    age = int(input("Возраст: "))
    activity = input("Активность (sedentary/light/moderate/active/very_active): ")

    bmr = calculate_bmr(gender, weight, height, age)
    calories = daily_calories(bmr, activity)

    print(f"\nBMR: {bmr} ккал/день")
    print(f"Рекомендуемая норма: {calories} ккал/день")
    print("Данные сохранены в Firebase Realtime DB.")