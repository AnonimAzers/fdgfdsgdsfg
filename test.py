from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from pyrogram.handlers import MessageHandler
from pyrogram import filters
import asyncio

class Menu:
    async def button_callback(self, client, message):
        text = message.text
        if text in self._menu_button_handlers:
            await self._menu_button_handlers[text](self, message)

    def __init__(self, _menu_button_handlers, _menu_keyboard, client, message):
        self.menu_button_handlers = _menu_button_handlers
        self._menu_keyboard = _menu_keyboard
        self.client = client
        client.add_handler(MessageHandler(self.button_callback, filters.text & filters.private))


class MeinMenu(Menu):

    _menu_button_handlers = {
        "🖥 Просмотры": lambda self, message: message.reply("Вы выбрали просмотры", reply_markup=ViewSettingsMenu(self.client, message)._menu_keyboard),
        "↩️ Переход": lambda self, message: message.reply("Вы выбрали Переход", reply_markup=TransitionSettingsMenu(self.client, message)._menu_keyboard),
        "⛔️ Жалобы": lambda self, message: message.reply("Вы выбрали Жалобы", reply_markup=ReportSettingsMenu(self.client, message)._menu_keyboard),
        "📢 Опрос": lambda self, message: message.reply("Вы выбрали Опрос", reply_markup=SurveySettingsMenu(self.client, message)._menu_keyboard),
        "❤️ Реакции": lambda self, message: message.reply("Вы выбрали Реакции", reply_markup=ReactionSettingsMenu(self.client, message)._menu_keyboard),
        "🗑 Удалить": lambda self, message: message.reply("Вы выбрали Удалить", reply_markup=RemoveSettingsMenu(self.client, message)._menu_keyboard)
    }

    _menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("🖥 Просмотры"), KeyboardButton("↩️ Переход")],
        [KeyboardButton("⛔️ Жалобы"), KeyboardButton("📢 Опрос")],
        [KeyboardButton("❤️ Реакции"), KeyboardButton("🗑 Удалить")]
    ], resize_keyboard=True, one_time_keyboard=True, placeholder="Press any button!")

    def __init__(self, client, message):
        super().__init__(MeinMenu._menu_button_handlers, MeinMenu._menu_keyboard, client, message)

class ViewSettingsMenu(Menu):
    _menu_button_handlers = {
        "🖥 Просмотры": lambda self, message: message.reply("Вы выбрали просмотры", reply_markup=ViewSettingsMenu(self.client, message)._menu_keyboard),
        "↩️ Переход": lambda self, message: message.reply("Вы выбрали Переход", reply_markup=TransitionSettingsMenu(self.client, message)._menu_keyboard),
        "⛔️ Жалобы": lambda self, message: message.reply("Вы выбрали Жалобы", reply_markup=ReportSettingsMenu(self.client, message)._menu_keyboard),
        "📢 Опрос": lambda self, message: message.reply("Вы выбрали Опрос", reply_markup=SurveySettingsMenu(self.client, message)._menu_keyboard),
        "❤️ Реакции": lambda self, message: message.reply("Вы выбрали Реакции", reply_markup=ReactionSettingsMenu(self.client, message)._menu_keyboard),
        "🗑 Удалить": lambda self, message: message.reply("Вы выбрали Удалить", reply_markup=RemoveSettingsMenu(self.client, message)._menu_keyboard)
    }

    _menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("🖥 Просмотры"), KeyboardButton("↩️ Переход")],
        [KeyboardButton("⛔️ Жалобы"), KeyboardButton("📢 Опрос")],
        [KeyboardButton("❤️ Реакции"), KeyboardButton("🗑 Удалить")]
    ], resize_keyboard=True, one_time_keyboard=True, placeholder="Press any button!")

    def __init__(self, client, message):
        super().__init__(ViewSettingsMenu._menu_button_handlers, ViewSettingsMenu._menu_keyboard, client, message)

