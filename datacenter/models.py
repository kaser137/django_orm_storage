from django.db import models
from django.utils.timezone import localtime


def get_duration(visit):
    return localtime(visit.leaved_at) - localtime(visit.entered_at)


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    format_duration = f'{hours}h {minutes}min'
    return format_duration


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
