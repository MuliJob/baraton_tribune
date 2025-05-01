"""Custom User Views"""
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import permissions

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from custom_user.forms import CreateUserForm, LoginForm


def get_tokens_for_user(user):
    """Helper function to create JWT tokens"""
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterAPIView(APIView):
    """API view for user registration"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Render the registration form"""
        form = CreateUserForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        """Handle user registration from form submission"""
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below!')
            return render(request, 'auth/register.html', {'form': form})


class LoginAPIView(APIView):
    """Login API view"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Render login form on GET request"""
        form = LoginForm()
        return render(request,
                      'auth/login.html',
                      {'form': form,
                       'request': request})

    def post(self, request):
        """Handle login form submission"""
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                tokens = get_tokens_for_user(user)
                request.session['access_token'] = tokens['access']
                request.session['refresh_token'] = tokens['refresh']

                messages.success(request, f"Logged in successfully. Welcome {user.email}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Login failed. Please correct the error below!")

        return render(request, 'auth/login.html', {'form': form, 'request': request})



class LogoutAPIView(APIView):
    """API view for user logout"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Handle logout via GET request (for template links)"""
        # Clear session tokens
        if 'access_token' in request.session:
            del request.session['access_token']
        if 'refresh_token' in request.session:
            del request.session['refresh_token']

        logout(request)

        messages.success(request, "Logged out successfully.")
        return redirect('login')

    def post(self, request):
        """Handle user logout"""
        try:
            refresh_token = request.data.get("refresh") or request.session.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            if 'access_token' in request.session:
                del request.session['access_token']
            if 'refresh_token' in request.session:
                del request.session['refresh_token']

            logout(request)

            messages.success(request, "Logged out successfully.")
            return redirect('login')
        except KeyError as e:
            messages.error(request, f"Session key error during logout: {e}")
            return redirect('home')
        except ValueError as e:
            messages.error(request, f"Token processing error during logout: {e}")
            return redirect('home')
