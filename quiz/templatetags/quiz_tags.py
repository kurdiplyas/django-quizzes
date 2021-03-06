from django import template

from django.contrib.auth.models import User
from quiz.models import QuizResult, Quiz

register = template.Library()

@register.filter(name='percentage')
def percentage(part, population):
    try:
        return (float(part) / float(population)) * 100
    except (ValueError, ZeroDivisionError):
        return ''

@register.filter(name='quiz_taken')
def quiz_taken(user, quiz):
    """Returns the amount of times the user has taken the specified quiz. Can
    also be used as a simple boolean."""
    if (not isinstance(user, User) or
        not isinstance(quiz, Quiz)):
        return ''
    return QuizResult.objects.filter(user=user, quiz=quiz).count()
