from django.shortcuts import render,redirect

from avmjalore.models import Avmform
from django.contrib import messages

# Create your views here.
def index(request):
   
    return render(request, 'index.html')

def avmform(request):
   
    print('Invoked ----> avmform', request)
    if request.method == "POST":
        name = request.POST.get('name')
        fathername = request.POST.get('fathername')
        batch = request.POST.get('batch')
        passout = request.POST.get('passout')
        presentaddress =request.POST.get('presentaddress') 
        permanentaddress = request.POST.get('permanentaddress')
        occupation = request.POST.get('occupation')
        workaddress = request.POST.get('workaddress')
        qualification =request.POST.get('qualification') 
        DOB = request.POST.get('DOB')
        mobile = request.POST.get('mobile')
        whatsapp = request.POST.get('whatsapp')
        interest = request.POST.get('interest')
        achievement = request.POST.get('achievement')
        organization = request.POST.get('organization')
        improvement = request.POST.get('improvement')
        suggestion = request.POST.get('suggestion')
        image = request.POST.get('image')
        # WOB = request.POST.get('WOB')
       
        
        
        
        #  python me kisi data ko debugg aise karte h
        print(
            name, 
            fathername, 
            batch, 
            passout,
            presentaddress,
            permanentaddress,
            occupation,
            workaddress,
            qualification,
            DOB,
            # WOB, 
            mobile,
            whatsapp,
            interest,
            achievement,
            organization,
            improvement,
            suggestion,
            image
           
        )
        
        avmform = Avmform(name=name, fathername=fathername, batch=batch, passout=passout, presentaddress=presentaddress, permanentaddress=permanentaddress, occupation=occupation, workaddress=workaddress, qualification=qualification, DOB=DOB, mobile=mobile, whatsapp=whatsapp, interest=interest, achievement=achievement, organization=organization, improvement=improvement, suggestion=suggestion, image=image)
        # # # avmform = Avmform(name=name, fathername=fathername)
        avmform.save()
        messages.success(request, "your form is successfully submitted.")
        return redirect("/")
        
    
    return render(request,'avmform.html')