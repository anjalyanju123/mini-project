from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,update_session_auth_hash
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Profile(request):
    try:
        # Get the profile of the logged-in user
        profile = ProfileModel.objects.get(user=request.user)
    except ProfileModel.DoesNotExist:
        profile = None

    return render(request, 'profile.html', {'profile': profile})

def homepage(request):
    return render(request,'home.html')

def authregister(request):
    if request.method == 'POST':
        rform = ProfileForm(request.POST, request.FILES)  # Handle file uploads

        if rform.is_valid():
            # Extract the form data
            e = request.POST['email']
            p = request.POST['password']
            rp = request.POST['re-password']

            # These are the profile-specific fields
            fn = rform.cleaned_data['first_name']
            ln = rform.cleaned_data['last_name']
            ad = rform.cleaned_data['address']
            ph = rform.cleaned_data['phone']
            ag = rform.cleaned_data['age']
            up = rform.cleaned_data['upload']

            if p == rp:
                if User.objects.filter(email=e).exists():
                    messages.error(request, 'Email already exists.')
                else:
                    # Create the User object
                    user = User.objects.create_user(username=e, email=e, password=p)
                    user.save()

                    # Create the Profile2Model instance and link it to the user
                    profile1 = ProfileModel(
                        first_name=fn, last_name=ln, address=ad, phone=ph, age=ag, upload=up, user=user
                    )
                    profile1.save()

                    messages.success(request, 'Registration completed successfully.')
                    return redirect('/authlogin')
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Form is invalid, please correct the errors.')

    else:
        rform = ProfileForm()

    return render(request, 'register.html')

def authlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Complete')
            return redirect('/Profile') 
        else:
            messages.error(request, 'Invalid Login')
    return render(request, 'login.html')  

@login_required
def authlogout(request):
    logout(request) 
    return redirect('/') 

@login_required(login_url='/authlogin/')
def book_list(request):
    book = Book.objects.all()
    paginator = Paginator(book, 6)  # Show 6 books per page
    
    # Get the page number from the query string
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,'Booklist.html',{'page':page})

@login_required(login_url='/authlogin/')
def reset_password(request, user_id):
    user = User.objects.get(id=user_id)  # Fetch the user by their ID

    if request.method == 'POST':
        # Ensure that the user is changing their own password
        if request.user != user:
            return redirect('some_error_page')  # Add error handling as needed

        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  # Save the new password
            update_session_auth_hash(request, user)  # Prevent user from being logged out after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Profile')  # Redirect to profile page or wherever you want after password reset
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'reset_password.html', {'form': form})


@login_required
def Edit_profile(request):
    # Get the current user's profile
    profile = ProfileModel.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('/Profile')  # Redirect to the profile page
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'Edit_profile.html', {'form': form})
