from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import MpesaPayments, mpesaRequest
from django.contrib.auth.models import User


from django.shortcuts import render
from django.http import Http404

from pesaapp.serializers import mpesaRequestSerializer, MpesaPaymentsSerializer
from pesaapp.models import mpesaRequest, MpesaPayments
from pesaapp.mpesa import request_stk_push, getTime
import json


# create user with id 1 as default if it is not there
try:
    if not User.objects.filter(id=1).exists():
        # Create the sample user
        user = User.objects.create_user(
            username='Martoh',
            password='Martoh',
            email='martinkagema01@gmail.com.com'
        )
        user.first_name = "Martoh"
        user.last_name = "Martoh"
        user.is_active = True
        user.save()
        print("Default user created")
    else:
        print("Default user already exists")
except Exception as e:  
    print(e)


class DefaultHomeView(APIView):
    def get(self, request):
        response_obj = {
            "message": "Welcome to mympesa API. Please check out the documentation at https://developer.safaricom.co.ke/",
            "stk-push": "Send STK push request to this endpoint: /api/v1/pesapap/pay/",
            "payment view": "Send payment request to this endpoint: /api/v1/pesapap/payments/"
        }
        return Response(response_obj, status=status.HTTP_200_OK)





class PaymentView(APIView):
    def post(self, request):
        print(request.data)
        print("Requested STK PUSH FROM WEB.......")

        USER_ID = 1

        user = User.objects.get(id=USER_ID)

        amount = 1 
        phone_number = request.data.get("phone")
        if not phone_number:
            return Response({
                "status": "error",
                "message": "Phone number is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        transaction_description = request.data.get("description", "payment")
        print(f"Phone Number: {phone_number}")
        print(f"Request is being sent to STK push... user {USER_ID}, phone {phone_number}")

        # (amount,phone_number,account_reference="Zeddy Pay",transaction_description="",user=1)
        ret_val = request_stk_push(
            float(amount),phone_number, 
            account_reference=str(USER_ID),
            transaction_description=transaction_description, user=USER_ID
        )
        if "errorMessage" in ret_val:
            return Response({
                "status": "error",
                "message": f"Hi {user.username}, your payment did not go through. Error: {ret_val['errorMessage']}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "status": "success",
                "message": f"Hi {user.username}, your payment is initiated. Please input your M-Pesa PIN from the STK request on your phone."
            }, status=status.HTTP_200_OK)



class StkCallbackView(APIView):
    def post(self, request):
        print("Mpesa callback has been called")
        
        # Try to load the JSON data from the body of the request
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"message": "error", "error": "Invalid JSON format"}, status=400)
        
        print(f"DATA is {data}")
        data_res = {}

        # Extract necessary information from the callback response
        data_res["merchant_id"] = data["Body"]["stkCallback"]["MerchantRequestID"]
        data_res["checkout_id"] = data["Body"]["stkCallback"]["CheckoutRequestID"]
        data_res["res_code"] = data["Body"]["stkCallback"]["ResultCode"]
        data_res["res_text"] = data["Body"]["stkCallback"]["ResultDesc"]

        # If ResultCode is greater than 0, we consider the payment failed
        if int(data_res["res_code"]) > 0:
            return JsonResponse(data, status=417)

        else:
            items = data["Body"]["stkCallback"]["CallbackMetadata"]["Item"]
            for item in items:
                data_res[item.get("Name")] = item.get("Value")

            data_res["trans_date"] = getTime(data_res["TransactionDate"])

            MerchantRequestID = data_res["merchant_id"]
            CheckoutRequestID = data_res["checkout_id"]
            try:
                request_stk_push_res = mpesaRequest.objects.get(
                    merchant_id=MerchantRequestID,
                    checkout_id=CheckoutRequestID,
                )
            except mpesaRequest.DoesNotExist:
                raise Http404("Order not found")

            user_id = 1 
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise Http404("User not found")

            payment = MpesaPayments()

            print(f"Data is {data}")

            payment.user = user
            payment.receipt = data_res.get("MpesaReceiptNumber")
            payment.merchant_id = data_res.get("merchant_id")
            payment.checkout_id = data_res.get("checkout_id")
            payment.res_code = data_res.get("res_code")
            payment.res_text = data_res.get("res_text")
            payment.amount = data_res.get("Amount")
            payment.phone = data_res.get("PhoneNumber")
            payment.trans_date = request_stk_push_res.trans_date

            payment.save()

            return JsonResponse({"desc": "success"}, status=200)


