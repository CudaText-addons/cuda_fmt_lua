from .lua_format import lua_format
import cudatext as app

def do_format(text):

    settings = {
        'tab_size': app.ed.get_prop(app.PROP_TAB_SIZE),
        'special_symbol_split': True,
        'bracket_split': False,
        }

    res = lua_format(text.splitlines(), settings)
    return res
