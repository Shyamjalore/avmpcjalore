from django.shortcuts import render, redirect
import os
from avmjalore.models import Avmform
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
import mimetypes

def index(request):
    return render(request, 'index.html')

def image(request, image_path):
    print("Getting imagepath:", image_path)
    image_path = os.path.join(settings.MEDIA_ROOT, image_path)

    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            content_type = mimetypes.guess_type(image_path)
            if content_type is None:
                content_type = 'application/octet-stream'

            response = HttpResponse(image_file.read(), content_type=content_type[0])
            return response

    return HttpResponse("Image not found", status=404)

def avmform(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            fathername = request.POST.get('fathername')
            batch = request.POST.get('batch')
            passout = request.POST.get('passout')
            presentaddress = request.POST.get('presentaddress')
            permanentaddress = request.POST.get('permanentaddress')
            occupation = request.POST.get('occupation')
            workaddress = request.POST.get('workaddress')
            qualification = request.POST.get('qualification')
            DOB = request.POST.get('DOB')
            DOW = request.POST.get('DOW')
            mobile = request.POST.get('mobile')
            whatsapp = request.POST.get('whatsapp')
            interest = request.POST.get('interest')
            achievement = request.POST.get('achievement')
            organization = request.POST.get('organization')
            improvement = request.POST.get('improvement')
            suggestion = request.POST.get('suggestion')
            image = request.FILES['image']

            if DOW == "":
                DOW = None

            print("DOW:",DOW)

            directory_path = os.path.join(settings.MEDIA_ROOT)
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            img_path = ""
            if image:
                img_path = os.path.join(directory_path, image.name)
                with open(img_path, 'wb') as img_file:
                    for chunk in image.chunks():
                        img_file.write(chunk)
                
            image_url = f'{request.get_host()}/images/{image.name}'

            avmform = Avmform(name=name, fathername=fathername, batch=batch, passout=passout, presentaddress=presentaddress, permanentaddress=permanentaddress, occupation=occupation, workaddress=workaddress,
                              qualification=qualification, DOB=DOB, DOW=DOW, mobile=mobile, whatsapp=whatsapp, interest=interest, achievement=achievement, organization=organization, improvement=improvement, suggestion=suggestion, image_url=image_url)
            avmform.save()
            messages.success(request, "your form is successfully submitted.")
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

            return HttpResponse(error_message, status=500)
        return redirect("/")

    return render(request, 'avmform.html')
