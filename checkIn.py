import requests
from tkinter import messagebox

def is_instagram_down():
    urls = "https://www.instagram.com/"
    response = requests.get(urls)
    return response.status_code != 200

def is_facebook_down():
    urls = "https://www.facebook.com/"
    response = requests.get(urls)
    return response.status_code != 200

def is_whatsapp_down():
    urls = "https://web.whatsapp.com/"
    response = requests.get(urls)
    return response.status_code != 200

def is_twitter_down():
    urls = "https://twitter.com/"
    response = requests.get(urls)
    return response.status_code != 200

if __name__ == "__main__":
    if is_instagram_down():
        messagebox.showinfo("Info", "instagram is down!")
    else:
        messagebox.showinfo("Info","instagram is running!")

    if is_facebook_down():
        messagebox.showinfo("Info","facebook is down!")
    else:
        messagebox.showinfo("Info","facebook is running!")

    if is_whatsapp_down():
        messagebox.showinfo("Info","whatsapp is down!")
    else:
        messagebox.showinfo("Info","whatsapp is running!")
    if is_twitter_down():
        messagebox.showinfo("Info","Twitter is running!")
    else:
        messagebox.showinfo("Info","Twitter is down")