class TransitionSettingsMenu(Menu):
    _menu_button_handlers = {
        "🖥 Просмотры": lambda self, message: message.reply("Вы выбрали просмотры", reply_markup=ViewSettingsMenu(self.client, message)._menu_keyboard),
        "↩️ Переход": lambda self, message: message.reply("Вы выбрали Переход", reply_markup=TransitionSettingsMenu(self.client, message)._menu_keyboard),
        "⛔️ Жалобы": lambda self, message: message.reply("Вы выбрали Жалобы", reply_markup=ReportSettingsMenu(self.client, message)(self.client, message)._menu_keyboard),
        "📢 Опрос": lambda self, message: message.reply("Вы выбрали Опрос", reply_markup=SurveySettingsMenu(self.client, message)._menu_keyboard),
        "❤️ Реакции": lambda self, message: message.reply("Вы выбрали Реакции", reply_markup=ReactionSettingsMenu(self.client, message)._menu_keyboard),
        "🗑 Удалить": lambda self, message: message.reply("Вы выбрали Удалить", reply_markup=RemoveSettingsMenu(self.client, message)._menu_keyboard)
    }

    _menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("🖥 Просмотры"), KeyboardButton("↩️ Переход")],
        [KeyboardButton("⛔️ Жалобы"), KeyboardButton("📢 Опрос")],
        [KeyboardButton("❤️ Реакции"), KeyboardButton("🗑 Удалить")]
    ], resize_keyboard=True, one_time_keyboard=True, placeholder="Press any button!")

    def __init__(self, client, message):
        super().__init__(TransitionSettingsMenu._menu_button_handlers, TransitionSettingsMenu._menu_keyboard, client, message)

class ReportSettingsMenu(Menu):
    _menu_button_handlers = {
        "🖥 Просмотры": lambda self, message: message.reply("Вы выбрали просмотры", reply_markup=ViewSettingsMenu(self.client, message)._menu_keyboard),
        "↩️ Переход": lambda self, message: message.reply("Вы выбрали Переход", reply_markup=TransitionSettingsMenu(self.client, message)._menu_keyboard),
        "⛔️ Жалобы": lambda self, message: message.reply("Вы выбрали Жалобы", reply_markup=ReportSettingsMenu(self.client, message)._menu_keyboard),
        "📢 Опрос": lambda self, message: message.reply("Вы выбрали Опрос", reply_markup=SurveySettingsMenu(self.client, message)._menu_keyboard),
        "❤️ Реакции": lambda self, message: message.reply("Вы выбрали Реакции", reply_markup=ReactionSettingsMenu(self.client, message)._menu_keyboard),
        "🗑 Удалить": lambda self, message: message.reply("Вы выбрали Удалить", reply_markup=RemoveSettingsMenu(self.client, message)._menu_keyboard)
    }

    _menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("🖥 Просмотры"), KeyboardButton("↩️ Переход")],
        [KeyboardButton("⛔️ Жалобы"), KeyboardButton("📢 Опрос")],
        [KeyboardButton("❤️ Реакции"), KeyboardButton("🗑 Удалить")]
    ], resize_keyboard=True, one_time_keyboard=True, placeholder="Press any button!")

    def __init__(self, client, message):
        super().__init__(ReportSettingsMenu._menu_button_handlers, ReportSettingsMenu._menu_keyboard, client, message)

class SurveySettingsMenu(Menu):
    _menu_button_handlers = {
        "🖥 Просмотры": lambda self, message: message.reply("Вы выбрали просмотры", reply_markup=ViewSettingsMenu(self.client, message)._menu_keyboard),
        "↩️ Переход": lambda self, message: message.reply("Вы выбрали Переход", reply_markup=TransitionSettingsMenu(self.client, message)._menu_keyboard),
        "⛔️ Жалобы": lambda self, message: message.reply("Вы выбрали Жалобы", reply_markup=ReportSettingsMenu(self.client, message)._menu_keyboard),
        "📢 Опрос": lambda self, message: message.reply("Вы выбрали Опрос", reply_markup=SurveySettingsMenu(self.client, message)._menu_keyboard),
        "❤️ Реакции": lambda self, message: message.reply("Вы выбрали Реакции", reply_markup=ReactionSettingsMenu(self.client, message)._menu_keyboard),
        "🗑 Удалить": lambda self, message: message.reply("Вы выбрали Удалить", reply_markup=RemoveSettingsMenu(self.client, message)._menu_keyboard)
    }

    _menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("🖥 Просмотры"), KeyboardButton("↩️ Переход")],
        [KeyboardButton("⛔️ Жалобы"), KeyboardButton("📢 Опрос")],
        [KeyboardButton("❤️ Реакции"), KeyboardButton("🗑 Удалить")]
    ], resize_keyboard=True, one_time_keyboard=True, placeholder="Press any button!")

    def __init__(self, client, message):
        super().__init__(SurveySettingsMenu._menu_button_handlers, SurveySettingsMenu._menu_keyboard, client, message)

