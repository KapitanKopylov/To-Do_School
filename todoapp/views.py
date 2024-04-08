from django.shortcuts import render, redirect
from todoapp.models import TodoItem, TodoUsers
from django.http import HttpResponse, JsonResponse
import json

mail = ''
password = ''


def account(request):
    return render(request, 'account.html')


def authentification(request):
    if request.method == "POST":
        try:
            # data = json.loads(request.body.decode('utf-8'))
            mail = request.COOKIES.get('mail')
            password = request.COOKIES.get('password')
            print(f"mail: {mail}")
            print(f"password: {password}")
            try:
                TodoUsers.objects.get(mail=mail)
            except TodoUsers.DoesNotExist:
                user = TodoUsers(mail=mail, password=password)
                user.save()
                print('welcome')
                return JsonResponse({'message': "success"}, content_type="application/json", status=200)
            else:
                try:
                    TodoUsers.objects.get(password=password, mail=mail)
                except TodoUsers.DoesNotExist:
                    print('wronk!!!')
                    return JsonResponse({'message': "Wrong"}, content_type="application/json", status=401)
                else:
                    return JsonResponse({'message': "success"}, content_type="application/json", status=200)
        except json.JSONDecodeError:
            print("We have some problem")
            return HttpResponse(json.dumps({"error": "Invalid data"}), content_type="application/json", status=400)
    else:
        return HttpResponse(json.dumps({"error": "Invalid request"}), content_type="application/json", status=400)


def index(request):
    mail = request.COOKIES.get('mail')
    all_items = TodoItem.objects.all()
    items = []
    for i in all_items:
        if i.mail == mail:
            items.append(i)
    return render(request, 'index.html', {'items': items})


def add_item(request):
    mail = request.COOKIES.get('mail')
    if request.method == 'POST':
        text = str(request.POST["text"])
        for numbers in text.split():
            if numbers == "7":
                text = text.replace(numbers, "семь")
        if text.strip():
            try:
                TodoItem.objects.get(item_id=text, mail=mail)
            except TodoItem.DoesNotExist:
                item = TodoItem(item_id=text, text=text, mail=mail)
                item.save()
                print(f"Добавлено: {request.POST['text']}, в аккаунт: {mail}") 
            else:
                items = []
                for i in TodoItem.objects.all():
                    if i.mail == mail:
                        items.append(i)

                for i in range(len(items)):
                    try:
                        TodoItem.objects.get(item_id=text + str(i), mail=mail)
                    except TodoItem.DoesNotExist:
                        item = TodoItem(item_id=text + str(i), text=text, mail=mail)
                        item.save()
                        print(f'Добавлено: "{item.item_id}", в аккаунт: {mail}')
                        break

    return redirect('index')


def delete(request, item):
    mail = request.COOKIES.get('mail')
    try:
        TodoItem.objects.get(item_id=item, mail=mail)
    except TodoItem.DoesNotExist:
        print("Item DoesN't Exist")
    else:
        item_to_delete = TodoItem.objects.get(item_id=item, mail=mail)
        item_to_delete.delete()
        print(f'Удалено: "{item_to_delete.item_id}", из аккаунта: {mail}')
    return HttpResponse(status=200)


def turn_on(request, item):
    mail = request.COOKIES.get('mail')
    try:
        TodoItem.objects.get(item_id=item, mail=mail)
    except TodoItem.DoesNotExist:
        print("Item DoesN't Exist")
    else:
        item_to_switch = TodoItem.objects.get(item_id=item, mail=mail)
        item_to_switch.completed = True
        item_to_switch.save()
        print(f'Выполнено "{item_to_switch.item_id}"')
    return HttpResponse(content_type="application/json", status=200)


def turn_off(request, item):
    mail = request.COOKIES.get('mail')
    try:
        TodoItem.objects.get(item_id=item, mail=mail)
    except TodoItem.DoesNotExist:
        print("Item DoesN't Exist")
    else:
        item_to_switch = TodoItem.objects.get(item_id=item, mail=mail)
        item_to_switch.completed = False
        item_to_switch.save()
        print(f'Ошибочка, не выполнено "{item_to_switch.item_id}"')
    return HttpResponse(content_type="application/json", status=200)
