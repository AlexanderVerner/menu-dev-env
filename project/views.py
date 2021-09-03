from django.shortcuts import render, get_object_or_404
from menu.models import MenuShow

def first_page(request):
    menu_list = MenuShow.objects.all()
    return render(request, './index.html', {'menu_list' : menu_list})

def checkout(request):
    checks = request.POST.getlist('checks')
    print(checks)  # Проверяем наличие id галочек
    array_num = [int(item) for item in checks]  # перевод в числовой вид из стрингового представления
    appen = []
    flag = False # флаг для определения 2 и более выбранных элементов (для if-else в HTML-шаблоне)
    if (len(array_num)>1):
        for el in range(0, len(array_num)):
            flag = True
            count = array_num[el]  # получение значения первого элемента листа
            chk = MenuShow.objects.get(id=count)  # выбираем из БД значение, равное id объекта в БД
            print(chk)
            appen.append(chk)  # присоединение к массиву для вывода двух и более галочек в итоговой таблице
        checks_list = appen
    else:
        checks_list = MenuShow.objects.get(id=array_num[0])
        flag = False
        print(checks_list)
    print(appen)
    return render(request, './checkout.html', {'checks': checks, 'checks_list': checks_list, 'flag': flag})
