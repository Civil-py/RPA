from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from .models import   Answers, BusinessUnit, Process, BusinessUnitManagers
from .forms import   AnswerForm, BusinessUnitForm, ProcessForm, ProcessConfigForm, BusinessUnitManagersForm
import smtplib
import ssl
import os
from uuid import uuid4
from .comp import Suitability, Ready, Benefit, RPAVP, Blockers, HumanInputs, HIGHEST



# Create your views here.

def superuser_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_superuser)(view_func))
    return decorated_view_func
def is_superuser(user):
    return user.is_superuser

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {user}')
            return redirect('business_units')
        else:
            return render(request, 'rpa/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'rpa/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def get_user_busniess_unit_id(user):
    logged_in_user_unit = get_object_or_404(BusinessUnitManagers, user=user).business_unit
    return logged_in_user_unit

def index(request):

    return render(request, "rpa/home.html", )

@superuser_required
def add_business_unit(request):
    form = BusinessUnitForm(initial={   'created_date': datetime.now()})
    if request.method == "POST":
        form = BusinessUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("business_units")
        else:
            messages.error(request, "Form is not valid")


    # context = {'form': form}
    return render(request, "rpa/add_business_unit.html", {
        'form': form
    })
@login_required
def business_units(request):

    user = request.user

    if is_superuser(user):
        business_units = BusinessUnit.objects.all()
        return render(request, "rpa/business_units.html", {
            "business_units": business_units
        })
    else:
        user_unit = get_user_busniess_unit_id(user).id
        users_business_units = BusinessUnit.objects.filter(id=user_unit)
        return render(request, "rpa/business_units.html", {
            "business_units": users_business_units
        })


@login_required
def view_business_unit(request, id):
    business_unit = BusinessUnit.objects.get(id=id)
    processes = Process.objects.filter(business_unit_id=id)

    process_data = []

    for process in processes:
        process_id = process.id
        process_name = process.name
        try:
            answers = Answers.objects.get(process=process)

            ready = Ready.ready(answers)
            ben = Benefit.benefit(answers)
            vp = RPAVP.rpa_vp(answers)
            bk = Blockers.blockers(answers)
            human_input = HumanInputs.inputs(answers)
            suitability_score = Suitability.suitability(answers)
            suit = round(sum(suitability_score) / HIGHEST * 100)

            process_data.append({
                "process": process,
                "name": process_name,
                "process_id": process_id,
                "ready": ready,
                "ben": ben,
                "vp": vp,
                "bk": bk,
                "human_input": human_input,
                "suit": suit,
            })

        except Answers.DoesNotExist:
            process_data.append({
                "process": process,
                "name": process_name,
                "process_id": process_id,
                "ready": None,
                "ben": None,
                "vp": None,
                "bk": None,
                "human_input": None,
                "suit": None,
            })


    return render(request, "rpa/view_business_unit.html", {
        "business_unit": business_unit,
        "processes": processes,
        "process_data": process_data
    })


def edit_business_unit(request, id):
    business_unit = BusinessUnit.objects.get(id=id)
    form = BusinessUnitForm(instance=business_unit, initial={'last_updated': datetime.now()})
    if request.method == "POST":
        form = BusinessUnitForm(request.POST, instance=business_unit)
        if form.is_valid():
            form.save()
            messages.success(request, f"{business_unit} edited")
            return redirect('business_unit',  id=id)

    context = {'form': form,
               'business_unit': business_unit
}
    return render(request, 'rpa/edit_business_unit.html', context)


def delete_business_unit(request, id):
    business_unit = BusinessUnit.objects.get( id=id)
    business_unit.delete()
    messages.success(request, f'Business Unit {business_unit.name} Removed')
    return redirect('business_units')

def add_business_unit_managers(request, id):
    business_unit = get_object_or_404(BusinessUnit, id=id)
    if request.method == "POST":
        form = BusinessUnitManagersForm(request.POST, site_instance=business_unit,)
        if form.is_valid():
            form.save()
            return redirect('business_units', )
    else:
        form = BusinessUnitManagersForm(initial={'business_unit': business_unit, 'assigned': datetime.now()}, site_instance=business_unit)

    return render(request, "rpa/add_business_unit_managers.html", {
        'form': form,
        'business_unit': business_unit
    })


def add_process(request, id):
    business_unit = BusinessUnit.objects.get(id=id)
    form = ProcessForm(initial={   'created_date': datetime.now(), 'business_unit': id})
    if request.method == "POST":
        form = ProcessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_business_unit", id=id)
        else:
            messages.error(request, "Form is not valid")


    # context = {'form': form}
    return render(request, "rpa/add_process.html", {
        'form': form,
        'business_unit': business_unit
    })

def view_process(request,id):

    process= Process.objects.get(id=id)
    try:
        answers = Answers.objects.get(process=process)
        comp = Ready.ready(answers)
        ben = Benefit.benefit(answers)
        vp = RPAVP.rpa_vp(answers)
        bk = Blockers.blockers(answers)
        human_input = HumanInputs.inputs(answers)
        suit = round(sum(Suitability.suitability(answers))/HIGHEST*100)


        return render(request, "rpa/view_process.html", {

            "process": process,
            'answers': answers,
            'comp': comp,
            'suit': suit,
            'benefit': ben,
            'vp': vp,
            'bk': bk,
            'input': human_input
        })

    except Answers.DoesNotExist:
        answers = None


    return render(request, "rpa/view_process.html", {

        "process": process,
        # 'answers': answers,
        # 'comp': comp
    })


def edit_process(request, id):
    process = Process.objects.get(id=id)
    form = ProcessForm(instance=process, initial={'last_updated': datetime.now()})
    if request.method == "POST":
        form = ProcessForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            messages.success(request, f"{process.name} sucessfully edited")
            return redirect('view_process',  id=id)

    context = {'form': form,
               'process': process
}
    return render(request, 'rpa/edit_process.html', context)

def config_process(request, id):
    process = Process.objects.get(id=id)
    form = ProcessConfigForm(instance=process, initial={'last_updated': datetime.now()})
    if request.method == "POST":
        form = ProcessConfigForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            messages.success(request, f"{process.name} sucessfully configured")
            return redirect('view_process',  id=id)

    context = {'form': form,
               'process': process
}
    return render(request, 'rpa/process_config.html', context)


def comp(request, id):
    process= Process.objects.get(id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST,initial={'process': id, 'created_date': datetime.now()})
        if form.is_valid():
            # answer = form.save(commit=False)
            # answer.process = process  # Manually assign the foreign key
            # answer.save()
            form.save()
            messages.success(request, f"Process {process.name} Compatability Added Successfully")
            return redirect('index')

        else:
            messages.error(request, "Form is not valid")
    else:
        form = AnswerForm(initial={'process': id, 'created_date': datetime.now()})

    return render(request, "rpa/comp.html", {'form': form,
                                             "process": process})


def edit_comp(request, id):
    process = Process.objects.get(id=id)
    answers = Answers.objects.get(process=id)
    form = AnswerForm(instance=answers, initial={'process': id,'last_updated': datetime.now()})
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answers)
        if form.is_valid():
            form.save()
            messages.success(request, f"{process.name} sucessfully edited")
            return redirect('view_process',  id=id)

    context = {'form': form,
               'process': process
}
    return render(request, 'rpa/edit_comp.html', context)


def delete_process(request, id):
    process = Process.objects.get( id=id)
    process.delete()
    messages.success(request, f'process {process.name} Removed')
    return redirect('business_units')

