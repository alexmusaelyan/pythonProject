from telegram import KeyboardButton, ReplyKeyboardMarkup

main_keyboard = [[KeyboardButton("Simple tenses", callback_data='1')],
                 [KeyboardButton("Negative and subject questions", callback_data='2')],
                 [KeyboardButton("Mixed sentences", callback_data='3')],
                 [KeyboardButton("To be", callback_data='4')],
                 ]
reply_markup_main = ReplyKeyboardMarkup(main_keyboard, one_time_keyboard=True)

simple_tenses = [[KeyboardButton("Lesson 1", callback_data='1')],
                 [KeyboardButton("Lesson 2", callback_data='2')],
                 [KeyboardButton("Lesson 3", callback_data='3')],
                 [KeyboardButton("Lesson 4", callback_data='4')],
                 [KeyboardButton("Lesson 5", callback_data='5')],
                 [KeyboardButton("Lesson 6", callback_data='6')],
                 [KeyboardButton("Lesson 7", callback_data='7')],
                 [KeyboardButton("Back", callback_data='8')],
                 ]
reply_markup_simple = ReplyKeyboardMarkup(simple_tenses, one_time_keyboard=True)

neg_sub_keyboard = [[KeyboardButton("Lesson 1", callback_data='1')],
                    [KeyboardButton("Lesson 2", callback_data='2')],
                    [KeyboardButton("Back", callback_data='3')],
                    ]
reply_markup_neg_sub = ReplyKeyboardMarkup(neg_sub_keyboard, one_time_keyboard=True)

mixed_sentences_keyboard = [[KeyboardButton("Lesson 1", callback_data='1')],
                            [KeyboardButton("Lesson 2", callback_data='2')],
                            [KeyboardButton("Back", callback_data='3')],
                            ]
reply_markup_mixed_sentences = ReplyKeyboardMarkup(mixed_sentences_keyboard, one_time_keyboard=True)

to_be_keyboard = [[KeyboardButton("Lesson 1", callback_data='1')],
                  [KeyboardButton("Lesson 2", callback_data='2')],
                  [KeyboardButton("Lesson 3", callback_data='3')],
                  [KeyboardButton("Lesson 4", callback_data='4')],
                  [KeyboardButton("Back", callback_data='5')],
                  ]
reply_markup_to_be = ReplyKeyboardMarkup(to_be_keyboard, one_time_keyboard=True)