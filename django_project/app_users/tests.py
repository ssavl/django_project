from django.test import TestCase

# Create your tests here.

# quest = ['Кто для тебя авторитет и почему? \n \nWho is your authority? And why?', 'Какие твои языки любви (подарки, помощь, слова, прикосновения, время)? \n \nWhat are your love languages (presents, help, words, touch, time)?', 'Каким был лучший день твоей жизни? Почему ты так считаешь? \n \nWhat was the best day of your life? Why do you think so?', 'Знают ли люди, которых ты любишь больше всего, как ты их любишь? \n \nDo people you love most know how much you love them? Sure?', 'Учитывая твою нынешнюю повседневную жизнь, чего ты рассчитываешь добиться через пять лет? \n \nGiven your current daily life what do you expect to achieve in five years?', 'Удовлетворен ли ты глубиной своих отношений с людьми? \n \nAre you satisfied with the depth of your relations with people?', 'Сколько часов в день/неделю ты проводишь в интернете? \n \nHow many hours a day/week do you spend online?', 'Каковы твои самые распространенные негативные мысли? Есть ли в них логика? \n \nWhat are your most common negative thoughts? Do they have logic?', 'Считаешь ли ты, что за некоторые вещи тебе уже поздно браться? Почему? \n \nDo you think its too late for you to take on some things? Why?', 'Если бы ты мог стать самым влиятельным человеком в мире, что бы ты изменил? \n \nIf you could become the most powerful person in the world, what would you change?', 'Как часто ты делишься чем-то, не ожидая получить что-то в ответ? \n \nHow often do you share something without expecting to get something back?', 'Каков главный вызов в твоей жизни? \n \nWhat is the main challenge in your life?', 'Как ты мог бы упростить свою жизнь и сосредоточиться на самом важном? \n \nHow could you simplify your life and focus on the most important things?', 'Что вызывает у тебя стресс? \n \nWhat causes your stress?', 'Что делает твою жизнь проще? \n \nWhat does make your life easier?', 'Что самое главное для тебя в жизни? Уделяешь ли ты этому достаточно времени? \n \nWhat is the most important thing in your life? Do you spend enough time on it?', 'Осложняют ли твою жизнь вещи, в которых нет необходимости? \n \nDo things that arent necessary make your life difficult?', 'Если бы ты мог отправить всему миру послание, что бы ты сказал за 30 секунд? \n \nIf you could send a message to the world, what would you say (you have only 30 seconds)?', 'Часто ли ты говоришь «да», хотя на самом деле хочешь сказать «нет»? Почему? \n \nHow often do you say «yes» when you really want to say «no»? Why?', 'О чем ты никому не рассказываешь и очень сожалеешь об этом? \n \nWhat you dont tell anyone and youre very sorry about it?', 'Назвал бы ты себя щедрым человеком? \n \nWould you call yourself a generous person?', 'Боишься ли ты выражать собственное мнение? \n \nAre you afraid to express your own opinion?', 'Бывает ли, что в разговоре ты только делаешь вид, что «слушаешь»? Как часто? \n \nDoes it happen that in a conversation you only pretend to «listen»? How often?', 'Не слишком ли часто ты поддаешься на уговоры других, а потом чувствуешь обиду и сожаление? \n \nDont you often give in to the persuasions of others, and then feel resentment and regret?', 'Что самое главное, что тебе нужно изменить в своей жизни в этом году? \n \nThe main thing you have to change in your life this year for yourself', 'Как часто ты отделываешься от других оправданиями? \n \nHow often do you get rid of others with excuses?', 'Сколько времени ты проводишь с семьей и друзьями? \n \nHow much time do you spend with your family and friends?', 'Что стоит между тобой и твоей самой главной целью? Дай ответ одним словом \n \nWhat stands between you and your most important goal? give the answer in one word', 'Если бы ты мог пригласить кого-нибудь на ужин (близкого человека, умершего родственника, знаменитость), кого бы ты выбрал? \n \nIf you could invite someone to dinner (a loved one, a deceased relative, a celebrity), who would you choose?', 'Прежде чем сделать звонок, тебе случается репетировать свою реплику? \n \nDo you rehearse your line before calling?', 'Хотел бы ты быть знаменитым? В чем? \n \nWould you like to be famous? By what?', 'Каким был бы для тебя «идеальный день»? \n \nDescribe your perfect day', 'У тебя есть тайное предчувствие того, как ты умрешь? \n \nDo you have a secret premonition about your death?', 'Когда ты в последний раз пел в одиночестве? \n \nWhen was the last time when you were singing alone?', 'Если бы ты мог прожить до 90 лет и в последние 60 лет сохранить либо разум, либо тело 30-летнего, что бы ты выбрал? \n \nIf you could live to be 90 and in the last 60 years keep either the mind or body of a thirty-year-old, what would you choose?', 'За 3 минуты расскажи историю своей жизни настолько подробно, насколько это возможно. \n \nTell the story of your life with as much details, as possible. You have only 3 minutes.', 'Если бы ты мог проснуться завтра, обладая каким-то умением или способностью, что бы это было? \n \nWhat skill or ability would you choose if you could?', 'Если бы магический кристалл мог открыть тебе правду, о чем бы ты хотел узнать? \n \nWhat would you want to know if there was a crystal which reveals the truth?', 'Есть ли что-то, что ты уже давно мечтаешь сделать? Почему ты еще не сделал этого? \n \nIs there something you’ve been dreaming to do for a long time? Why haven’t you done it?', 'Какое твое самое ужасное воспоминание? \n \nThe most terrible memory in your life.', 'Каково наибольшее достижение твоей жизни? \n \nWhat is the biggest achievement in your life?', 'Какое твое самое дорогое воспоминание? \n \nThe most precious memory in your life.', 'Назови твою самую характерную черту. \n \nName one your characteristic.', 'Если бы ты знал, что умрешь через год, что бы ты изменил в том, как живешь? Почему? \n \nImagine that this year is the last for you. What would you change in your life then? Why?', 'Какое у тебя любимое занятие? \n \nYour favourite activity', 'Что для тебя значит дружба? \n \nWhat is the meaning of friendship for you?', 'Что ты считаешь самым большим несчастьем? \n \nThat is the biggest misfortune in your opinion?', 'Назови по одному положительному качеству каждого из участников (желательно не самые очевидные) \n \nName one positive quality for each to the participants', 'В какой стране ты хотел бы жить? \n \nWhat country would you like to live in?', 'Продолжи фразу: «Я бы хотел, чтобы был кто-то, с кем можно разделить…» \n \nContinue the sentence: «I would like to have someone to share ……. with»', 'Какой ваш любимый цвет? \n\nYour favourite colour', 'Когда ты в последний раз плакал при ком-нибудь? А в одиночестве? \n \nWhen was the last time when you cried in front of someone? And alone?', 'Твой любимый цветок \n \nYour favourite flower', 'Если бы ты должен был умереть сегодня до конца дня, ни с кем не поговорив, о чем несказанном ты бы больше всего жалел? Почему ты еще не сказал этого? \n \nImagine that you should die today. And you can’t talk with anyone. What didn’t you say you’ll be most sorry for? Why haven’t you told it yet?', 'Каково твое состояние духа в настоящий момент? \n \nHow are you doing now?', 'Какой ты персонаж из мультфильма? И почему? \n \nWho are you from the cartoon characters? And why?', 'Каков твой девиз? \n \nWhat is your motto?', 'О чем ты мечтаешь? \n \nWhat do you dream about?', 'Какова самая мудрая мысль, которую ты когда-либо слышал? \n \nWhat is the wisest thought you have ever heard?', 'Что тебя раздражает? \n \nWhat does annoy you?', 'Если бы тебе осталось жить год, чего бы ты попытался достичь? \n \nImagine that you have only a year to live. What would you try to achieve?', 'Что ты больше всего ценишь в своих друзьях? \n \nWhat do you appreciate the most in your friends?', 'За что ты благодарен (в целом или конкретно сейчас)? \n \nWhat are you grateful for (in general or right now)?']
# quest.remove('\n')
# print(quest)