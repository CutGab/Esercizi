messages = ["Ciao!", "Tutto bene?", "A domani!", "Sono occupato."]
sent_messages = [] 

def send_messages(messages: list):

    for i in range (len(messages)):
        sent_messages.append(messages[i])
        
        if len(sent_messages) == len(messages):
            break

    print(messages)
    print(sent_messages)
    return sent_messages

send_messages(messages)