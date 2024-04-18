# coding: UTF-8
import telebot
import secret
from telebot import types
from datetime import datetime

bot = telebot.TeleBot(secret.botToken)

startCommand = 'start'
helpCommand = 'help'
testCommand = 'test'

backToMainMenuButtonText = 'На головну'
weHaveRightsButtonText = 'У всіх нас є права/ДИТЯЧИЙ МУЛЬТФІЛЬМ/ЮНІСЕФ'
UNConventionButtonText = 'Конвенція ООН «Про права дитини»'
ChildrenRightsAccordingToUNButtonText = 'Права дитини згідно з Конвенцією'
CheckYourselfButtonText = "Перевір себе: твої права та обов'язки"
DoYouKnowYourRightsButtonText = 'Чи знаєш ти свої права? Вікторина'
RealLifeSituationsButtonText = 'На прикладі життєвих ситуацій дай відповідь: яке право дитини було порушено?'

backToMainMenuText = 'На головну'
weHaveRightsText = 'https://www.youtube.com/watch?v=ez51o35YiiI'
UNConventionText = """
Дитинство – період життя людини, коли формуються найважливіші функції організму, активно здійснюється засвоєння моральних норм, знань і цінностей, що дозволяє малюку почуватися повноцінним членом суспільства.

     Діти – це особлива соціально-демографічна група населення з віковими обмеженнями від народження до 18 років, яка має свої права, інтереси, специфічні проблеми, але не може відстоювати і захищати їх перед суспільством. Унаслідок цього сьогодні досить гостро постає проблема захисту дітей та їхніх прав.
Міжнародне співтовариство, Організація Об’єднаних Націй уже кілька десятиріч працюють над тим, щоб створити дітям усього світу якнайкращі умови для життя й усебічного розвитку. Результатом цієї праці стала низка міжнародних документів надзвичайної ваги, які стосуються прав дитини і забезпечення виживання, захисту та розвитку юного покоління. Зокрема, було створено дитячий фонд ООН – ЮНІСЕФ.
Основними міжнародними документами ЮНІСЕФ щодо прав дітей є: «Декларація прав дитини» (1959 р.), Конвенція ООН «Про права дитини» (1989 р.), Всесвітня декларація про забезпечення виживання, захисту і розвитку дітей (1990 р.). Базовим документом, спрямованим на захист дітей, є Конвенція «Про права дитини», прийнята Організацією Об’єднаних Націй. Це найперша у світовій історії глобальна угода щодо прав дитини: 191 країна світу ратифікувала Конвенцію, зобов’язавшись узгодити власне законодавство з її положеннями. Україна приєдналась до неї у 1991 році.
Раніше у світі турбота про дітей та їхній захист розглядалися як надання допомоги тим, хто її потребує. Конвенція ж визначає нову концепцію, проголошуючи забезпечення виживання, захисту і розвитку дітей обов’язком держави та суспільства, а не питанням доброї волі. Діти ще від народження мають усі основні свободи й невід’ємні права кожної людини.
Конвенція «Про права дитини» – міжнародний правовий документ, у якому закріплені гарантії прав дитини. Він поєднав у собі високі соціально-моральні та правові норми міжнародного стандарту й педагогічні основи спілкування дорослих із дітьми. Конвенція складається з преамбули і 54 статей. Усі статті можна згрупувати у три основні блоки:
І. Статті 1-41: основні статті, що визначають права дитини та обов’язки держав-сторін, які ратифікували Конвенцію.
ІІ. Статті 42-45: процедури моніторингу запровадження Конвенції.
ІІІ. Статті 46-54: формальні положення, які регламентують порядок, коли Конвенція набуває чинності.
"""
ChildrenRightsAccordingToUNFileName = 'Child-friendly-convention-UA.pdf'
CheckYourselfText = 'https://wordwall.net/play/71628/048/229'
DoYouKnowYourRightsText = 'https://wordwall.net/play/71628/028/866'
RealLifeSituationsText = 'Обери ситуацію'

