from twilio.rest import Client

#use twilio make an account.
sid='your_sid'
auth="your_auth"
a="your_twilio_number"
client=Client(sid,auth)

message =client.messages.create(
    from_=a,
    to='Receiver_number',
    body="Hello from Python!"
)

print(message.sid)