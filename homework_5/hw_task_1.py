# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)
from collections import namedtuple, deque


def averaging(*args):
    return sum(args) / len(args)


num_of_companies = int(input('Введите количество компаний: '))

Company = namedtuple('Company', 'name quart_1 quart_2 quart_3 quart_4')

list_of_companies = []

for i in range(num_of_companies):
    print(f'Компания №{i + 1}: ')
    list_of_companies.append(
        Company(
            input('Введите название компании: '),
            int(input('Введите прибыль за 1ый квартал: ')),
            int(input('Введите прибыль за 2ой квартал: ')),
            int(input('Введите прибыль за 3ий квартал: ')),
            int(input('Введите прибыль за 4ый квартал: ')))
    )
    print('*' * 50)

company_profit = {}

for company in list_of_companies:
    company_profit[company.name] = averaging(company.quart_1,
                                             company.quart_2,
                                             company.quart_3,
                                             company.quart_4)

average_profit = averaging(*company_profit.values())
print(f'Средняя прибыль по рынку за год {average_profit}')

for company, profit in company_profit.items():
    if profit >= average_profit:
        print(f'У компании {company} прибыль выше среднего по рынку')
    else:
        print(f'У компании {company} прибыль ниже среднего по рынку')
