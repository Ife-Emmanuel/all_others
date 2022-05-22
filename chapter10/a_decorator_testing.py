import decorator_function


@decorator_function.decorator_func
def game_prompt():
    print('GAME STARTED !!!')


game_prompt()