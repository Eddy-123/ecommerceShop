from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        #treat the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,
                                 password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/signup.html')