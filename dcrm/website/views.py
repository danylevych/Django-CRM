from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpUserForm, AddRecordForm
from .models import Record


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Wow you've been logged in!")
        else:
            messages.success(request, "There was an error login in, please try again")
        return redirect('home')

    records = Record.objects.all()

    return render(request, 'home.html', {'records' : records})


def logout_user(request):
    logout(request)
    messages.success(request, "You heve been logged out...")
    return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SingUpUserForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, "Wow you've been logged in!")
				return redirect('home')
			else:
				messages.success(request, "Try to fill all fields by correct values!")
	else:
		form = SingUpUserForm()

	return render(request, 'register.html', {'form':form})


def customer_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        return render(request, 'record.html', { 'customer_record':record })
    else:
        messages.success(request, "Only authorized users have access to the page!!!")
        return redirect('home')


def delete_record(request, id):
    if request.user.is_authenticated:
        deleted_record = Record.objects.get(id=id)
        deleted_record.delete()
        messages.success(request, "You heve deleted an object from Records!!!")
        return redirect('home')
    else:
        messages.success(request, "For doing this stuff you need to be authorized!!!")
        return redirect('home')


def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "You've successfuly create an instance of Record!!!")
                return redirect('home')

            messages.success(request, "Try to fill all fields by correct values!")
        else:
            form = AddRecordForm()

        return render(request, 'add_record.html', { 'form':form })
    else:
        messages.success(request, "For doing this stuff you need to be authorized!!!")
        return redirect('home')



def update_record(request, id):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=id)
		form = AddRecordForm(request.POST or None, instance=current_record)

		if form.is_valid():
			form.save()
			messages.success(request, "Record has been updated!!!")
			return redirect('home')
		return render(request, 'update_record.html', { 'form':form })
	else:
		messages.success(request, "For doing this stuff you need to be authorized!!!")
		return redirect('home')
