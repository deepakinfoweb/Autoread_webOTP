from django.shortcuts import redirect, render
# import library
import math
import random
import requests
from twilio.rest import Client
import json

# Create your views here.


def home(request):
    return render(request, 'home.html')


def send_otp(request):
    output_json = {}
    if request.method == "POST":
        input_json = request.POST.dict()
    else:
        input_json = request.GET.dict()
    try:
      # Your OTP is: 123456.
      # @web-otp.glitch.me #12345
        digits = "0123456789"
        OTP = ""
        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]
        account_sid = "AC008c71e4047a771bf56300f7b5589717"
        auth_token = "28b767becc063ad038950b4b0ee6f654"
        client = Client(account_sid, auth_token)
        msg = str(OTP)+" is your OTP code. Do not share the OTP with anyone. @https://392b-2405-201-6801-4d-d187-9d94-daa9-9675.ngrok.io #"+str(OTP)
        print("msg ::: "+msg)
        message = client.messages.create(to="+91"+str(input_json.get('number')), from_="+17735709301", body=msg)
        print(message)
        return render(request, 'otp.html')
    except Exception as ex:
        return redirect('home')


def index(request):
    return render(request, 'index.html')
