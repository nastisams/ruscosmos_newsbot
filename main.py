import lxml
import requests
import re
import telebot
import datetime
import config
import bot_worker
from bs4 import BeautifulSoup



bot = telebot.TeleBot(config.token)

pict_main = 'https://www.roscosmos.ru/im/logo_roscosmos.png'

def cosmos_news(day, id):
    url = 'https://www.roscosmos.ru/102/'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml')
    dates = []
    names = []
    picts = []
    anons = []
    links = []
    bot.send_message(id, "Роскосмос:")
    block = soup.find_all('div', {'class':'newslist'})
    for i in block:
        dates.append(i.find_all('span', {'class':'date'})[0].text.strip())
        names.append(i.find_all('span', {'class':'name'})[0].text.strip())
        picts.append('https://www.roscosmos.ru' + i.find_all('img')[0]['src'])
        anons.append(i.find_all('span', {'class':'anons'})[0].text.strip())
        links.append('https://www.roscosmos.ru' + i.find_all('a', {'class':'link'})[0]['href'])
    if day == 0:
        r = 0
        for j in range(0, len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today():
                bot.send_message(id, dates[j])
                bot.send_photo(id, picts[j])
                bot.send_message(id, names[j])
                bot.send_message(id, links[j])
                r += 1
            else:
                continue
        if r == 0:
            bot.send_message(id, 'К сожалению, за сегодня у Роскосмоса еще новостей нет')
    elif day == 1:
        s = 0
        for j in range(0, len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today() - datetime.timedelta(days = 2):
                bot.send_message(id, dates[j])
                bot.send_photo(id, picts[j])
                bot.send_message(id, names[j])
                bot.send_message(id, links[j])
                s += 1
            else:
                continue
        if s == 0:
            bot.send_message(id, 'К сожалению, за вчера у Роскосмоса новостей нет')
    elif day == 2:
        for j in range(0, 3):
            bot.send_message(id, dates[j])
            bot.send_photo(id, picts[j])
            bot.send_message(id, names[j])
            bot.send_message(id, links[j])
    else:
        pass

def tsniimash_news(day, id):
    url = 'https://www.tsniimash.ru/press-center/news/'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml')
    dates = []
    names = []
    picts = []
    links = []
    bot.send_message(id, "ЦНИИмаш:")
    block = soup.find_all('div', {'class':'grid-col-3'})
    for i in block:
        dates.append(i.find_all('div', {'class':'card2__date'})[0].text.strip())
        names.append(i.find_all('div', {'class':'card2__link-wrap'})[0].text.strip())
        picts.append('https://www.tsniimash.ru' + i.find_all('img')[0]['src'])
        links.append('https://www.tsniimash.ru' + i.find_all('a', {'class':'card2__link'})[0]['href'])
    if day == 0:
        r = 0
        for j in range(0,len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today():
                bot.send_message(id , dates[j])
                bot.send_photo(id , picts[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                r += 1
            else:
                continue
        if r == 0:
            bot.send_message(id, 'К сожалению, за сегодня у ЦНИИмаш новостей еще нет')
    elif day == 1:
        s = 0
        for j in range(0,len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today() - datetime.timedelta(days = 4):
                bot.send_message(id , dates[j])
                bot.send_photo(id , picts[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                s += 1
            else:
                continue
        if s == 0:
            bot.send_message(id, 'К сожалению, за вчера у ЦНИИмаш новостей нет')
    elif day == 2:
        for j in range(0, 3):
            bot.send_message(id, dates[j])
            bot.send_photo(id, picts[j])
            bot.send_message(id, names[j])
            bot.send_message(id, links[j])
    else:
        pass

def rcs_news(day, id):
    url = 'http://russianspacesystems.ru/news/tidings/'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml')
    dates = []
    names = []
    picts = []
    links = []
    bot.send_message(id , "РКС:")
    block = soup.find_all('div',{'class':'wf-cell'})
    for i in block:
        dates.append(i.find_all('time')[0].text.strip())
        names.append(i.find_all('h3', {'class':'entry-title'})[0].text.strip())
        picts.append(i.find_all('img')[0]['data-src'])
        links.append(i.find_all('h3', {'class':'entry-title'})[0].find_all('a')[0]['href'])
    if day == 0:
        r = 0
        for j in range(0,len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today():
                bot.send_message(id , dates[j])
                bot.send_photo(id , picts[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                r += 1
            else:
                continue
        if r == 0:
            bot.send_message(id, 'К сожалению, за сегодня новостей у РКС еще нет')
    elif day == 1:
        s = 0
        for j in range(0,len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today() - datetime.timedelta(days = 1):
                bot.send_message(id , dates[j])
                bot.send_photo(id , picts[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                s += 1
            else:
                continue
        if s == 0:
            bot.send_message(id, 'К сожалению, за вчера у РКС новостей нет')
    elif day == 2:
        for j in range(0, 3):
            bot.send_message(id, dates[j])
            bot.send_photo(id, picts[j])
            bot.send_message(id, names[j])
            bot.send_message(id, links[j])
    else:
        pass


def laspace_news(day, id):
    url = 'https://www.laspace.ru/press/news/'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml').find_all('ul', {'class':'news-list'})[0]
    dates = []
    names = []
    anons = []
    links = []
    bot.send_message(id , "НПО Лавочкина:")
    block = soup.find_all('li')
    for i in block:
        dates.append(i.find_all('span')[0].text.strip())
        names.append(i.find_all('a')[0].text.strip())
        anons.append(i.find_all('div')[0].text.strip())
        links.append('https://www.laspace.ru' + i.find_all('a')[0]['href'])
    if day == 0:
        r = 0
        for j in range(0,len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today():
                bot.send_message(id , dates[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                r += 1
            else:
                continue
        if r == 0:
            bot.send_message(id,'К сожалению, за сегодня у НПО Лавочкина новостей еще нет.')
    elif day == 1:
        s = 0
        for j in range(0,len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today() - datetime.timedelta(days = 3):
                bot.send_message(id , dates[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                s += 1
            else:
                continue
        if s == 0:
            bot.send_message(id, 'К сожалению, за вчера у НПО ЛАвочкина новостей нет')
    elif day == 2:
        for j in range(0, 3):
            bot.send_message(id, dates[j])
            bot.send_message(id, names[j])
            bot.send_message(id, links[j])
    else:
        pass

def tsenki_news (day, id):
    url = 'http://www.russian.space/101/'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml')
    dates = []
    names = []
    picts = []
    anons = []
    links = []
    bot.send_message(id, "ЦЭНКИ:")
    block = soup.find_all('div',{'class':'newslist'})
    for i in block:
        dates.append(i.find_all('span', {'class':'date'})[0].text.strip())
        names.append(i.find_all('span', {'class':'name'})[0].text.strip())
        picts.append('http://www.russian.space' + i.find_all('img')[0]['src'])
        anons.append(i.find_all('span', {'class':'anons'})[0].text.strip())
        links.append('http://www.russian.space' + i.find_all('a', {'class':'link'})[0]['href'])
    if day == 0:
        r = 0
        for j in range(0,len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today():
                bot.send_message(id , dates[j])
                bot.send_photo(id , picts[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                r += 1
            else:
                continue
        if r == 0:
            bot.send_message(id, 'К сожалению, за сегодня у ЦЭНКИ еще новостей нет')
    elif day == 1:
        s = 0
        for j in range(0, len(dates)):
            if datetime.datetime.strptime(dates[j], '%d.%m.%Y').date() == datetime.date.today() - datetime.timedelta(days = 2):
                bot.send_message(id , dates[j])
                bot.send_photo(id , picts[j])
                bot.send_message(id , names[j])
                bot.send_message(id , links[j])
                s += 1
            else:
                continue
        if s == 0:
            bot.send_message(id, 'К сожалению, за вчера у ЦЭНКИ новостей нет')
    elif day == 2:
        for j in range(0, 3):
            bot.send_message(id, dates[j])
            bot.send_photo(id, picts[j])
            bot.send_message(id, names[j])
            bot.send_message(id, links[j])
    else:
        pass

@bot.message_handler(commands=["info"])
def cmd_info(message):
    bot.send_message(message.chat.id, "Я умею рассказывать по запросу новости русского космоса.\n"
                                      "Для начала нужно выбрать за какой день нужны новости:\n"
                                      "Я знаю только за сегодня или вчера, или могу дать несколько последних новостей.\n"
                                      "Затем нужно выбрать новости каких организаций тебе нужны.\n"
                                      "Я пока знаю только новости самого Роскосмоса, а также его предприятий:\n"
                                      "ЦНИИмаш, РКС, НПО ЛАвочкина и ЦЭНКИ.\n")
    bot.send_message(message.chat.id, "Посмотреть этот список можно по команде /list_organizations.\n"
                                      "Вводить организации нужно через запятую и как у меня в списке.\n"
                                      "Ну а если хочешь увидеть все команды, которые я знаю, то в помощь /commands.\n"
                                      "А если хочешь прервать все и начать выбирать день новостей, то введи /reset.")

@bot.message_handler(commands=["list_organizations"])
def cmd_listfields(message):
    x = ['Роскосмос', 'ЦНИИмаш', 'РКС', 'НПО Лавочкина', 'ЦЭНКИ']
    bot.send_message(message.chat.id, ", ".join(x))

@bot.message_handler(commands=["commands"])
def cmd_commands(message):
    bot.send_message(message.chat.id, "/reset - если хочешь прервать все и начать выбирать день новостей.\n"
                                      "/start - начать нашу беседу.\n"
                                      "/info - расскажу о себе.\n"
                                      "/commands - если хочешь увидеть все команды, которые я знаю.\n"
                                      "/list_organizations - список организаций, по которым могу рассказать новости")

@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Хорошо, начнем сначала.\n"
                                      "Новости за какой день ты хочешь получить: сегодня, вчера или последние?\n"
                                      "Если нужно понять, что я умею, введи /info или /commands.")
    bot.send_photo(message.chat.id, pict_main)
    bot_worker.set_state(message.chat.id, config.States.S_ENTER_DAY.value)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot_worker.set_state(message.chat.id, config.States.S_START.value)
    state = bot_worker.get_current_state(message.chat.id)
    bot.send_message(message.chat.id, "Приветсвую тебя, любитель космоса! Я новенький, еще совсем маленький, но все-таки уже ruscosmos_newsbot:) \n"
                                      "Новости за какой день ты хочешь получить: сегодня, вчера или последние?\n"
                                      "Введи /info, если хочешь узнать, что я умею.\n"
                                      "Введи /commands, если нужно узнать все мои команды.\n"
                                      "Введи /reset, чтобы начать нашу беседу заново.")
    bot.send_photo(message.chat.id, pict_main)
    bot_worker.set_state(message.chat.id, config.States.S_ENTER_DAY.value)


@bot.message_handler(func=lambda message: bot_worker.get_current_state(message.chat.id) == config.States.S_ENTER_DAY.value
                     and message.text.strip().lower() not in ('/reset', '/info', '/start', '/commands',
                                                              '/list_organizations'))
def get_day(message):
    bot_worker.del_state(str(message.chat.id)+'day')
    if message.text.lower().strip() == 'вчера' or message.text.lower().strip() == '/вчера':
        bot.send_message(message.chat.id, "Хорошо, я понял, тебе нужны новости за вчера.\n"
                                          "Но сначала нужно определиться, чьи новости тебе интересны.\n"
                                          "Пожалуйста, введи одну или несколько организаций через запятую.\n"
                                          "Список организаций можно узнать по команде /list_organizations.\n"
                                          "Введи /info, если хочешь узнать, что я умею.\n"
                                          "Введи /reset, чтобы начать нашу беседу заново.")
        bot_worker.set_state(str(message.chat.id)+'day', 'yesterday')
        bot_worker.set_state(message.chat.id, config.States.S_ENTER_ORGANIZATION.value)
    elif message.text.lower().strip() == 'сегодня' or message.text.lower().strip() == '/сегодня':
        bot.send_message(message.chat.id, "Хорошо, я понял, тебе нужны сегодняшние новости.\n"
                                          "Но сначала нужно определиться, чьи новости тебе интересны.\n"
                                          "Пожалуйста, введи одну или несколько организаций через запятую.\n"
                                          "Список организаций можно узнать по команде /list_organizations.\n"
                                          "Введи /info, если хочешь узнать, что я умею.\n"
                                          "Введи /reset, чтобы начать нашу беседу заново.")
        bot_worker.set_state(str(message.chat.id) + 'day', 'today')
        bot_worker.set_state(message.chat.id, config.States.S_ENTER_ORGANIZATION.value)
    elif 'последние' in message.text.lower().strip():
        bot.send_message(message.chat.id, "Хорошо, я понял, тебе нужны последние новости.\n"
                                          "Но сначала нужно определиться, чьи новости тебе интересны.\n"
                                          "Пожалуйста, введи одну или несколько организаций через запятую.\n"
                                          "Список организаций можно узнать по команде /list_organizations.\n"
                                          "Введи /info, если хочешь узнать, что я умею.\n"
                                          "Введи /reset, чтобы начать нашу беседу заново.")
        bot_worker.set_state(str(message.chat.id) + 'day', 'last')
        bot_worker.set_state(message.chat.id, config.States.S_ENTER_ORGANIZATION.value)
    else:
        bot.send_message(message.chat.id, "Кажется, мы уже общались.\n"
                                          "И сейчас нужно выбрать, за сегодня, вчера или последние вы хотите получить новости.\n"
                                          "Введите, пожалуйста, сегодня или вчера.\n"
                                          "Введи /info, если хочешь узнать, что я умею.\n"
                                          "Введи /reset, чтобы начать нашу беседу заново.")

@bot.message_handler(func=lambda message: bot_worker.get_current_state(message.chat.id) == config.States.S_ENTER_ORGANIZATION.value
                     and message.text.strip().lower() not in ('/reset', '/info', '/start', '/commands',
                                                              '/list_organizations'))

def enter_organization(message):
    bot_worker.del_state(str(message.chat.id) + 'organizations')
    organizations = [x.strip() for x in re.split(',', message.text)]
    bot.send_message(message.chat.id, 'Спасибо, подбираю для тебя информацию.')
    bot_worker.set_state(str(message.chat.id) + 'organizations', organizations)
    lst = ['Роскосмос', 'ЦНИИмаш', 'РКС', 'НПО Лавочкина', 'ЦЭНКИ']
    if bot_worker.get_current_state(str(message.chat.id)+'day').strip() == 'today':
        d = 0
    elif bot_worker.get_current_state(str(message.chat.id)+'day').strip() == 'yesterday':
        d = 1
    elif bot_worker.get_current_state(str(message.chat.id)+'day').strip() == 'last':
        d = 2
    else:
        pass
    errors = [i for i in organizations if i not in lst]
    org_w_err = [i for i in organizations if i in lst]
    # print(errors)
    if org_w_err != []:
        for i in org_w_err:
            if i == lst[0]:
                cosmos_news(d, message.chat.id)
            elif i == lst[1]:
                tsniimash_news(d, message.chat.id)
            elif i == lst[2]:
                rcs_news(d, message.chat.id)
            elif i == lst[3]:
                laspace_news(d, message.chat.id)
            elif i == lst[4]:
                tsenki_news(d, message.chat.id)
        if errors != []:
            bot.send_message(message.chat.id,
                             "Несколько наименований введено направильно, или я их не знаю :(\n"
                             "Вот они:" + ", ".join(errors) + "\n"
                             "Используй команду /list_organizations, чтобы увидеть как правильно нужно писать организации.")
        else:
            bot_worker.set_state(message.chat.id , config.States.S_START.value)
    else:
        bot.send_message(message.chat.id, 'Что-то пошло не так, пожалуйста, введи через запятую правильно организации.'
                                          'Используй команду /list_organizations, чтобы увидеть как правильно нужно писать организации.')
        bot_worker.del_state(str(message.chat.id) + 'organizations')




@bot.message_handler(func=lambda message: message.text not in ('/reset', '/info', '/start', '/commands',
                                                              '/list_organizations'))
def cmd_sample_message(message):
    bot.send_message(message.chat.id, "Я ruscosmos_newsbot и умею только рассказывать новости!\n"
                                      "Поэтому нажми /start и давай начнем. \n"
                                      "Введи /info, если хочешь узнать, что я умею.\n")
    bot.send_photo(message.chat.id, pict_main)


if __name__ == '__main__':
    bot.infinity_polling()
