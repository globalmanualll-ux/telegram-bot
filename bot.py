from telegram.ext import Application, MessageHandler, filters

TOKEN = "8762962186:AAHIpWCSdrDNw51qcnjqz_dM8SJ-GcdRyw4"

message_count = 0

async def count_messages(update, context):
    global message_count

    message_count += 1

    print(f"Сообщений: {message_count}")

    if message_count % 100 == 0:
        await update.message.reply_text(
            "Test bota"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, count_messages)
)

print("Бот запущен")

app.run_polling()
