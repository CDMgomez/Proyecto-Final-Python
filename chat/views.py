from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Message
from .forms import MessageForm

User = get_user_model()


@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'chat/inbox.html', {
        'messages': messages
    })


@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('chat:inbox')
    else:
        form = MessageForm(user=request.user)

    return render(request, 'chat/send_message.html', {
        'form': form
    })


@login_required
def conversation(request, username):
    other = get_object_or_404(User, username=username)
    # messages between request.user and other
    conv = Message.objects.filter(
        Q(sender=request.user, receiver=other) | Q(sender=other, receiver=request.user)
    ).order_by('timestamp')

    # Mark incoming messages as read
    unread = Message.objects.filter(sender=other, receiver=request.user, is_read=False)
    if unread.exists():
        unread.update(is_read=True)

    return render(request, 'chat/conversation.html', {
        'messages': conv,
        'other': other
    })
