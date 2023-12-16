import stock_price


def update_player_state(player, spy_price, tecl_price):
    if 'selected_action' not in player:
        return player
    selected_action = player['selected_action']
    if selected_action == "vender TECL":
        player['cash'] += player['tecl'] * tecl_price
        player['tecl'] = 0
    if selected_action == "vender SPY":
        player['cash'] += player['spy'] * spy_price
        player['spy'] = 0
    if selected_action == "comprar TECL":
        stocks = player['cash'] // tecl_price
        cash_available = player['cash'] - stocks * tecl_price
        player['tecl'] += int(stocks)
        player['cash'] = cash_available
        player['tecl_price'] = tecl_price
    if selected_action == "comprar SPY":
        stocks = player['cash'] // spy_price
        cash_available = player['cash'] - stocks * spy_price
        player['spy'] += int(stocks)
        player['cash'] = cash_available
        player['spy_price'] = spy_price
    player['cash'] = round(player['cash'])
    player['selected_action'] = None
    return player


def update_profit(player, spy_price, tecl_price):
    player['profit'] = player['cash'] + player['spy'] * spy_price + player['tecl'] * tecl_price
    player['profit'] = int(player['profit'])
    return player


def update_available_actions(player, spy_price, tecl_price):
    cash = player['cash']
    player['available_actions'] = []
    if cash >= tecl_price:
        player['available_actions'].append("comprar TECL")
    if cash >= spy_price:
        player['available_actions'].append("comprar SPY")
    if player['tecl'] > 0:
        player['available_actions'].append("vender TECL")
    if player['spy'] > 0:
        player['available_actions'].append("vender SPY")

    player['available_actions'].append("pasar")
    return player


def next_month(game_state):
    month = game_state['month']
    spy_price = game_state['spy_prices'][month]
    tecl_price = game_state['tecl_prices'][month]

    new_state = game_state.copy()
    new_state['players'] = list(
        map(lambda player: update_player_state(player, spy_price, tecl_price), new_state['players']))

    month += 1
    new_state['month'] = month

    new_spy_price = game_state['spy_prices'][month]
    new_tecl_price = game_state['tecl_prices'][month]

    new_state['players'] = list(
        map(lambda player: update_profit(player, new_spy_price, new_tecl_price), new_state['players']))

    new_state['players'] = list(
        map(lambda player: update_available_actions(player, new_spy_price, new_tecl_price), new_state['players']))

    return new_state


def initial_game_state():
    prices = stock_price.stock_prices()
    tecl_prices = prices['TECL'].values.tolist()
    spy_prices = prices['SPY'].values.tolist()

    player_initial_state = {
        'cash': 100000,
        'spy': 0,
        'spy_price': 0,
        'tecl': 0,
        'tecl_price': 0,
        'profit': 0,
        'available_actions': ["comprar TECL", "comprar SPY", "pasar"],
    }
    return {
        'month': 0,
        'tecl_prices': tecl_prices,
        'spy_prices': spy_prices,
        'players': [
            player_initial_state,
            player_initial_state,
        ]
    }
