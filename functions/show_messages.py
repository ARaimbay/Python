def show_messages(short_messages):
    for short_message in short_messages:
        msg=f"{short_message}"
        print(msg)
message_list=['I will be soon', 'I will call back', 'Busy', 'Sleeping']
show_messages(message_list)