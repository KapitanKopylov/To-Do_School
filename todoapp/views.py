import re
from django.shortcuts import render, redirect
from todoapp.models import TodoItem, TodoUsers
from django.http import HttpResponse, JsonResponse
import json

mail = ''
password = ''

def main(request):
    pass

def account(request):
    return render(request, 'account.html')

def authentification(request):
    global mail
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            mail = data.get('mail')
            password = data.get('password')
            print("success")
            # return redirect('index')
            return JsonResponse({'message': "success"}, content_type="application/json", status=200)
        except json.JSONDecodeError:
            print("We have some problem")
            return HttpResponse(json.dumps({"error": "Invalid data"}), content_type="application/json", status = 400)
    else:
        return HttpResponse(json.dumps({"error": "Invalid request"}), content_type="application/json", status = 400)


def add_user(request):
    # if request.method == 'POST':
    #     adress = request.POST.get('adress')
    #     password = request.POST.get('password')
    #     try:
    #         TodoUsers.objects.get(mail = adress)
    #     except TodoUsers.DoesNotExist:
    #         User = TodoUsers(mail = adress, password = password)
    #         User.save()
        
    return redirect('index')

def index(request):
    # print('index')
    # global mail
    # print(mail)

    # if request.method == "POST":
        # try:
            # data = json.loads(request.body.decode('utf-8'))
    #         mail = data.get('mail')
    #         password = data.get('password')
    #         items = TodoItem.objects.filter(mail=mail)
    #         print('ok')
    #         # return render(request, 'index.html', {'items': items})
    #         # render(request, 'index.html', {'items': items})
    #         # return redirect('index')
    #         return HttpResponse(content_type="application/json", status = 200)
    #     except json.JSONDecodeError:
    #         print("We have some problem")
    #         return HttpResponse(json.dumps({"error": "Invalid data"}), content_type="application/json", status = 400)
    # else:
    #     return HttpResponse(json.dumps({"error": "Invalid request"}), content_type="application/json", status = 400)
    items = TodoItem.objects.all()
    return render(request, 'index.html', {'items': items})

def add_item(request):
    global mail
    # user = request.user
    # if user == mail:
    if request.method == 'POST':
        # print(request.POST)
        text = str(request.POST["text"])
        # print(text)
        text_arr = [i for i in text.split()]
        for numbers in text.split():
            if numbers == "7":
                text = text.replace(numbers, "семь")
        # if text:
        #     text = text[0].upper() + text[1:]
        if text.strip():
            try:
                TodoItem.objects.get(item_id = text)
            except TodoItem.DoesNotExist:
                item = TodoItem(item_id = text, text = text, mail = mail)
                item.save()
                print(f"Добавлено: {request.POST['text']}, в аккаунт: {mail}") 
            else:
                for i in range(len(TodoItem.objects.all())):
                    try:
                        TodoItem.objects.get(item_id = text + str(i))
                    except TodoItem.DoesNotExist:
                        item = TodoItem(item_id = text + str(i), text = text)
                        item.save()
                        print(f"Добавлено: {request.POST['text']}") 
                        break

    return redirect('index')

def delete(request, item):
    try:
        TodoItem.objects.get(item_id = item)
    except TodoItem.DoesNotExist:
        print("Item DoesN't Exist")
    else:
        item_to_delete = TodoItem.objects.get(item_id = item)
        print(f"Удалено: {item_to_delete.item_id}")
        item_to_delete.delete()
    return HttpResponse(content_type="application/json", status = 200)

def turn_On(request, item):
    try:
        TodoItem.objects.get(item_id = item)
    except TodoItem.DoesNotExist:
        print("Item DoesN't Exist")
    else:
        item_to_switch = TodoItem.objects.get(item_id = item)
        item_to_switch.completed = True
        item_to_switch.save()
        print(f'Выполнено "{item_to_switch.item_id}"')
    return HttpResponse(content_type="application/json", status = 200)

def turn_Off(request, item):
    try:
        TodoItem.objects.get(item_id = item)
    except TodoItem.DoesNotExist:
        print("Item DoesN't Exist")
    else:
        item_to_switch = TodoItem.objects.get(item_id = item)
        item_to_switch.completed = False
        item_to_switch.save()
        print(f'Ошибочка, не выполнено "{item_to_switch.item_id}"')
    return HttpResponse(content_type="application/json", status = 200)