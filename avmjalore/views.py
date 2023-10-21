from django.shortcuts import render,redirect
import os
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
        uploaded_image = request.FILES['image']
        # if uploaded_image:
        #     img_path = os.path.join('static', 'media', 'uploaded_image', uploaded_image.name)
        #     with open(img_path, 'wb') as img_file:
        #        for chunk in uploaded_image.chunks():
        #            img_file.write(chunk)
            
            # image_url = '/media/uploaded_image/' + uploaded_image.name
            # render_base_url = os.environ.get('RENDER_BASE_URL')
            # image_url = f'{render_base_url}/media/uploaded_image/{uploaded_image.name}'
        
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
            uploaded_image
          
            
           
        )
        
        avmform = Avmform(name=name, fathername=fathername, batch=batch, passout=passout, presentaddress=presentaddress, permanentaddress=permanentaddress, occupation=occupation, workaddress=workaddress, qualification=qualification, DOB=DOB, mobile=mobile, whatsapp=whatsapp, interest=interest, achievement=achievement, organization=organization, improvement=improvement, suggestion=suggestion, image_url=uploaded_image)
        # # # avmform = Avmform(name=name, fathername=fathername)
        avmform.save()
        messages.success(request, "your form is successfully submitted.")
        return redirect("/")
        
    
    return render(request,'avmform.html')
