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
    image_path = os.path.join(settings.MEDIA_ROOT, image_path)

    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            content_type = mimetypes.guess_type(image_path)
            if content_type is None:
                content_type = 'application/octet-stream'

            response = HttpResponse(image_file.read(), content_type=content_type)
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
            mobile = request.POST.get('mobile')
            whatsapp = request.POST.get('whatsapp')
            interest = request.POST.get('interest')
            achievement = request.POST.get('achievement')
            organization = request.POST.get('organization')
            improvement = request.POST.get('improvement')
            suggestion = request.POST.get('suggestion')
            uploaded_image = request.FILES['image']

            directory_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_image')
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            img_path = ""
            if uploaded_image:
                img_path = os.path.join(directory_path, uploaded_image.name)
                with open(img_path, 'wb') as img_file:
                    for chunk in uploaded_image.chunks():
                        img_file.write(chunk)
                
                render_base_url = os.environ.get('RENDER_BASE_URL')
                image_url = f'{render_base_url}/{img_path}'

            print({img_path, image_url, render_base_url})

            file_names = []

            if os.path.exists(directory_path) and os.path.isdir(directory_path):
                for filename in os.listdir(directory_path):
                    if os.path.isfile(os.path.join(directory_path, filename)):
                        file_names.append(filename)
            else:
                print(">> dir path not found or is not directory")

            for file_name in file_names:
                print(f"Files list in dir: {directory_path} - ", file_name)

            # image_url = '/media/uploaded_image/' + uploaded_image.name
            avmform = Avmform(name=name, fathername=fathername, batch=batch, passout=passout, presentaddress=presentaddress, permanentaddress=permanentaddress, occupation=occupation, workaddress=workaddress,
                              qualification=qualification, DOB=DOB, mobile=mobile, whatsapp=whatsapp, interest=interest, achievement=achievement, organization=organization, improvement=improvement, suggestion=suggestion, image_url=image_url)
            avmform.save()
            messages.success(request, "your form is successfully submitted.")
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

            return HttpResponse(error_message, status=500)
        return redirect("/")

    return render(request, 'avmform.html')
