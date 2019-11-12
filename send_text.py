from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4f70b6d18acba9c2649825ee6826fd68"
# Your Auth Token from twilio.com/console
auth_token  = "dd1a248fb52dac0250d154cf8bacd76e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+48602206413",
    from_="+37123230835",
    body="Cześć, takie rzeczy można robić Pythonem")

print(message.sid)