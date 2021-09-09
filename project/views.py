from django.shortcuts import render, get_object_or_404
from menu.models import MenuShow

def first_page(request):
    menu_list = MenuShow.objects.all()
    return render(request, './index.html', {'menu_list' : menu_list})

def checkout(request):
    checks = request.POST.getlist('checks')
    array_num = [int(item) for item in checks]  # перевод в числовой вид из стрингового представления
    appen = []
    flag = False
    summ = 0
    if (len(array_num) != 0):
        for el in range(0, len(array_num)):
            count = array_num[el]  # получение значения первого элемента листа
            chk = MenuShow.objects.get(id=count)  # выбираем из БД значение, равное id объекта в БД
            appen.append(chk)  # присоединение к массиву для вывода двух и более галочек в итоговой таблице
            summ += int(chk.menu_price)
            chk_id = chk.id
            menu_title = chk.menu_title
            menu_allergens = chk.menu_allergens
            menu_price = chk.menu_price
        checks_list = appen
        flag = True
    else:
        flag = False
        checks_list = []
        menu_title = ''
        menu_allergens = ''
        menu_price = ''
        summ = 0
    return render(request, './checkout.html', {'checks': checks,
                                               'checks_list': checks_list,
                                               'summ' : summ,
                                               'menu_title': menu_title,
                                               'menu_allergens' : menu_allergens,
                                               'menu_price' : menu_price,
                                               'flag' : flag,})