import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import keyboards
import lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8_neg_sub, lesson9_mix, lesson10_to_be, lesson11_to_be

import config

TOKEN = config.TOKEN

STATE = None


def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f"Hey {first_name}! Let's start!")
    what_topic_message(update, context)


def what_topic_message(update, context):
    global STATE
    STATE = 4
    update.message.reply_text('What topic?', reply_markup=keyboards.reply_markup_main)


def choose_topic(update, context):
    global STATE
    topic = update.message.text
    if topic == "Simple tenses":
        update.message.reply_text('What lesson?', reply_markup=keyboards.reply_markup_simple)
        STATE = "Simple tenses"
    elif topic == "Negative and subject questions":
        update.message.reply_text('What lesson?', reply_markup=keyboards.reply_markup_neg_sub)
        STATE = "Negative and subject questions"
    elif topic == "Mixed sentences":
        update.message.reply_text('What lesson?', reply_markup=keyboards.reply_markup_mixed_sentences)
        STATE = "Mixed sentences"
    elif topic == "To be":
        update.message.reply_text('What lesson?', reply_markup=keyboards.reply_markup_to_be)
        STATE = "To be"
    else:
        update.message.reply_text("Sorry. I can't find it")
        what_topic_message(update, context)


def creating_lesson_simple(update, context):
    global STATE, dictionary, i, key_list
    lesson_number = update.message.text
    if lesson_number == "Lesson 1":
        dictionary = lesson1.d
        key_list = list(dictionary.keys())
        showing_questions(update, key_list)
    elif lesson_number == "Lesson 2":
        dictionary = lesson2.d
        key_list = list(dictionary.keys())
        showing_questions(update, key_list)
    elif lesson_number == "Lesson 3":
        dictionary = lesson3.d
        key_list = list(dictionary.keys())
        showing_questions(update, key_list)
    elif lesson_number == "Lesson 4":
        dictionary = lesson4.d
        key_list = list(dictionary.keys())
        showing_questions(update, key_list)
    elif lesson_number == "Lesson 5":
        dictionary = lesson5.d
        key_list = list(dictionary.keys())
        showing_questions(update, key_list)
    elif lesson_number == "Lesson 6":
        dictionary = lesson6.d
        key_list = list(dictionary.keys())
        showing_questions(update, key_list)
    elif lesson_number == "Lesson 7":
        dictionary = lesson7.d
        key_list = list(dictionary.keys())
        showing_questions(update, key_list)
    elif lesson_number == "Back":
        what_topic_message(update, context)
    else:
        update.message.reply_text("Sorry. I can't find it. Try again please.")
        update.message.text = "Simple tenses"
        choose_topic(update, context)


def creating_lesson_neg_sub(update, context):
    global STATE, dictionary, i, key_list

    lesson_number = update.message.text

    if lesson_number == "Lesson 1":
        dictionary = lesson8_neg_sub.d
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Lesson 2":
        dictionary = lesson8_neg_sub.d_2
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Back":
        what_topic_message(update, context)
    else:
        update.message.reply_text("Sorry. I can't find it. Try again please.")
        update.message.text = "Negative and subject questions"
        choose_topic(update, context)


def creating_lesson_mix(update, context):
    global STATE, dictionary, i, key_list

    lesson_number = update.message.text

    if lesson_number == "Lesson 1":
        dictionary = lesson9_mix.d
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Lesson 2":
        dictionary = lesson9_mix.d_2
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Back":
        what_topic_message(update, context)
    else:
        update.message.reply_text("Sorry. I can't find it. Try again please.")
        update.message.text = "Mixed sentences"
        choose_topic(update, context)


def creating_lesson_to_be(update, context):
    global STATE, dictionary, i, key_list

    lesson_number = update.message.text

    if lesson_number == "Lesson 1":
        dictionary = lesson10_to_be.d
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Lesson 2":
        dictionary = lesson10_to_be.d_2
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Lesson 3":
        dictionary = lesson11_to_be.d
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Lesson 4":
        dictionary = lesson11_to_be.d_2
        key_list = list(dictionary.keys())
        showing_questions(update, context)
    elif lesson_number == "Back":
        what_topic_message(update, context)
    else:
        update.message.reply_text("Sorry. I can't find it. Try again please.")
        update.message.text = "To be"
        choose_topic(update, context)


def showing_questions(update, context):
    global STATE, i, key_list
    if key_list:
        i = random.choice(key_list)
        update.message.reply_text(i)
        STATE = 3
    else:
        update.message.reply_text('Congrats!\nThe test has been passed')
        STATE = None


def checking_answers(update, context):
    global STATE, dictionary, i, key_list

    answer = update.message.text

    lower_example = []
    [lower_example.append(element.lower()) for element in dictionary.get(i)]

    if answer.lower() in lower_example:
        update.message.reply_text('Correct')
        key_list.remove(i)
        update.message.reply_text(len(key_list))
    else:
        update.message.reply_text('Incorrect')
        a = dictionary.get(i)
        update.message.reply_text(f'"{a[0]}"' if len(a) == 1 else f'"{a[0]}" or "{a[1]}"')

    showing_questions(update, context)


# function to handle the /help command
def help(update, context):
    update.message.reply_text('help command received')


# function to handle errors occurred in the dispatcher
def error(update, context):
    update.message.reply_text('An error occurred')


# function to handle normal text
def text(update, context):
    global STATE
    if STATE == "Simple tenses":
        return creating_lesson_simple(update, context)
    elif STATE == "Negative and subject questions":
        return creating_lesson_neg_sub(update, context)
    elif STATE == "Mixed sentences":
        return creating_lesson_mix(update, context)
    elif STATE == "To be":
        creating_lesson_to_be(update, context)
    elif STATE == 2:
        return showing_questions(update, context)
    elif STATE == 3:
        return checking_answers(update, context)
    elif STATE == 4:
        return choose_topic(update, context)
    elif STATE == 5:
        return what_topic_message(update, context)


def main():
    # the updater, that will automatically create also a dispatcher and queue to make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    # add an handler for errors
    dispatcher.add_error_handler(error)
    # start your shiny new bot
    updater.start_polling()
    # go the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
