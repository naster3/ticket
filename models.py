import uuid
from django.db import models
from users.models import User

class Ticket(models.Model):
    status_choices = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    )
    ticker_number = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    date_created = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    ticket_status = models.CharField(max_length=15, choices=status_choices)

    def __str__(self) -> str:
        return self.title

    @classmethod
    def create_ticket(cls, title, description, created_by):
        ticket = cls(
            title=title,
            description=description,
            created_by=created_by,
            ticket_status='Pending'
        )
        ticket.save()
        return ticket

    def update_ticket(self, title, description):
        self.title = title
        self.description = description
        self.save()

    def assign_ticket(self, assigned_to):
        self.assigned_to = assigned_to
        self.ticket_status = 'Active'
        self.accepted_date = models.DateTimeField.now()
        self.save()

    def close_ticket(self):
        self.ticket_status = 'Completed'
        self.is_resolved = True
        self.closed_date = models.DateTimeField.now()
        self.save()