mainMenuMarkup = types.ReplyKeyboardMarkup()
mainMenuMarkup.row(types.KeyboardButton(weHaveRightsButtonText), types.KeyboardButton(UNConventionButtonText))
mainMenuMarkup.row(types.KeyboardButton(ChildrenRightsAccordingToUNButtonText),
                   types.KeyboardButton(CheckYourselfButtonText))
mainMenuMarkup.row(types.KeyboardButton(DoYouKnowYourRightsButtonText),
                   types.KeyboardButton(RealLifeSituationsButtonText))

situations_index_name_map = {}
for i in range(11):
    situation_name_pattern = 'Ситуація'
    situation_index = i
    situations_index_name_map[situation_index] = situation_name_pattern + ' ' + str(i + 1)

situations_texts = [
    'У давнину була держава Спарта. Вона славилась своїм непереможними воїнами: сильними і мужніми. І кожну новонароджену дитину ретельно оглядали. Якщо дитина народжувалась слабкою і хворою - її скидали вниз. Яке право дитини порушували?',
    'Юрко постійно балується та розмовляє під час уроків. Яке право він порушує?',
    'У Маринки болить зуб. Коли мама зібралася вести її в стоматологію, дівчинка відмовилася, пояснивши, що зуб вже її не турбує. А насправді вона просто боїться йти до лікаря. Яке право не використала Маринка?',
    "Тарас купив свій улюблений журнал \"Спорт\". Він виніс його на подвір'я показати друзям. Раптом хлопчик із сусіднього будинку вихопив журнал і втік. Які права порушив хлопчик?",
    "На спортивному майданчику хлопці грали в футбол. Воротар Василь пропустив декілька м'ячів, його команда стала програвати. Хлопці посварили і вигнали його з гри. Чи порушили хлопці права Василя? Якщо так, то які? ",
    "Богдан підставив підніжку Катерині під час перерви. Дівчинка впала і розбила коліно. Чи було порушено права дівчинки?",
    "У Великій Британії дитина, маленький англійський хлопчик, був побитий палкою вітчимом, в результаті чого зазнав серйозних поранень. Європейський суд з прав людини виніс рішення про порушення права дитини. Яке?",
    "У багатодітній родині, де батьки незрячі, було відібрано чотирьох дітей і розміщено їх у різних інтернатних закладах. Діти під час судового засідання не були заслухані, а також розділені й розміщені в різних закладах. Європейський суд визнав це порушенням прав дітей. Яке право порушено?",
    "Коли Алексу виповнилось 12 років, він почав працювати на вугільній копанці по 12 годин на день. Тепер йому 14 років, і старший, що керує, вимагає, щоб він працював більше. Яке право порушено?",
    "У Києві та Харкові учасники злочинної організації під прикриттям діяльності клініки із подання послуг сурогатного материнства здійснювали продаж новонароджених дітей. За кордон незаконно вивезено 8 немовлят. Вартість послуг \"становило\" від 50 до 70 тис євро. Яке право порушено?",
    "На Закарпатті чоловік намагався продати дитину до ЄС за 25 тисяч  доларів США. Уповноважений Д. Лубінець відреагував. Яке право дитини порушено?",
]

situations_name_text_map = {}
for index in situations_index_name_map.keys():
    situations_name_text_map[situations_index_name_map[index]] = situations_texts[index]

