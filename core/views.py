from social_media.models import Image, SocialPost, SocialComment
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from social_media.forms import SocialPostForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logged_in_user=request.user
        posts = SocialPost.objects.all().order_by('-created_on')
        form = SocialPostForm()
        
        context = {
            'posts': posts,
            'form':form

        }
        return render(request, 'pages/index.html', context)
    
    
    def post(self, request, *args, **kwargs):
        logged_in_user=request.user

        posts = SocialPost.objects.all()

        form = SocialPostForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = logged_in_user
            new_post.save()

            for f in files:
                img = Image(image=f)
                img.save()
                new_post.image.add(img)

            new_post.save()

        context={
            'posts':posts,
            'form':form
        }
        return render(request, 'pages/index.html', context)
    

#Email confirmation




def send_email(request, View):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = {'email': email}

        subject = 'Email Confirmation'
        

        content = 'Hi, thanks for joining us!'

        message = EmailMultiAlternatives(subject, content, settings.EMAIL_HOST_USER, email)
        html_content = template.render({'user': user})

        message.attach_alternative(html_content, 'text/html')
        message.send()

        
        redirect_url = request.POST.get('redirect_url', 'account/email_confirm.html')
        return HttpResponseRedirect(redirect_url)

    
    return render(request, 'account/signup.html')
