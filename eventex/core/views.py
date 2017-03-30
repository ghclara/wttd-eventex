from django.shortcuts import render, get_object_or_404

from .models import Speaker, Talk


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(
        request,
        'core/speaker_detail.html',
        {'speaker': speaker}
    )


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.filter(start='10:00'),
        'afternoon_talks': Talk.objects.filter(start='13:00'),
    }
    return render(request, 'core/talk_list.html', context)
