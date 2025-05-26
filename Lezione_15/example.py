# # PATH: str = "Lezione_15/example.txt"
# # mode: str = "w"
# # encoding: str = "utf-8"

# # file = open(PATH, mode=mode, encoding=encoding)
# # # output: str = file.read()
# # input_text: str = input("Enter text to write: \n")
# # # output: str = file.write("Ciao belo")
# # output: str = file.write(input_text)
# # print(output)
# # file.close
# # print(file)

# ########################################

# # with open("example.txt", mode = "w", encoding="utf-8") as file:

# #     message: str = "Hello world!\n"
# #     written_char: int = file.write(message)
# #     print(f"Written characters: {written_char}")

# #########################################

# import time

# class StopWatch:

#     def __init__(self):

#         self.start_time = None
#         self.stop_time = None

#     def __enter__(self):

#         self.start_time = time.time()

#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):

#         self.end_time = time.time()
#         elapsed_time = self.end_time - self.start_time
#         print(f"Elapsed Time: {elapsed_time:.8f} seconds")

#         if exc_type is not None:

#             print(f"Exception type: {exc_type}")
#             print(f"An error occurred: {exc_value}")
#             print(f"Traceback: {traceback}")

#         return False
    

# with StopWatch():

#     print("Hello, world!")
#     time.sleep(2)
#     print("Goodbye, world!")

import json

PATH: str = "Lezione_15/config.json"
mode: str = "r"
encoding: str = "utf-8"

config = None

def connect(host, port):

    print(f"Connected to {host}: {port}")

with open(PATH, mode=mode, encoding=encoding) as file:

    config: dict = json.load(file)


# print(f"Host: {config["server"]["host"]} Port: {config["server"]["port"]}")

print(config)

# connect(host = config["server"]["host"], port=config["server"]["port"])

config["AGGIUNTA"] = "NUOVO"
config["server"]["host"] = "google.it"

with open(PATH, mode = "w") as file:

    json.dump(config, file, indent = 4) 