"""Wrapps functions output with long strings
above and below."""
def decorator_func(func):
    def wrapper_func():
        print('Z' * 20)
        func()
        print('Z' * 20)
    return wrapper_func



@decorator_func
def game_prompt():
    print('GAME STARTED !!!')

@decorator_func
def top_winners():
    print('GOLDEN PLAYERS!!!')
# decorator_func(game_prompt)()
#game_prompt()