class ViewMpesaRequests(APIView):
    def get(self, request):
        try:
            request_res = mpesaRequest.objects.all()
            serial_obj = mpesaRequestSerializer(request_res, many=True)
        except mpesaRequest.DoesNotExist:
            raise Http404("Order not found")
        return Response(serial_obj.data, status=200)
    

class ViewMpesaPayments(APIView):
    def get(self, request):
        try:
            # 
            payment_res = MpesaPayments.objects.all() 
            serial_obj = MpesaPaymentsSerializer(payment_res, many=True)
        except MpesaPayments.DoesNotExist:
            raise Http404("Order not found")
        return Response(serial_obj.data, status=200)
    


# simulate the process via web page
# def payvia_webapp(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone')
#         amount = request.POST.get('amount', 1)
#         description = request.POST.get('description', "hi there")

#         USER_ID = 1
#         user = User.objects.get(id=USER_ID)
#         #call the stk        
#         # 
#         ret_val = request_stk_push(
#             float(amount),
#             phone_number, 
#             account_reference=str(USER_ID),
#             transaction_description=str(description), user=USER_ID
#         )
#         if "errorMessage" in ret_val:
#             return JsonResponse({
#                 "status": "error",
#                 "message": f"Hi {user.username}, your payment did not go through. Error: {ret_val['errorMessage']}"
#             }, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return JsonResponse({
#                 "status": "success",
#                 "message": f"Hi {user.username}, your payment is initiated. Please input your M-Pesa PIN from the STK request on your phone."
#             }, status=status.HTTP_200_OK)

#     return render(request, 'form.html')




def payvia_webapp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount', 1)
        description = request.POST.get('description', "Payment Description")

        USER_ID = 1  # Replace with dynamic user retrieval if needed
        user = User.objects.get(id=USER_ID)

        # Initiate STK push
        ret_val = request_stk_push(
            float(amount),
            phone_number,
            account_reference=str(USER_ID),
            transaction_description=description,
            user=USER_ID
        )

        if "errorMessage" in ret_val:
            return JsonResponse({
                "status": "error",
                "message": f"Hi {user.username}, your payment did not go through. Error: {ret_val['errorMessage']}"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({
                "status": "success",
                "message": f"Hi {user.username}, your payment is initiated. Please input your M-Pesa PIN from the STK request on your phone."
            }, status=status.HTTP_200_OK)

    return render(request, 'form.html')

def stk_callback(request):
    if request.method == 'POST':
        print(request.body)  # Log the callback data
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Success"})
    
def form(request):
    return render(request, 'form.html')


# """
# CRUD:
#     - C = Create --> MpesaPayments,objects.create({
#         "user": 1,
#         "amount": 1,
#         "receipt": 1,
#         "merchant_id": 1,
#         })

#     - R = Read --> MpesaPayments.objects.all() --get all values in the table
#                --> MpesaPayments.objects.get(pk=1) --get a single value
#                --> MpesaPayments.objects.filter(pk=1) --get a value which has same value as filter

#     - U = Update --> MpesaPayments.objects.filter(pk=1).update({})

#     - D = Delete  --> MpesaPayments.objects.filter(pk=1).delete() #for specifig
#                   --> MpesaPayments.objects.all().delete() #for all
#                   --> MpesaPayments.objects.get(description__icontains="test").delete() #for specific which has same value
# """