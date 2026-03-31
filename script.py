from curl_cffi import requests
import requests as sync_requests
import os

print(os.environ)
# Telegram credentials
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {
            'chat_id': CHAT_ID,
            'text': message
        }
        response = sync_requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            print(f"Telegram message sent: {message}")
        else:
            print(f"Failed to send Telegram message: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

def check_availability():
    date = '20260403'
    url = f"https://in.bookmyshow.com/movies/kolkata/project-hail-mary/buytickets/ET00481564/{date}"
    
    # Note: 'impersonate' does the magic of making your SSL handshake look like Chrome
    response = requests.get(url, impersonate="chrome110")
    
    if response.status_code == 200:
        print("Bypassed! Content length:", len(response.text))
    else:
        print(f"Still blocked: {response.status_code}")
        return f"Still blocked: {response.status_code}"
    
    
    if response.text.count(date) > 20:
        message = "Seats available!"
        print(message)
        return message
    else:
        message = "Date unavailable!"
        print(message)
        return message

if __name__ == "__main__":
    message = check_availability()
    send_telegram_message(message)



