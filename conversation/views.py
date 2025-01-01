from django.shortcuts import render, redirect
from .models import Conversation
from .forms import ConversationMessageForm

def new_conversation(request):
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create()
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            
            return redirect('dashboard:index')
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })




