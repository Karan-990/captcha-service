from django.http import HttpResponse
from django.shortcuts import render
from .utils import generate_captcha
from .forms import CaptchaForm


def captcha_image(request):
    captcha_text, image = generate_captcha()
    request.session['captcha_text'] = captcha_text  # Store in session for verification
    return HttpResponse(image, content_type='image/png')

def index(request):
    form = CaptchaForm()
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            user_captcha = form.cleaned_data['captcha']
            if user_captcha == request.session.get('captcha_text'):
                return HttpResponse("CAPTCHA Verified Successfully!")
            else:
                return HttpResponse("CAPTCHA Verification Failed!")
    
    return render(request, 'index.html', {'form': form})