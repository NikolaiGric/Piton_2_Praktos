person = {}


def hi_human():
    while True:
        na = input("Как к Вам можно обращаться? ")
        try:
            ag = int(input("Сколько вам лет? "))
            person = {
                "name": na,
                "age": ag
            }
            break
        except:
            print("Вы ввели не возраст, введите свой возраст.")

    person = person
    agi = person["name"]
    print(f'Приветствую {agi} в своей текстовой игре новелле\nПойдём в сюжет!')


hi_human()

print('''Вы попали в удивительный мир \"Варкрафт\": мир состоит из 4 основных рас: орки, эльфы, люди и нежить.
Этот мир уже 2 столетия охвачен кровопролитной войной, но в последний год всё изменилось: умер король людей Лотар1 и Вам предстоит возглавить государство людей.
Государство находиться в кризисе за двести лет люди устали от войны, да и экономика страдает, нежить захватывает всё большие границы Вашего государства. Государство на порследнем вздохе именно Вы должны помочь государству людей выжить.
Выбирай молодой правитель путь по которому пойдёт твоё государство, но помни за тобой ответственность за миллионы жизней''')

stop = []


def sujet():
    while (stop != [1, 2, 3, 4, 5]):
        unhuman()
        stop.append(1)

        economic()
        stop.append(2)

        var()
        stop.append(3)

        rost()
        stop.append(4)

        ocrujenie()
        stop.append(5)


collections = []


def unhuman():
    print('У государства людей проблема: Нежить захватывает всё больше наших территорий, что будем делать?')
    i = 0
    while (i != 2):
        print(
            '1) Зачем что-то делать, люди сами справятся\n2) Вложить много денег в армию и нанести решающий удар!\n3) Вкладываться в развитие техгологий')
        try:
            i = int(input())
            if (i == 1):
                print("Слишком умное решение)")
            elif (i == 2):
                print("Хорошие решение! Армия врага разбита!")
                print("Вы получили достижение: Победитель Легиона")
                collections.append("Победитель Легиона,")
            elif (i == 3):
                print(
                    "Вы вложились в технологии умное решение, но разработка технологий закончилась когда нас захватили(")
            else:
                print("Вы выбрали неправильное действие, выбирите из списка.")
        except ValueError:
            print("Введите цифру!")


def economic():
    print("Но появляется ещё одна проблема: экономика сейчас не в лучшем состоянии, что будем делать?")
    while (True):
        print('1) Увеличеть налоги\n2) Инвестировать всё в банки орды\n3) Уменьшить налоги на бизнес для крестьян')
        try:
            i = int(input())
            if (i == 3):
                print(
                    "Правильное решение, теперь у крестьян организуются больше кооперативов и приток в казну увеличился, stoncs")
                print("Вы получили достижение: Экономист")
                collections.append("Экономист,")
                break
            elif (i == 2):
                print("Это были МММ пирамиды орда нас обманула")
            elif (i == 1):
                print("И без того бедные крестьяне, стали ещё беднее, и подняли бунт, с революцией, Вас свергли.")
            else:
                print("Введите правльное действие вашего действия не существует.")
        except ValueError:
            print("Введите ту цифру, которую у Вас просят!")


def var():
    print(
        "Пока вы отлично справляетесь, но к вам поступили сведения о том, что войны с другими рассами вызывают общественное недовольство, грядёт революция, что будем делать?")
    i = 0
    while (True):
        print('1) Повесить всех недовльных\n2) Идти до победного\n3) Наладить мир с другими государствами')
        try:
            i = int(input())
            if (i == 1 or i == 2):
                print('Автор игры пацифист, ваш ответ неправильный.')
            elif (i == 3):
                print("Люди больше не умирают и с радостью Вас поддерживают")
                print("Вы получили достижение: Военный миротворец")
                collections.append("Военный миротворец,")
                break
            else:
                print("Для кого здесь написан выбор действий :-)")
        except ValueError:
            print("Введите цифру!")


def rost():
    print(
        "На этом проблемы не закончились, у нам демографический кризис, люди больше не хотят детей, как это исправить?")
    b = {1, "ryzen_amd", False}
    while (True):
        print(
            '1) Ввести законы подержки многодетных и малодых семей\n2) Пропаганда деторождения\n3) Выделять больше денег из казны для хорошей жизни детей')
        try:
            i = int(input())
            print("Вы получили достижение: Великий демограф")
            collections.append("Великий демограф,")
            print("Ура Вы выбрали правильный варинт, люди счастливы!")
            if (False in b):
                break
        except ValueError:
            print("Введите цифру!")


def ocrujenie():
    print(
        "Вам пришлось покинуть королевство с целью: отпуска, вас не было всего неделю и тут поднялся заговор против вашего трона, наступает революция, что прикажете делать?")
    i = 0
    while (i != 1):
        print(
            '1) Объявить военное положение и армией начать гражданскую войну\n2) Поговорить чего хотят заговорщики\n3) Бежать из столицы королевства с надеждой на то что вам помогут те кто ещё вас поддерживают')
        try:
            i = int(input())
            if (i == 1):
                print('Заговорщики не успели опомниться как их армия была разбита, и вы победели их!')
                print("Вы получили достижение: Военный миротворец")
                collections.append("Победитель революций.")
                break
            elif (i == 2):
                print('Хорошаая попытка, но как только заговорщики вас увидили вас тут же повесели(.')
            elif (i == 3):
                print(
                    "Вас никто не успел поддержать, так как пока вы ехали из столицы вас нашли шпионы, вы были посажены в тюрьму.")
            else:
                print("Почитай внимательно условия выбора.")
        except ValueError:
            print("Введите цифру!")


sujet()
print('''К сожалению наша игра закончилаась и наврядли мир увидит более мудрого правителя чем ВЫ, хотелось бы закончить на следующей ноте, и подарить вашему кругозору следующий замечательный стих:
Как говорят:
«инцидент исперчен»,
любовная лодка 
разбилась о быт.
Я с жизнью в расчёте 
и не к чему перечень
взаимных болей,
бед
и обид.
Счастливо оставаться.
Владимир Маяковский.
1930 г.
«Кругом измена, трусость и обман» Николай II ''')
print("Ваши достижения:", *collections)
