def government_format(func):
    def wrapper(company_data):
        result = func(company_data)
        return f"=== ГОСУДАРСТВЕННАЯ ОРГАНИЗАЦИЯ ===\n{result}\n"
    return wrapper

def ngo_format(func):
    def wrapper(company_data):
        result = func(company_data)
        return f"--- НКО ---\n{result}\n"
    return wrapper

def commercial_format(func):
    def wrapper(company_data):
        result = func(company_data)
        return f">> КОММЕРЧЕСКАЯ ОРГАНИЗАЦИЯ <<\n{result}\n"
    return wrapper

def financial_report(data):
    income = data['income']
    expenses = data['expenses']
    profit = income - expenses
    tax = profit * 0.2 if profit > 0 else 0
    return f"Доходы: {income}\nРасходы: {expenses}\nПрибыль: {profit}\nНалог: {tax}"

company_data = {
    'name': 'ООО "Ромашка"',
    'year': 2024,
    'income': 5000000,
    'expenses': 3200000
}

print(government_format(financial_report)(company_data))
print(ngo_format(financial_report)(company_data))
print(commercial_format(financial_report)(company_data))