__version__ = '0.0.1'

from .my_magic_class import MyMagicClass

def load_ipython_extension(ipython):
	print('Executing load_ipython_extension in magicpackage')
	ipython.register_magics(MyMagicClass)