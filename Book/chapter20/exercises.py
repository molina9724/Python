import ezgmail
from ezgmail import GmailMessage, GmailThread

# ezgmail.send(
#     recipient="molina9724@gmail.com",
#     subject="Email sent from Python!",
#     body="You did it, you son of a bitch!",
# )
# print(ezgmail.EMAIL_ADDRESS)
unread_threads: list[GmailThread] = ezgmail.unread(maxResults=1000)
# print(ezgmail.summary(unread_threads))

# print(len(unread_threads))
# print(unread_threads[0])

# print(len(unread_threads[0].messages))
# print(unread_threads[0].messages[0])
# print(unread_threads[0].messages[0].subject)
# print(unread_threads[0].messages[0].body)
# print(unread_threads[0].messages[0].timestamp)
# print(unread_threads[0].messages[0].sender)
# print(unread_threads[0].messages[0].recipient)


recent_threads: list[GmailThread] = ezgmail.recent()
print(len(recent_threads))

first_thread: GmailThread = unread_threads[0]
print(f"{first_thread=}")
first_message: GmailMessage = first_thread.messages[0]
print(first_message.subject)
print(first_message.body)
print(first_message.timestamp)
print(first_message.sender)
print(first_message.recipient)

results_threads = ezgmail.search("Security Alert label:UNREAD", 200)
print(len(results_threads))

has_attch = ezgmail.search("subject:Carlos label:UNREAD")
print(len(has_attch))
# A space is interpreted as AND


# ezgmail.send(
#     "antigravityhack25@gmail.com",
#     "email with attachment",
#     "Check the attachment",
#     "/Users/daniel_molina/Downloads/Python/Python/json_to_csv.csv",
# )

msg_with_attch: GmailMessage = None  # type: ignore

# for thread in unread_threads:
#     for message in thread.messages:
#         if message.attachments:
#             print(message.subject)
#             msg_with_attch = message

# print(msg_with_attch.attachments)
# msg_with_attch.downloadAttachment(
#     filename="json_to_csv.csv",
#     downloadFolder="/Users/daniel_molina/Downloads/",
# )
# msg_with_attch.downloadAllAttachments(
#     downloadFolder="/Users/daniel_molina/Downloads/", overwrite=True
# )

# security_alert_search_threads: list[GmailThread] = ezgmail.search("Security alert")
# for thread in security_alert_search_threads:
#     thread.trash()

ezgmail.send(
    "3162952730@comcel.com.co",
    "Hello from hell",
    "This is you!",
)

import requests

# requests.post(
#     "https://ntfy.sh/my_notificatiobs",
#     "I did it, you son of a bitch",
#     headers={
#         "Title": "Important!",
#         "Tags": "warning,neutral_face",
#         "Priority": "5",
#     },
# )

resp = requests.get("https://ntfy.sh/my_notificatiobs/json?poll=1&since=10m")
resp = requests.get("https://ntfy.sh/my_notificatiobs/json?poll=1")
print(resp.text)

import json

notifications = list()
for json_text in resp.text.splitlines():
    notifications.append(json.loads(json_text))
    print("--------------------")
    print(json_text)


print(notifications[0]["id"])
print(notifications[0]["time"])
print(notifications[0]["expires"])
print(notifications[0]["message"])
print(notifications[0]["title"])
print(notifications[0]["topic"])

print(resp.text.splitlines())
print(type(resp.text))
print(type(resp.text.splitlines()))

print(notifications)
