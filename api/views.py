from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
import io
from api.models import BioData
from api.serializers import BioDataSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
   if request.method == "POST":
       registrationData = request.body
       stream = io.BytesIO(registrationData)
       parsed_data = JSONParser().parse(stream)

       username = parsed_data["username"] 
       password = parsed_data["password"] 
       email = parsed_data["email"] 
       hobby = parsed_data["hobby"] 
       phone =parsed_data["phone"] 

       myuser = User.objects.create_user(username,email,password)
       myuser.save()

       biodata  = BioData(email=email, hobby=hobby,phone=phone,user=myuser)
       biodata.save()

       msg= JSONRenderer().render({'msg':'Registration Successfull !'})
       return HttpResponse(msg,content_type='application/json')
   return HttpResponse("Something Went Wrong")

@csrf_exempt
def loginUser(request):
    if request.method == "POST":
         loginData = request.body
         stream = io.BytesIO(loginData)
         parsed_data = JSONParser().parse(stream)

         loginusername = parsed_data["username"] 
         loginpassword =  parsed_data["password"]
         user = authenticate(username=loginusername,password= loginpassword)
       
         if user is not None:
                login(request, user)    
                biodata = BioData.objects.get(user= user)
                serializer = BioDataSerializer(biodata)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data,content_type='application/json')
    json_data = JSONRenderer().render({"msg":"Incorrect Credentials"})        
    return HttpResponse(json_data,content_type='application/json')
    
    
@csrf_exempt
def logoutUser(request):
    if request.method == "POST":
      logout(request)
      return HttpResponse("successfully logged out") 
    
    return HttpResponse("successfully logged out ")    
          