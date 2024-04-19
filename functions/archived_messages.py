def messages(send_messages, sent_messages):
    while send_messages:
        current_message=send_messages.pop()
        print(f"Sending messages: {current_message}")
        sent_messages.append(current_message)
def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)

send_messages=['I will be soon', 'I will call back', 'Busy', 'Sleeping']
sent_messages=[]
messages(send_messages[:], sent_messages)
show_sent_messages(sent_messages)
print(send_messages)
print(sent_messages)