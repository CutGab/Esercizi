def check_length(word: str):

    if len(word) > 10:
        print("This string is longer than 10 characters")

    elif len(word) < 10:
        print("This string is smaller than 10 characters")

    else:
        print("This string is equal to 10 characters")