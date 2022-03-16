def say_hi():
	print("Hi!")

def shout(message="Hi"):
    	print(f"{message}!")

def main():	 #create main to use this as moduel
	say_hi()
	shout()
	shout("I love python")
	shout(message="And keyword arguments")
 
if __name__ == "__main__":	#only run main when not being used as module
     main()
