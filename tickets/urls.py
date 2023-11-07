from django.urls import path
from . import views

urlpatterns = [
    path('ticket-details/<int:pk>/',views.ticket_details,name='ticket_details'),
    path('create-ticket/',views.create_ticket,name='create_ticket'),
    path('update-ticket/<int:pk>/',views.update_ticket,name='update-ticket'),
    path('all-tickets/',views.all_tickets,name='all_tickets'),
    path('ticket-queue/',views.ticket_queue,name='ticket_queue'),
    path('accept-ticket/<int:pk>/',views.accept_ticket,name='accept-ticket'),
    path('closed-ticket/<int:pk>/',views.closed_ticket,name='closed-ticket'),
    path('workspace/',views.workspace,name='workspace'),
    path('all-closed-tickets/',views.all_closed_tickets,name='all-closed-tickets'),
    ]