messages: list = ["Ciao!", "Tutto bene?", "A domani!", "Sono occupato."]

def show_messages (messages: list):

    for i in messages:
        print(i)

    return messages


show_messages(messages)