class ReactionSettingsMenu(Menu):
    _menu_button_handlers = {
        "🖥 Просмотры": lambda self, message: message.reply("Вы выбрали просмотры", reply_markup=ViewSettingsMenu(self.client, message)._menu_keyboard),
        "↩️ Переход": lambda self, message: message.reply("Вы выбрали Переход", reply_markup=TransitionSettingsMenu(self.client, message)._menu_keyboard),
        "⛔️ Жалобы": lambda self, message: message.reply("Вы выбрали Жалобы", reply_markup=ReportSettingsMenu(self.client, message)._menu_keyboard),
        "📢 Опрос": lambda self, message: message.reply("Вы выбрали Опрос", reply_markup=SurveySettingsMenu(self.client, message)._menu_keyboard),
        "❤️ Реакции": lambda self, message: message.reply("Вы выбрали Реакции", reply_markup=ReactionSettingsMenu(self.client, message)._menu_keyboard),
        "🗑 Удалить": lambda self, message: message.reply("Вы выбрали Удалить", reply_markup=RemoveSettingsMenu(self.client, message)._menu_keyboard)
    }

    _menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("🖥 Просмотры"), KeyboardButton("↩️ Переход")],
        [KeyboardButton("⛔️ Жалобы"), KeyboardButton("📢 Опрос")],
        [KeyboardButton("❤️ Реакции"), KeyboardButton("🗑 Удалить")]
    ], resize_keyboard=True, one_time_keyboard=True, placeholder="Press any button!")

    def __init__(self, client, message):
        super().__init__(ReactionSettingsMenu._menu_button_handlers, ReactionSettingsMenu._menu_keyboard, client, message)

class RemoveSettingsMenu(Menu):
    _menu_button_handlers = {
        "🖥 Просмотры": lambda self, message: message.reply("Вы выбрали просмотры", reply_markup=ViewSettingsMenu(self.client, message)._menu_keyboard),
        "↩️ Переход": lambda self, message: message.reply("Вы выбрали Переход", reply_markup=TransitionSettingsMenu(self.client, message)._menu_keyboard),
        "⛔️ Жалобы": lambda self, message: message.reply("Вы выбрали Жалобы", reply_markup=ReportSettingsMenu(self.client, message)._menu_keyboard),
        "📢 Опрос": lambda self, message: message.reply("Вы выбрали Опрос", reply_markup=SurveySettingsMenu(self.client, message)._menu_keyboard),
        "❤️ Реакции": lambda self, message: message.reply("Вы выбрали Реакции", reply_markup=ReactionSettingsMenu(self.client, message)._menu_keyboard),
        "🗑 Удалить": lambda self, message: message.reply("Вы выбрали Удалить", reply_markup=RemoveSettingsMenu(self.client, message)._menu_keyboard)
    }

    _menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("🖥 Просмотры"), KeyboardButton("↩️ Переход")],
        [KeyboardButton("⛔️ Жалобы"), KeyboardButton("📢 Опрос")],
        [KeyboardButton("❤️ Реакции"), KeyboardButton("🗑 Удалить")]
    ], resize_keyboard=True, one_time_keyboard=True, placeholder="Press any button!")

    def __init__(self, client, message):
        super().__init__(RemoveSettingsMenu._menu_button_handlers, RemoveSettingsMenu._menu_keyboard, client, message)
