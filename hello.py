import sys

def hello_world():
	print 'Hello, World!'

def main():
	for i in range(5):
		hello_world()

	sys.exit()

if __name__ == '__main__':
	main()

