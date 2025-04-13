def calculate_net_salary(
    gross_salary,
    tax_class=1,
    has_children=False,
    health_insurance_percent=13.6,
    additional_health_insurance=1.3,
    church_tax=False
):
    # Социальные отчисления
    pension = gross_salary * 0.093  # Пенсионное
    unemployment = gross_salary * 0.012  # По безработице
    health = gross_salary * (health_insurance_percent + additional_health_insurance) / 100 / 2
    care = gross_salary * 0.01525  # Страховка на уход
    if not has_children and tax_class != 3:
        care += gross_salary * 0.0025  # Дополнительный взнос если нет детей

    social_total = pension + unemployment + health + care

    # Примерная формула подоходного налога (очень упрощенная)
    tax_base = gross_salary - social_total
    income_tax = 0

    if tax_class == 1:
        if tax_base < 10908:
            income_tax = 0
        elif tax_base <= 15999:
            income_tax = (tax_base - 10908) * 0.14
        elif tax_base <= 62809:
            income_tax = (tax_base - 15999) * 0.24 + 700
        else:
            income_tax = (tax_base - 62809) * 0.42 + 14000

    elif tax_class == 3:
        if tax_base < 23000:
            income_tax = 0
        else:
            income_tax = (tax_base - 23000) * 0.20

    elif tax_class == 5:
        income_tax = tax_base * 0.25

    # Церковный налог
    if church_tax:
        income_tax += income_tax * 0.09

    # Солидарный налог
    solidarity_tax = income_tax * 0.055 if income_tax > 16 else 0

    total_tax = income_tax + solidarity_tax
    net_salary = gross_salary - social_total - total_tax

    return {
        "gross_salary": round(gross_salary, 2),
        "net_salary": round(net_salary, 2),
        "social_contributions": round(social_total, 2),
        "income_tax": round(income_tax, 2),
        "solidarity_tax": round(solidarity_tax, 2),
        "tax_class": tax_class
    }


# 🧪 Пример использования:
if __name__ == "__main__":
    salary_info = calculate_net_salary(
        gross_salary=2350,
        tax_class=1,
        has_children=False,
        church_tax=False
    )
    for key, value in salary_info.items():
        print(f"{key}: {value} €")
