# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Counsellor, Student


# # Create your views here.
# def index(request): 
#     return render(request, 'index.html')

# @login_required
# def student_dashboard(request):
#     if not request.user.groups.filter(name='Students').exists():
#         return redirect('login')
#     student = Student.objects.get(email=request.user.email)
#     return render(request, 'student_dashboard.html', {'student': student})

# @login_required
# def counsellor_dashboard(request):
#     if not request.user.groups.filter(name='Counsellors').exists():
#         return redirect('login')
#     counsellor = Counsellor.objects.get(email=request.user.email)
#     return render (request, 'counsellor_dashboard.html', {'counsellor': counsellor})

# def loginUser(request):
#     return render(request, 'login_page.html')

# def doLogin(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if not (email and password):
#             messages.error(request, "Please provide both email and password!")
#             return render(request, 'login_page.html')

#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             if hasattr(user, 'student'):
#                 return redirect('student_dashboard')
#             elif hasattr(user, 'counsellor'):
#                 return redirect('counsellor_dashboard')
#             else:
#                 messages.error(request, 'Invalid user type!')
#                 return render(request, 'login_page.html')
#         else:
#             messages.error(request, 'Invalid login credentials!')
#             return render(request, 'login_page.html')

#     else:
#         return render(request, 'login_page.html')



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, Counsellor
from django.contrib.auth import logout
from .forms import CustomStudentPasswordChangeForm, CustomCounsellorPasswordChangeForm, StudentProfileForm, CounsellorProfileForm
from django.contrib.auth import update_session_auth_hash


def index(request): 
    return render(request, 'index.html') 

@login_required
def student_dashboard(request):
    if not request.user.groups.filter(name='Students').exists():
        return redirect('login')
    student = Student.objects.get(email=request.user.email)
    return render(request, 'student_dashboard.html', {'student': student})

@login_required
def counsellor_dashboard(request):
    if not request.user.groups.filter(name='Counsellors').exists():
        return redirect('login')
    counsellor = Counsellor.objects.get(email=request.user.email)
    return render(request, 'counsellor_dashboard.html', {'counsellor': counsellor,})

def loginUser(request):
    return render(request, 'login_page.html')

def doLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (email and password):
            messages.error(request, "Please provide both email and password!")
            return render(request, 'login_page.html')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if hasattr(user, 'student'):
                return redirect('student_dashboard')
            elif hasattr(user, 'counsellor'):
                return redirect('counsellor_dashboard')
            else:
                messages.error(request, 'Invalid user type!')
                return render(request, 'login_page.html')
        else:
            messages.error(request, 'Invalid login credentials!')
            return render(request, 'login_page.html')

    else:
        return render(request, 'login_page.html')
    
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')


@login_required
def change_student_password(request):
    if request.method == 'POST':
        form = CustomStudentPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important, to update the session with the new password
            messages.success(request, 'Your password was successfully updated!')
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomStudentPasswordChangeForm(request.user)
    return render(request, 'registration/change_student_password.html', {
        'form': form
    })

@login_required
def change_counsellor_password(request):
    if request.method == 'POST':
        form = CustomCounsellorPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important, to update the session with the new password
            messages.success(request, 'Your password was successfully updated!')
            return redirect('counsellor_dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomCounsellorPasswordChangeForm(request.user)
    return render(request, 'registration/change_counsellor_password.html', {
        'form': form
    })

def profile_view(request):
    Student = request.user.student  # Assuming there is a one-to-one relationship with the user
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=Student)
        if form.is_valid():
            form.save()
            # Redirect or add a success message
            return redirect('student_profile')
    else:
        form = StudentProfileForm(instance=Student)

    return render(request, 'student_profile.html', {'form': form})

def counsellor_profile_view(request):
    Counsellor = request.user.counsellor  # Assuming there is a one-to-one relationship with the user
    if request.method == 'POST':
        form = CounsellorProfileForm(request.POST, instance=Counsellor)
        if form.is_valid():
            form.save()
            # Redirect or add a success message
            return redirect('counsellor_profile')
    else:
        form = CounsellorProfileForm(instance=Counsellor)

    return render(request, 'counsellor_profile.html', {'form': form})


def student_dashboard(request):
    # Example context data
    context = {
        'counselors': [
            {'name': 'Dr. John Doe', 'available': True},
            {'name': 'Dr. Jane Smith', 'available': False},
        ],
        'messages': [
            {'sender': 'Dr. John Doe', 'unread_count': 1},
            {'sender': 'Dr. Jane Smith', 'unread_count': 0},
        ],
        'resources': [
            {'title': 'Resource 1', 'description': 'Description 1', 'image_url': 'https://via.placeholder.com/150'},
            {'title': 'Resource 2', 'description': 'Description 2', 'image_url': 'https://via.placeholder.com/150'},
        ]
    }
    return render(request, 'student_dashboard.html', context)

def counselor_dashboard(request):
    # Example context data
    context = {
        'appointments': [
            {'student_name': 'John Doe', 'date': '2024-06-21', 'time': '10:00 AM'},
            {'student_name': 'Jane Smith', 'date': '2024-06-22', 'time': '02:00 PM'},
        ],
        'messages': [
            {'student_name': 'John Doe', 'unread_count': 1},
            {'student_name': 'Jane Smith', 'unread_count': 0},
        ],
        'resources': [
            {'title': 'Resource 1', 'description': 'Description 1', 'image_url': 'https://via.placeholder.com/150'},
            {'title': 'Resource 2', 'description': 'Description 2', 'image_url': 'https://via.placeholder.com/150'},
        ]
    }
    return render(request, 'counselor_dashboard.html', context)