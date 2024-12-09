# from base64 import b64encode
# from datetime import datetime

# #from utils import current_time_stamp, getPassword, access_token_mpesa, save_stkpush_request  # Assuming these are defined elsewhere
# import requests
# from django.conf import settings
# from pesaapp.models import mpesaRequest
# from django.http import HttpResponse
# from django_daraja.mpesa.core import MpesaClient


# """
# ADVICE: put the variables in this class into an envrioment variable
# """
# class STKPUSHSECRET:
#     passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
#     business_short_code = 174379
#     consumer_key = "NwfSxvbZUO4UaDlJTcABKGlgiThShkbrdmezuWmda1qzRV99"
#     consumer_secret = "3Z2e7YvWRqHjmkHRxVCzogUm2hd0e8e0B5YrnoioyHKLt3G58BelnGcx8v6E6JnG"
#     onlinePayment_URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     auth_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
#     callback_url = "https://a5ab-197-136-183-22.ngrok-free.app/api/v1/stk-callback/"



# STKPUSHSECRET = STKPUSHSECRET()


# def access_token_mpesa(consumer_key, consumer_secret):
#     credentials = f"{consumer_key}:{consumer_secret}"
#     encoded_credentials = b64encode(credentials.encode('utf-8')).decode('utf-8')
#     headers = {'Authorization': f"Basic {encoded_credentials}",'Content-Type': 'application/json'}
#     r = requests.get(STKPUSHSECRET.auth_URL, headers=headers)
#     json_response = r.json()
#     access_token = json_response.get("access_token")
#     return access_token


# def current_time_stamp():
#     unformatted_time = datetime.now()
#     formatetted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#     return formatetted_time


# def getTime(unformatted_time):
#     transation_time = str(unformatted_time)
#     transation_date_time = datetime.strptime(transation_time, "%Y%m%d%H%M%S")
#     return transation_date_time


# def getPassword(business_short_code, passkey, timestamp):
#     data = f"{business_short_code}{passkey}{timestamp}"
#     encoded_string = b64encode(data.encode())
#     return encoded_string.decode("utf-8")



# # https://github.com/safaricom/mpesa-php-sdk/issues/51

# # def request_stk_push(amount,phone_number,account_reference="Zeddy Pay",transaction_description="",user=1):
# #     timestamp = current_time_stamp()
# #     password = getPassword(STKPUSHSECRET.business_short_code, STKPUSHSECRET.passkey, timestamp)
# #     access_token = access_token_mpesa(STKPUSHSECRET.consumer_key, STKPUSHSECRET.consumer_secret)
# #     headers = {"Authorization": "Bearer %s" % access_token}
# #     request = {
# #         "BusinessShortCode": "174379",
# #         "Password": "Safaricom999!*!",
# #         "Timestamp": "20241209083220",
# #         "TransactionType": "CustomerPayBillOnline", #"CustomerBuyGoodsOnline",
# #         "Amount": "1",
# #         "PartyA": "254742957112",
# #         "PartyB": "174379",
# #         "PhoneNumber": "254742957112",
# #         "CallBackURL":  "https://a5ab-197-136-183-22.ngrok-free.app",
# #         "AccountReference": "Zeddy Pay Inc.",
# #         "TransactionReference": account_reference,
# #         "TransactionDesc": transaction_description,
# #     }
# #     response = requests.post(STKPUSHSECRET.onlinePayment_URL, json=request, headers=headers)
# #     response_data = response.json()
# #     if "errorCode" in response_data.keys():
# #         print(f"Error At the MPESA CODE  {response_data}")
# #         return response_data
# #     else:
# #         save_stkpush_request(response_data, phone_number, account_reference, transaction_description )
# #         return response_data





# def request_stk_push(amount, phone_number, account_reference="Zeddy Pay", transaction_description="", user=1):
#     # Generate dynamic timestamp
#     timestamp = current_time_stamp()  # Assuming this returns the correct format: YYYYMMDDHHMMSS
    
#     # Generate password dynamically
#     password = getPassword(STKPUSHSECRET.business_short_code, STKPUSHSECRET.passkey, timestamp)
    
#     # Get access token
#     access_token = access_token_mpesa(STKPUSHSECRET.consumer_key, STKPUSHSECRET.consumer_secret)
    
#     headers = {"Authorization": f"Bearer {access_token}"}
    
