class node:
	value = ""
	left = None
	right = None
	
	def _init__(value):
		self.value = value;

symbols = ["^", "v", ">", "=", "!"]

n1 = node("p")
n2 = node("^")
n3 = node("q")

interpretation = {"p"
