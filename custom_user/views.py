"""Custom User Views"""
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

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
            user.set_password(password)  # Hash the password
            user.save()

            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
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
            username = form.cleaned_data.get('username')  # ✅ Safe now
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Generate tokens
                tokens = get_tokens_for_user(user)
                request.session['access_token'] = tokens['access']
                request.session['refresh_token'] = tokens['refresh']

                print(f"Access Token: {tokens['access']}")
                print(f"Refresh Token: {tokens['refresh']}")
                messages.success(request, f"Logged in successfully. Welcome {user.email}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")  # fallback
        else:
            # 🔥 ADD better debugging here
            error_list = [f"{field}: {error}" for field, errors in form.errors.items() for error in errors]
            error_message = " | ".join(error_list)
            messages.error(request, f"Login failed. Details: {error_message}")

        return render(request, 'auth/login.html', {'form': form, 'request': request})



class LogoutAPIView(APIView):
    """API view for user logout"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Handle user logout"""
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token is required."},
                                status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            # Also logout the user
            logout(request)

            return Response({"message": "Logout successful."},
                            status=status.HTTP_205_RESET_CONTENT)
        except KeyError as e:
            return Response({"error": f"Missing or invalid refresh token. {e}"},
                            status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({"error": f"Invalid token. {e}"}, status=status.HTTP_400_BAD_REQUEST)
