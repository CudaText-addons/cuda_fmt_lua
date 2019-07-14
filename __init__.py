from .lua_format import lua_format

def do_format(text):

    settings = {
        'tab_size': 4,
        'special_symbol_split': True,
        'bracket_split': False,
        }

    res = lua_format(text.splitlines(), settings)
    return res
