from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choose = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="🎣 Get info about trade-pair",
                                          callback_data="trade-pair"
                                      )
                                  ],
                              ])

cancel = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Cancel",
                                          callback_data="cancel"
                                      )
                                  ]
                              ])
