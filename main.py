import datetime
import pickle
from collections import defaultdict
import os

transactions = {}
transactions_to_count = {}
account_password = ''
balance = 0
threshold = int
transactions_more_than = {}


def collect_transactions_for_more_than(user_info):
    transactions = user_info['transactions']
    for key in transactions:
        yield key


def generate_list_of_transactions_more_than_threshold(user_info, threshold):
    generator_data = collect_transactions_for_more_than(user_info)
    dictionary_result = dict(zip(generator_data, generator_data))
    for key in dictionary_result:
        if transactions[key] >= threshold:
            transactions_more_than.update({key: transactions[key]})
    return transactions_more_than


def save_user_info():
    with open('user_info.txt', 'wb') as user_info_file:
        pickle.dump(user_info, user_info_file)


def main():
    if not os.path.exists('user_info.txt'):
        with open('user_info.txt', 'wb') as file:
            pass


if __name__ == '__main__':
    main()
    print(f'Добро пожаловать в банк КОСМОС!')
    option = input(f'Вы хотите восстановить сохраненные ранее данные? Введите "да" или "нет": ').lower()
    main()
    if option == 'да':
        try:
            if not os.path.exists('user_info.txt'):
                print(f'Отсутствуют ранее сохраненные данные.')
                exit()
            else:
                with open('user_info.txt') as file:
                    print(f'Данные восстановлены.')
        finally:
            pass
    elif option == 'нет':
        if not os.path.exists('user_info.txt'):
            with open('user_info.txt', 'wb') as file:
                pass
        else:
            os.remove('user_info.txt')

    while True:
        print()
        print(f'Приложение поможет Вам совершить любую из этих операций: ')
        print()
        print(f'1  - Cоздать аккаунт                     - 1\n'
              '2  - Внести деньги на счет               - 2\n'
              '3  - Снять деньги                        - 3\n'
              '4  - Вывести баланс на экран             - 4\n'
              '5  - Выставить ожидаемое пополнение      - 5\n'
              '6  - Выставить максимальный лимит        - 6\n'
              '7  - Применить транзакции                - 7\n'
              '8  - Статистика по ожидаемым пополнениям - 8\n'
              '9  - Фильтровать ожидаемые пополнения    - 9\n'
              '10 - Выйти из программы                  - 10\n')

        operation_choice = int(input("Введите НОМЕР нужной ОПЕРАЦИИ: "))

        try:
            operation_choice = int(input("Введите НОМЕР нужной ОПЕРАЦИИ: "))
            if 1 <= operation_choice < 11:
                pass
            else:
                raise ValueError
        except ValueError:
            print(f'Чтобы перейти к нужной операции, введите соответствующий номер '
                  f'операции (1-10). Другие символы не распознаются.')
            continue

        if operation_choice == 1:
            print(f'Приступим к созданию аккаунта в банке Космос.')
            print()
            name = input("Введите ФИО полностью: ")
            balance = 0
            print()
            year_of_birth = input("Введите ГОД рождения: ")
            today = datetime.date.today()
            year = today.year
            age = int(year) - int(year_of_birth)
            print()
            if age % 10 == 1 and age != 11:
                print(f'Создаем аккаунт для: {name} ({age} год).')
            elif 1 < age % 10 < 5:
                print(f'Создаем аккаунт для: {name} ({age} года).')
            else:
                print(f'Создаем аккаунт для: {name} ({age}) лет).')
            print()
            account_password = str(input("Придумайте ПАРОЛЬ для этого аккаунта: "))
            user_info = {'name': name, 'balance': balance, 'year_of_birth': year_of_birth,
                         'account_password': account_password}
            save_user_info()
            print()
            print(f'Введенные данные сохранены. Аккаунт создан!')

        elif operation_choice == 2:
            print(f'Внести деньги на счет в банке КОСМОС.')
            print()
            amount_to_add = input("Введите СУММУ ПОПОЛНЕНИЯ в RUB: ")
            balance = 0 + int(amount_to_add)
            with open('user_info.txt', 'rb') as user_info_file:
                user_info = pickle.load(user_info_file)
                user_info.update({'balance': balance})
            save_user_info()
            print()
            print(f'Вы успешно пополнили счет на сумму {amount_to_add} RUB.')

        elif operation_choice == 3:
            with (open('user_info.txt', 'rb') as user_info_file):
                user_info = pickle.load(user_info_file)
                while str(input("Введите ПАРОЛЬ от аккаунта: ")) != user_info['account_password']:
                    print(f'Введен неверный пароль. Попробуйте еще раз!')
                    continue
                else:
                    print(f'Текущий баланс счета: {user_info['balance']} RUB.')
                    amount_to_withdraw = int(input("Введите СУММУ для СНЯТИЯ в RUB: "))
                    while amount_to_withdraw > user_info['balance']:
                        print(f'Запрашиваемая сумма превышает баланс счета.')
                        break
                    else:
                        balance = balance - amount_to_withdraw
                        user_info.update({'balance': balance})
                        print(f'Операция по снятию совершена.')
                        print(f'Текущий БАЛАНС счета: {user_info['balance']} RUB.')
            save_user_info()

        elif operation_choice == 4:
            with open('user_info.txt', 'rb') as user_info_file:
                user_info = pickle.load(user_info_file)
                while True:
                    input_password = str(input("Чтобы увидеть баланс счета на экране, введите ПАРОЛЬ от аккаунта: "))
                    if input_password != user_info['account_password']:
                        print()
                        print(f'Введен неверный пароль. Попробуйте еще раз!')
                        continue
                    else:
                        print(f'Текущий БАЛАНС счета: {user_info['balance']} RUB.')
                        break

        elif operation_choice == 5:
            replenishment_amount = int(input(f'Введите СУММУ ожидаемого пополнения: '))
            replenishment_purpose = input(f'Введите НАЗНАЧЕНИЕ ожидаемого пополнения: ')
            with open('user_info.txt', 'rb') as user_info_file:
                user_info = pickle.load(user_info_file)
            if 'transactions' not in user_info:
                user_info['transactions'] = {replenishment_purpose: replenishment_amount}
                save_user_info()
            else:
                with open('user_info.txt', 'rb') as user_info_file:
                    user_info = pickle.load(user_info_file)
                    transactions = user_info['transactions']
                    transactions.update({replenishment_purpose: replenishment_amount})
                save_user_info()
            with open('user_info.txt', 'rb') as user_info_file:
                user_info = pickle.load(user_info_file)
                transactions = user_info['transactions']
                print(f'Количество ожидаемых пополнений: {len(transactions)}')

        elif operation_choice == 6:
            limit = int(input(f'Установите МАКСИМАЛЬНУЮ СУММУ, которая должна быть на счету (RUB): '))
            with open('user_info.txt', 'rb') as user_info_file:
                user_info = pickle.load(user_info_file)
                user_info.update({'limit': limit})
            save_user_info()
            print(f'Вы установили максимальный лимит: {limit} RUB.')
            print()

        elif operation_choice == 7:
            with (open('user_info.txt', 'rb') as user_info_file):
                user_info = pickle.load(user_info_file)
                limit = user_info['limit']
                balance = user_info['balance']
                transactions = user_info['transactions']
            print(f'Учитывая максимальный лимит {user_info['limit']} RUB: ')
            for key in transactions:
                if balance + int(transactions[key]) <= limit and balance <= limit:
                    balance = balance + int(transactions[key])
                    print(f'Транзакция «{key}» на сумму {transactions[key]} RUB успешно ПРИМЕНЕНА.')
                else:
                    print(f'Транзакция «{key}» на сумму {transactions[key]} RUB НЕ ПРИМЕНЕНА (превышен лимит).')
            user_info['transactions'] = {key: transactions[key]}
            save_user_info()
            print()

        elif operation_choice == 8:
            with open('user_info.txt', 'rb') as user_info_file:
                user_info = pickle.load(user_info_file)
                transactions = user_info['transactions']
                replenishment_amounts = transactions.values()
                count_values = defaultdict(int)
                for value in replenishment_amounts:
                    count_values[value] += 1
                for value, count in count_values.items():
                    print(f'{value} RUB: {count} платеж(а)')

        elif operation_choice == 9:
            threshold = int(input(f'Установите сумму транзакции в качестве нижнего порога для фильтрации: '))
            with open('user_info.txt', 'rb') as user_info_file:
                user_info = pickle.load(user_info_file)
                transactions = user_info['transactions']
            collect_transactions_for_more_than(user_info)
            generate_list_of_transactions_more_than_threshold(user_info, threshold)

            print(f'Ожидаемые пополнения от {threshold} RUB:')
            for key in transactions_more_than:
                print(f'{key} на сумму {transactions_more_than[key]} RUB')

        elif operation_choice == 10:
            print(f'Спасибо! Всего доброго!')
            break
