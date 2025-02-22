from inspect import currentframe

# import class_chap02

print( 'TEST---------------------------TEST' )

def pr(self):
	print( 'PR---------------------------PR' )
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )
	print( 'PR---------------------------PR' )
