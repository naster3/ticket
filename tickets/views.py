import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Ticket
from .form import CreateTicketForm,UpdateTicketForm

def ticket_details(request,pk):
    tickets= Ticket.objects.get(pk=pk)
    context={'tickets':tickets}
    return render(request,'ticket/ticket_details.html',context)

def create_ticket(request):
    if request.method== "POST":
        form=CreateTicketForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.created_by=request.user
            var.ticket_status='pending'
            var.save()
            messages.info(request,'tu ticket ha sido creado')
            return redirect('dashboard')
        else:
            messages.warning(request,'los datos no son validos')
            return redirect("create-tickect")
    else:
        form=CreateTicketForm()
        context={'form': form}
        return redirect(request,'ticket/create-ticket.html',context)

def update_ticket(request, pk):
    ticket=Ticket.objects.get(pk=pk)
    if request.method== "POST":
        form=UpdateTicketForm(request.POST,instance=ticket)
        if form.is_valid():
            form.save()
            
            messages.info(request,'tu ticket ha sido actualizado')
            return redirect('dashboard')
        else:
            messages.warning(request,'los datos no son validos')
            #return redirect("create-tickect")
    else:
        form=CreateTicketForm()
        context={'form': form}
        return redirect(request,'ticket/updated-ticket.html',context)

def all_tickets(request):
    tickets=Ticket.objects.filter(created_by=request.user)
    context={'ticket':tickets}
    return render(request,'ticket/all_tickets.html',context)

def ticket_queue(request):
    tickets=Ticket.objects.filter(ticket_status='Pending')
    context={'ticket':tickets}
    return render(request,'ticket/ticket_queue.html',context)
def accept_ticket(request, pk):
    ticket=Ticket.objects.get(pk=pk)
    ticket.assigned_to=request.user
    ticket.ticket_status='Active'
    ticket.accepted_date= datetime.datetime.now()
    ticket.save()
    messages.info(request,'tu ticket ha sido aceptado')
    return redirect('ticket-queue')
def closed_ticket(request, pk):
    ticket=Ticket.objects.get(pk=pk)
    ticket.ticket_status='Complete'
    ticket.is_resolved=True
    ticket.closed_date= datetime.datetime.now()
    ticket.save()
    messages.info(request,'tu ticket ha sido completado, gracias por su uso')
    return redirect('ticket-queue')
def workspace(request):
    tickets= Ticket.objects.filter(assigned_to=request.user, is_resolved=False)
    context={'tickets':tickets}
    return render(request,'ticket/workspace.html',context)
def all_closed_tickets(request):
    tickets= Ticket.objects.filter(assigned_to=request.user, is_resolved=True)
    context={'tickets':tickets}
    return render(request,'ticket/all_closed_tickets.html',context)