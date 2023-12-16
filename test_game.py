import game


def test_month_changes():
    state = game.initial_game_state()

    new_state = game.next_month(state)

    assert new_state['month'] == 1


def test_p1_buy_spy():
    player = {
        'cash': 100000,
        'spy': 10,
        'tecl': 10,
        'selected_action': 'comprar SPY'
    }

    updated_player = game.update_player_state(player, 420, 16)

    assert updated_player['cash'] == 40
    assert updated_player['spy'] == 248
    assert updated_player['spy_price'] == 420


def test_p1_available_actions_sell_not_allowed():
    #no puede vernder si no tiene acciones
    player = {
        'cash': 319,
        'spy': 1,
        'tecl': 0
    }

    spy_price = 420
    tecl_price = 16

    updated_player = game.update_available_actions(player, spy_price, tecl_price)
    available_actions = updated_player['available_actions']

    assert 'vender SPY' in available_actions
    assert 'comprar TECL' in available_actions
    assert 'vender TECL' not in available_actions
    assert len(available_actions) == 3

def test_p1_available_actions_buy_not_allowed():
    #no puede comprar si no tiene cash
    player = {
        'cash': 319,
        'spy': 1,
        'tecl': 0
    }

    spy_price = 420
    tecl_price = 16

    updated_player = game.update_available_actions(player, spy_price, tecl_price)
    available_actions = updated_player['available_actions']

    assert 'comprar SPY' not in available_actions
    assert 'comprar TECL' in available_actions
    assert len(available_actions) == 3

def test_p1_buy_tecl():
    player = {
        'cash': 160,
        'spy': 0,
        'tecl': 0,
        'selected_action': 'comprar TECL'
    }

    updated_player = game.update_player_state(player, 420, 16)

    assert updated_player['cash'] == 0
    assert updated_player['tecl'] == 10


def test_p1_sell_tecl():
    player = {
        'cash': 160,
        'spy': 0,
        'tecl': 10,
        'selected_action': 'vender TECL'
    }

    updated_player = game.update_player_state(player, 420, 16)

    assert updated_player['cash'] == 320
    assert updated_player['tecl'] == 0

