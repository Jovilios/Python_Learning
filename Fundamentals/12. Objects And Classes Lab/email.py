class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def fet_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []

command = input()

while command != "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

send_emails = [int(x) for x in input().split(", ")]

for index, email in enumerate(emails):
    if index in send_emails:
        emails[index].send()
    print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_send}")




