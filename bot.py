from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Вставьте свой токен
TOKEN = "7256588032:AAG4Jtw5a3APVHzXpnAM6olC1x0otvmDHEE"

# Вставьте ID вашего канала
CHANNEL_ID_1 = "@anonimchat208"  # Замените на ваш идентификатор канала
CHANNEL_ID_2 = "@school208admin"

# Список для хранения сообщений анонимно
messages = []


# Функция, которая срабатывает при старте бота
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Отправьте ваше сообщение, и я перешлю его анонимно.")

# Функция, которая обрабатывает текстовые сообщения
async def handle_message(update: Update, context: CallbackContext) -> None:
    # Сохраняем сообщение в список
    message_meta = {
        "text": update.message.text,
        "username": update.message.chat.username
    }
    messages.append(message_meta["text"])
    messages.append(message_meta["username"])
    
    
    # Пересылаем сообщение в канал
    await context.bot.send_message(chat_id=CHANNEL_ID_2, text=f"Отправил: {message_meta['username']}\nСообщение: {message_meta['text']}")
    await context.bot.send_message(chat_id=CHANNEL_ID_1, text=f"{message_meta['text']}")

    await update.message.reply_text("Ваше сообщение отправлено анонимно!")
# Функция, которая выводит все сообщения
async def show_messages(update: Update, context: CallbackContext) -> None:
    if messages:
        for i, msg in enumerate(messages, 1):
            await update.message.reply_text(f"Сообщение {i}: {msg}")
    else:
        await update.message.reply_text("Нет сообщений.")

# Основная логика для запуска бота
def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем хендлеры
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("show", show_messages))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()

    

if __name__ == '__main__':
    main()
    
    
