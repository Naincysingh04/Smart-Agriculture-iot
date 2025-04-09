import requests 

def send_notification(message):
    print("Sending Notification:", message)
    # Example: Twilio / Firebase or a webhook
    payload = {"title": "Smart Irrigation Alert", "message": message}
    requests.post("https://your-notify-api.com/send", json=payload)