rightToLive = 'Право на життя'
rightToBeLiveAndHealthy = 'Право на життя та здоров\'я'
rightForEducation = 'Право на освіту'
rightForSelfIdentification = 'Неповноцінна в розумовому або фізичному відношенні дитина має право вести повноцінне і достатнє життя.'
rightForInformation = 'Право на інформацію'
rightForLeisure = 'Право на дозвілля і відпочинок'
rightForCommunication = 'Право на спілкування'
rightForSympathy = 'Право на співчуття'
rightForHealthcare = 'Право на медичну допомогу'
rightForSpecialProtection = 'Право на особливий захист і допомогу'
rightForDignifiedTreatment = 'Право на гідне ставлення, усі рівні'
rightForFavoriteSports = 'Право займатись улюбленим спортом'
rightForPeerInteraction = 'Право на спілкування з однолітками'
rightForNoCruelPunishment = 'Заборона піддавати дитину жорстоким або принижуючим гідність покаранням'
rightForLoveAndCare = 'Право на любов та піклування'
rightForSafeLivingConditions = 'Належні та безпечні умови життя'
rightForSafety = 'Право на безпеку'
rightForTemporaryProtection = 'Дитина, яка тимчасово позбавлена сімейного оточення, має право на особливий захист і допомогу з боку держави'
rightForWork = 'Право на працю'
rightForProtectionFromExploitation = 'Захист від економічної експлуатації та виконання будь-якої роботи, що може являти небезпеку здоров\'ю'
rightForNoChildLabor = 'Заборона застосовування праці неповнолітніх на важких, підземних роботах, мінімальний вік прийому на роботу'
rightForNoHumanTrafficking = 'Заборона торгівлі людьми, дітьми'
rightForFamily = 'Право на сім\'ю'
rightForPhysicalAndMentalHealth = 'Право на повноцінний фізичний розвиток та духовне здоров\'я'
rightForPreventingAbduction = 'Відвернення викрадення дітей, торгівлі дітьми чи їх контрабанда у будь-яких цілях'
rightToKnowBiologicalParents = 'Право дитини знати біологічних батьків'
rightToNotBeDividedWithParents = 'Право дитини не розлучатись з батьками всупереч їх бажанням'
rightForProtectionFromViolence = 'Право на захист від насильства'
dutyToPrioritizeBestInterest = 'Обов\'язок держави першочергову увагу приділяти якнайкращому забезпеченню прав дитини'


rightAnswerText = 'Все вірно'
wrongAnswerText = 'Неправильно. Правильна відповідь - '

situations_name_answer_map = {
    situations_index_name_map[0]: rightToLive,
    situations_index_name_map[1]: rightForEducation,
    situations_index_name_map[2]: rightForHealthcare,
    situations_index_name_map[3]: rightForInformation,
    situations_index_name_map[4]: rightForDignifiedTreatment,
    situations_index_name_map[5]: rightToBeLiveAndHealthy,
    situations_index_name_map[6]: rightForNoCruelPunishment,
    situations_index_name_map[7]: dutyToPrioritizeBestInterest,
    situations_index_name_map[8]: rightForNoChildLabor,
    situations_index_name_map[9]: rightForNoHumanTrafficking,
    situations_index_name_map[10]: rightForPreventingAbduction,
}


answersMarkup = {}
for situation_index, situation_name_for_cycle in situations_index_name_map.items():
    answersMarkup[situation_name_for_cycle] = types.ReplyKeyboardMarkup()
    if situation_index == 0:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightToLive), types.KeyboardButton(rightForEducation))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForSelfIdentification), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 1:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForEducation), types.KeyboardButton(rightForLeisure))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForCommunication), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 2:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForSympathy), types.KeyboardButton(rightForHealthcare))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForSpecialProtection), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 3:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForEducation), types.KeyboardButton(rightForCommunication))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForInformation), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 4:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForDignifiedTreatment), types.KeyboardButton(rightForFavoriteSports))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForPeerInteraction), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 5:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForSafety), types.KeyboardButton(rightToBeLiveAndHealthy))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForLeisure), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 6:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForNoCruelPunishment), types.KeyboardButton(rightForLoveAndCare))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForSafeLivingConditions), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 7:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(dutyToPrioritizeBestInterest), types.KeyboardButton(rightToNotBeDividedWithParents))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForTemporaryProtection), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 8:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForWork), types.KeyboardButton(rightForProtectionFromExploitation))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForNoChildLabor), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 9:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForNoHumanTrafficking), types.KeyboardButton(rightForFamily))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightForPhysicalAndMentalHealth), types.KeyboardButton(backToMainMenuButtonText))
    elif situation_index == 10:
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightToLive), types.KeyboardButton(rightForPreventingAbduction))
        answersMarkup[situation_name_for_cycle].row(types.KeyboardButton(rightToKnowBiologicalParents), types.KeyboardButton(backToMainMenuButtonText))

situationsMarkup = types.ReplyKeyboardMarkup()
for situation in situations_index_name_map.values():
    situationsMarkup.add(types.KeyboardButton(situation))
