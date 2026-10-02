from django.shortcuts import render, HttpResponse

def ahoj(request):
        return HttpResponse('<h1>Ahooooooooooooooooooooooj</h1>')

def o_mne(request):
        kontext = {
                'meno':'David',
                'vek': 17,
                'zaluby': ['sport','hry','progravonie'],
        }
        return render(request, 'ulohy/o_mne.html', kontext)