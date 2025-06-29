from twilio.rest import Client 

ACCOUNT_SID = "ACc52a964dda4ec617c60903ee11030410"
AUTH_TOKEN = "77030555be70236515384858bc607f7c"
FROM_PHONE = "+14094055045"
TO_PHONE = "+61432129128"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(body: str):
    message = client.messages.create(
        body=body,
        from_=FROM_PHONE,
        to=TO_PHONE
    )
    print("✅ SMS sent:", message.sid)
