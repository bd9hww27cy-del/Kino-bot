import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@reklamauz_11"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = await context.bot.get_chat_member(CHANNEL, update.effective_user.id)

    if user.status in ["member", "administrator", "creator"]:
        await update.message.reply_text(
            "🎬 Kino kodini yuboring.\n\nMasalan: 123"
        )
    else:
        await update.message.reply_text(
            "❗ Avval kanalga obuna bo‘ling:\n"
            "https://t.me/reklamauz_11\n\n"
            "Keyin /start ni qayta bosing."
        )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()

    await update.message.reply_text(
        f"🎬 {code} kodi qabul qilindi.\n"
        "Hozircha bu kod uchun kino biriktirilmagan."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    app.run_polling()

if __name__ == "__main__":
    main()
