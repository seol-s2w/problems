class ChatRoom:
    def __init__(self):
        self.messages = []
        self.id_to_name = {}

    def add_message(self, message):
        if message.startswith("Enter"):
            action, id, name = message.split()
            self.messages.append((action, id))
            self.id_to_name[id] = name
        elif message.startswith("Leave"):
            action, id = message.split()
            self.messages.append((action, id))
        else:
            action, id, name = message.split()
            self.id_to_name[id] = name

    def get_messages(self):
        messages = []
        for action, id in self.messages:
            if action == "Enter":
                messages.append(f"{self.id_to_name[id]}님이 들어왔습니다.")
            else:
                messages.append(f"{self.id_to_name[id]}님이 나갔습니다.")
        return messages


def solution(record):
    chatroom = ChatRoom()
    for r in record:
        chatroom.add_message(r)
    answer = chatroom.get_messages()

    return answer
