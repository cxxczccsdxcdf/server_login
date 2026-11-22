import time                           #библиотека времени когда зашёл пользователь
class Servers:                        #создаем класс сервера 
                                      
    def __init__(self,server_name):    # создаём функцию и объекты с ней
        self.server_name = server_name
        self.user = {}
        self.max_hp = 70
        self.sitting_time = 2.0
    def sitting_server(self, current_user_only): # функция настройками сервера с объектами
        if current_user_only is None: return     #условие для запуска сервера
        print(f"\n сервер {self.server_name}  запускаем")
        player_starts = {"hp": self.max_hp, "score": 0}
        while True:
            command = input(f"[{current_user_only}]>").strip().lower() #задали цикл и делаем проверку чтоб программа не вылетела
            if command == "выход пользователя":
                break      #останавка если пользователь  выходит
            elif command == "действие": 
                print("выполнение действия")  #во сколько польльзователь  зашёл и вышел
                time.sleep(self.setting_time)
                player_starts["score"] += random.randint(20, 70) 
                print(f"завершил действе {player_starts["score"]}")

    def register_user(self, max_users): #создали новую функцию для максмального количества пользоваетелей
        print(f"Регистрация на на нашем сервере [{self.server_name}]") #начало регистрации на сервере
        spisok_mats = ["пздц", "пиздец", "блять"] #список матов которые нельзя использовать
        while len(self.user) < max_users: #цикл количесвта пользователей меньше чем максимум пользователей
            name = input("напиши имя пользователя").strip().lower() #здесь пишем имя задали проверку чтрб программа после отпечаток не вылетела
            her_spisok_mat = False  #ложь если ник с матом
            for mat in spisok_mats: #цикл матов мы добавляем в список запрещённых матов
                if mat in name:     #берет кажыдй список 
                    her_spisok_mats = True 
                    break           #завершили цикл чтоб не повторялось
            if her_spisok_mat:   #условие если какой то имя содержи мат
                 print(f"бан ник {name} содержит мат доступ ограничекн")
                 continue     #вовращение цикла

            if name in self.user: #условие при котором ник будет занят мы помещаем в селф юзер
                print(f"ошибка ник {name} занят! придумайте пожалуйстра другой")
                continue  #берёт с сначала где просит ввести ник
            easy_password = ["1235049", "3304049", "qwertyuiop"] #список паролей при которых выдаст ошибку
            while True: #цикл будет повторяться если пароль неверный или кажыдй раз когда пользваоетль будет заходить
              password_input = input("введите пароль: ")
              if password_input in easy_password:  #к условию при вводе пароля добавляем недоступность легких паролей
                print("ошибка очень легкий пароль")
                continue  #вовращает нас на начало обьекта
              else:
                  self.user[name] = password_input
                  break  #заканчиваем цикл чтоб не бьло ошибки
            print(f"игрок [{name} мы успешно добавили на сервер")
            print("-" * 40)
        print("места закончились места завершив регистрацию")
        print(f"игроки на сервере добавлены {list(self.user.keys())}") #берёт из списка всех игроков
    def account_user(self): #создалм функцию при входе в аккаунт
        print(f"входим в аккаунт на сервер [{self.server.name}")
        name = input("введём имя")
        if name not in self.user:  #здесь если мы ведём пользователя которого нет на сервере
            print("такого пользователя нет")
            return None  
        attemps = 3   создали объект попыток
        while True:  #цикл верно если пароль неверный
            print(f"неверный пароль отсалось пыпок {attemps}")
            password = input("Введите пароль")
            if password == self.user[name]: 
                time_sleap = time.strftine("%d.%m.%Y.%H:%M:%S") #здесь время когда зашёл пользователь 
                print(f"пароль был введен верно {name}") #здесь будет указано имя пользователя котоырй ввёл пароль верно
                print(f"Точное время входа: {time_sleap}")
                print("_" * 80)
                return name #завершили функцию имя
            else:
                print("парль неверный вход недоступен")

                attemps -= 1  #вычитается количество попыток в случае неверного пароля
                print(f"пароль неверный {attemps}") 
                if attemps == 0:  #здесь если попыток не осталось в случае чего будет заморозка
                    print("мы поратиои все попытки заморозка через 3 секунд")
                    time.sleep(3) #через сколько времени будет замороженно
                    return None
                change = input("хотели ли вы изменить пароль (да/нет").strip().lower() #здесь пользователь выбирает правильный ответ от возможных отпечаток была поставлена проверка
                if change == да:
                    new_pwd = input("введиите новый пароль")  #здесь мы создали объект с вопросом при котором пользователь вводит новый пароль
                    self.user[name] = new_pwd  #у конкретного имени новый пароль
                    break #выходим чтоб сохранить новый пароль
                    print("мы изменили ваш пароль")
                else:
                    print("отменен вход") #после измнения нас сбрасывают и мы указываем те же джанные но с новым паролем
                    break
    def star_chat(self, prosto_user): 
        if prosto_user is None:
             return None
        print(f"подключен  в чат сервера {self.server_name}"),
        print("мы дали доступ к таким командам /history /game"),
        print("_" * 40)
        chat = ["[система]: приглашаем в чат"],
        words =  ["маты", "плохе слова"]
        while True:
            message =  input(f"[prosto_user]>").strip()
            if message.lower() == "exit":
                print("exit from chat")
                break
            elif message.lower == "history":
                print("history chat")
                for log in chat:
                    print(log)
                print("==================")
                continue
            elif message == "":
                continue
            mats_check = message.lower()
            bad_words = False
            for word in bad_words:
                if word in bad_words:
                    bad_words = True
                    break
            if bad_words:
                print("ошибка мы заблокирвоали ваше сообщение запретили маты")
                continue
            check_time = time.strtime("%H:%M:%s")
            formated_message = f"[{prosto_user} в {check_time}]: (message)"
            mats_check.append(formated_message)
            print(f" [отправили] {formated_message}")
passwords_users = [
    Servers("сервер админа"),
    Servers("сервер модера"),
    Servers("сервер офнера")
]
for my_server in passwords_users:
    print("=" * 30)
    print(f"доступен сервер {my_server.server_name}")
    print("=" * 30)
    my_server.register_user(2)
    logged_user = my_server.account_user()
    my_server.sitting_server(logged_user)
