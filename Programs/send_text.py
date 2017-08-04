from twilio.rest import TwilioRestClient

# Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC7d50c922529f8e1535bc4c6031b6c70f"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = TwilioRestClient(account_sid,auth_token)

message = client.messages.create(
        to="+115005550003",
        from_="+18176011349",
        body="Test Message from Twiio - This is Ron Burgundy")
print(message.sid)

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
                           to="+15005550003",
                           from_="+15005550006")
print(call.sid)

