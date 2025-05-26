messages = ["Ciao!", "Tutto bene?", "A domani!", "Sono occupato."]
sent_messages = [] 

def send_messages(messages: list):

    while messages:
        sent_messages.append(messages[0])
        messages.pop(0)

    print(messages)
    print(sent_messages)
    return sent_messages

send_messages(messages)