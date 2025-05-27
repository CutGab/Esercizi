def make_shirt(size = "L", message:str = "I love Python"):
    print(f"The size of the shirt is: {size}. \n"
          f"The message on the shirt will be: '{message}'")
    
make_shirt()

make_shirt("M")

make_shirt("S", "I hate Python")