situationsMarkup.add(types.KeyboardButton(backToMainMenuButtonText))


@bot.message_handler(commands=[startCommand])
def bot_start(message):
    bot.send_message(message.chat.id, 'Вітаю, ' + message.from_user.first_name, reply_markup=mainMenuMarkup)
    save_log_with_data(message)


@bot.message_handler(commands=[helpCommand])
def bot_help(message):
    bot.send_message(message.chat.id, 'Обери один з варіантів нижче', reply_markup=mainMenuMarkup)
    save_log_with_data(message)


@bot.message_handler(commands=[testCommand])
def bot_help(message):
    bot.send_message(message.chat.id, 'Id:' + str(message.from_user.id))
    save_log_with_data(message)


@bot.message_handler()
def on_click(message):
    if message.text == backToMainMenuButtonText:
        bot.send_message(message.chat.id, 'Вітаю, ' + message.from_user.first_name, reply_markup=mainMenuMarkup)
    elif message.text == weHaveRightsButtonText:
        bot.send_message(message.chat.id, weHaveRightsText)
    elif message.text == UNConventionButtonText:
        bot.send_message(message.chat.id, UNConventionText)
    elif message.text == ChildrenRightsAccordingToUNButtonText:
        file = open('./' + ChildrenRightsAccordingToUNFileName, 'rb')
        bot.send_document(message.chat.id, file)
    elif message.text == CheckYourselfButtonText:
        bot.send_message(message.chat.id, CheckYourselfText)
    elif message.text == DoYouKnowYourRightsButtonText:
        bot.send_message(message.chat.id, DoYouKnowYourRightsText)
    elif message.text == RealLifeSituationsButtonText:
        bot.send_message(message.chat.id, RealLifeSituationsText, reply_markup=situationsMarkup)
    elif message.text in situations_index_name_map.values():
        situation_name = message.text
        bot.send_message(message.chat.id, situations_name_text_map[situation_name], reply_markup=answersMarkup[situation_name])
        bot.register_next_step_handler(message, situation_check, situation_name)
    save_log_with_data(message)


def situation_check(message, situation_name):
    right_answer = situations_name_answer_map[situation_name]

    if right_answer == '':
        bot.send_message(message.chat.id, 'Сталася якась помилка. Обери ситуацію ще раз.')
    elif message.text == right_answer:
        bot.send_message(message.chat.id, rightAnswerText)
    else:
        bot.send_message(message.chat.id, wrongAnswerText + situations_name_answer_map[situation_name])
    bot.send_message(message.chat.id, RealLifeSituationsText, reply_markup=situationsMarkup)
    send_message_to_admin(message, situation_name, right_answer)


def send_message_to_admin(message, situation_name, right_answer):
    admin_id = secret.sendResultsTo
    message_date = datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S')

    message_text = str(message_date) + '\n'
    message_text += message.from_user.first_name
    if message.from_user.last_name is not None:
        message_text += ' ' + message.from_user.last_name
    message_text += ' [user_id: ' + str(message.from_user.id) + '] відповів:\n'
    message_text += situation_name + ' - ' + message.text
    message_text += '\nПравильна відповідь:\n'
    message_text += situation_name + ' - ' + right_answer
    bot.send_message(admin_id, message_text)
    save_log(message_text)


def save_log_with_data(message):
    message_date = datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S')
    message_text = str(message_date) + '\n'
    message_text += message.from_user.first_name
    if message.from_user.last_name is not None:
        message_text += ' ' + message.from_user.last_name
    message_text += ' [user_id: ' + str(message.from_user.id) + '] wrote:\n'
    message_text += message.text
    save_log(message_text)


def save_log(log_message):
    file_name = "log.txt"
    print(log_message)
    with open(file_name, "r", encoding="utf-8") as file:
        existing_content = file.read()
    with open(file_name, "w", encoding="utf-8") as file:
        full_log_message = ''
        full_log_message += "Log message:\n"
        full_log_message += log_message
        full_log_message += "\n\n"
        file.write(full_log_message + existing_content)


bot.infinity_polling()
