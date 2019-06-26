from IPython.core.magic import magics_class, line_magic, Magics

@magics_class
class MyMagicClass(Magics):
	def __init__(self, shell):
		super(MyMagicClass, self).__init__(shell)
		self.count = 0

	@line_magic
	def magicpackagelinemagic(self, line):
		self.count += 1
		print('this magic has been executed %d time%s' % (self.count, 's' if self.count > 1 else ''))