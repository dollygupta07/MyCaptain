class Rect:

	def __init__(self , length , breadth):
		self.length = length
		self.breadth = breadth

	def area(self):
		return self.length * self.breadth

def main():
	length = int(input("Enter length :"))
	breadth = int(input("Enter breadth :"))

	obj = Rect(length ,breadth)
	print("Area:"  ,obj.area())

if __name__ == '__main__':
	main()

