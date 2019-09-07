from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'textProcess/index.html')


def analyze_view(request):
    #getting text
    text = request.GET.get('text','default')
    print(text)

    #checking checkbox value
    remove_punctuations = request.GET.get('Punctuations','off')
    upper_case = request.GET.get('upper_case','off')
    new_line = request.GET.get('new_line','off')
    extra_space = request.GET.get('extra_space','off')
    remove_number = request.GET.get('remove_number','off')


    #removing Punctuations
    if (remove_punctuations == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text = ""
        for char in text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
        my_dict = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed_text}
        text = analyzed_text

    if (upper_case) == 'on':
        analyzed_text = ""
        for char in text:
            analyzed_text = analyzed_text + char.upper()

        my_dict = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed_text}
        text = analyzed_text

    if (new_line == 'on'):
        analyzed_text = ""
        for char in text:
            if char != '\n' and char != '\r':
                analyzed_text = analyzed_text + char

        my_dict = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed_text}
        text = analyzed_text

    if (extra_space == 'on'):
        analyzed_text = ""
        for index, char in enumerate(text):
            # It is for if a extraspace is in the last of the string
            if char == text[-1]:
                    if not(text[index] == " "):
                        analyzed_text = analyzed_text + char

            elif not(text[index] == " " and text[index+1]==" "):
                analyzed_text = analyzed_text + char

        my_dict = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed_text}
        text = analyzed_text

    if (remove_number == 'on'):
        analyzed_text = ""
        num = '0123456789'
        for char in text:
            if char not in num:
                analyzed_text = analyzed_text + char

        my_dict = {'purpose': 'Number removed', 'analyzed_text': analyzed_text}
        text = analyzed_text

    if(remove_punctuations != 'on' and  upper_case != 'on' and new_line != 'on' and extra_space != 'on' and remove_number != 'on' ):
        return  HttpResponse("please select at least one operation and try again")

    return render(request,"textProcess/analyze.html",my_dict)
