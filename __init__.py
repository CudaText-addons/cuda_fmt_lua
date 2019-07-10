from . import lua_format
import cudatext as app

def do_format(text):
    lua_format.SETTING_TAB_SIZE = app.ed.get_prop(app.PROP_TAB_SIZE)
    text = lua_format.format(text)
    return text
