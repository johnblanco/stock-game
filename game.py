import random


def current_price(day):
    return random.randint(80, 120)


def clear():
    print("\n" * 500)


def update_account(price, account, option_selected):
    cash = account['cash']
    stocks = account['stocks']
    costs = account['costs']

    if 'c' in option_selected:
        stocks_to_buy = int(option_selected.replace('c', ''))
        transaction_value = stocks_to_buy * price
        cash = cash - transaction_value
        costs += 25

        stocks += stocks_to_buy

        if cash < 0:
            return account

    if 'v' in option_selected:
        stocks_to_sell = int(option_selected.replace('v', ''))
        transaction_value = stocks_to_sell * price
        cash = cash + transaction_value
        costs += 25

        stocks -= stocks_to_sell

        if stocks < 0:
            return account

    value = cash + (price * stocks) - costs
    return {
        'cash': cash,
        'stocks': stocks,
        'costs': costs,
        'value': value
    }


def main():
    day = 1
    account = {
        'cash': 10000,
        'stocks': 0,
        'costs': 0,
        'value': 10000
    }
    price = 100

    while True:
        clear()
        price = current_price(day)
        print("Dia {}".format(day))
        print("Precio actual {}".format(price))
        print("Acciones: {}, cash: {}, costos: {}, valor portfolio: {}".format(
            account['stocks'],
            account['cash'],
            account['costs'],
            account['value']))

        option_selected = input('ingrese opcion: ')
        account = update_account(price, account, option_selected)
        day += 1


if __name__ == "__main__":
    main()