#     # Construct the request payload
#     request_payload = {
#         "BusinessShortCode": "174379",  # Use your configured business short code
#         "Password": password,
#         "Timestamp": timestamp,
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": "1",
#         "PartyA": "254742957112",
#         "PartyB": "174379",
#         "PhoneNumber":  "254742957112",
#         "CallBackURL": "https://a5ab-197-136-183-22.ngrok-free.app",  # Make sure this URL is correct and active
#         "AccountReference": "account_reference",
#         "TransactionDesc": "transaction_description",
#     }

#     try:
#         # Send the STK Push request
#         response = requests.post(STKPUSHSECRET.onlinePayment_URL, json=request_payload, headers=headers)
#         response_data = response.json()
        
#         # Check for errors in the response
#         if "errorCode" in response_data:
#             print(f"Error At the MPESA CODE: {response_data}")
#             return response_data
#         else:
#             # Save the request to your database or logs
#             save_stkpush_request(response_data, phone_number, account_reference, transaction_description)
#             return response_data
    
#     except requests.exceptions.RequestException as e:
#         print(f"Network Error: {e}")
#         return {"error": str(e)}





# # def request_stk_push(request):
# #     cl = MpesaClient()
# #     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
# #     phone_number = '0742957112'
# #     amount = 1
# #     account_reference = 'reference'
# #     transaction_desc = 'Description'
# #     callback_url = "https://a5ab-197-136-183-22.ngrok-free.app/api/v1/stk-callback/";
# #     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
# #     return HttpResponse(response)

# # def stk_push_callback(request):
# #         data = request.body
        
# #         return HttpResponse("STK Push in Django👋")

# def save_stkpush_request(response_data, phone_number, account_reference, transaction_description):
#     if "errorCode" in response_data.keys():
#         print(f"we have received an error here    {response_data}")
#         return response_data
#     else:
#         data = {}
#         data["merchant_id"] = response_data["MerchantRequestID"]
#         data["checkout_id"] = response_data["CheckoutRequestID"]
#         data["res_code"] = response_data["ResponseCode"]
#         data["res_text"] = response_data["ResponseDescription"]
#         data["msg"] = response_data["CustomerMessage"]
#         data["phone"] = phone_number
#         data["ref"] = account_reference
#         data["trans_date"] = transaction_description

#         push_request_res = mpesaRequest.objects.create(**data)
#         push_request_res.save()
#         return response_data



import requests
from datetime import datetime
from django.http import HttpResponse
from django.conf import settings

# def current_time_stamp():
#     return datetime.now().strftime('%Y%m%d%H%M%S')

# pesaapp/mpesa.py
def getTime():
    from datetime import datetime
    return datetime.now().strftime('%Y%m%d%H%M%S')


def getPassword(shortcode, passkey, timestamp):
    import base64
    data = f"{shortcode}{passkey}{timestamp}"
    return base64.b64encode(data.encode()).decode('utf-8')

def access_token_mpesa(consumer_key, consumer_secret):
    token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(token_url, auth=(consumer_key, consumer_secret))
    response_data = response.json()
    return response_data.get('access_token')

def request_stk_push(amount, phone_number, account_reference="Zeddy Pay", transaction_description="", user=1):
    timestamp = current_time_stamp()
    password = getPassword(settings.STKPUSHSECRET['business_short_code'], settings.STKPUSHSECRET['passkey'], timestamp)
    access_token = access_token_mpesa(settings.STKPUSHSECRET['consumer_key'], settings.STKPUSHSECRET['consumer_secret'])
    
    headers = {"Authorization": f"Bearer {access_token}"}
    
    request_payload = {
         "BusinessShortCode": "174379",  # Use your configured business short code
        #  "Password": password,
        #  "Timestamp": timestamp,
         "TransactionType": "CustomerPayBillOnline",
         "Amount": "1",
         "PartyA": "254742957112",
         "PartyB": "174379",
         "PhoneNumber":  "254742957112",
         "CallBackURL": "https://a5ab-197-136-183-22.ngrok-free.app",   #Make sure this URL is correct and active
         "AccountReference": "account_reference",
         "TransactionDesc": "transaction_description",
     }


    response = requests.post(settings.STKPUSHSECRET['onlinePayment_URL'], json=request_payload, headers=headers)
    return response.json()
def stk_push_callback(request):
    data = request.body
        
    return HttpResponse("STK Push in Django👋")

