from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

#  Catálogo WebApp URL
CATALOGO_URL = "https://residentkiwi.github.io/catalogo-bot-telegram/"

#  Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 Abrir Catálogo", web_app=WebAppInfo(url=CATALOGO_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Olá! Seja bem-vindo(a) ao bot do Catálogo de Canais.\n\n"
        "Use o botão abaixo para acessar o catálogo:",
        reply_markup=reply_markup
    )

#  Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Lista de Comandos Disponíveis:*\n\n"
        "/start – Inicia o bot e mostra o botão do catálogo\n"
        "/help – Exibe esta mensagem de ajuda\n"
        "/poema – Gera um poema aleatório\n"
        "/catalogo – Abre o catálogo de canais via botão\n",
        parse_mode="Markdown"
    )

#  Comando /poema
async def poema(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poemas = [
        "Nas sombras do cosmos, a eternidade passa,\nA solidão ecoa, mas o espírito não fracassa.",
        "Os mundos giram como histórias sem fim,\nCada estrela, um novo começo para mim.",
        "Ao céu escuro dou meu olhar,\nProcurando redenção onde o amor possa estar.",
        "Caminhei por terras que o tempo esqueceu,\nAinda buscando algo que sempre foi meu."
    ]
    poema_escolhido = random.choice(poemas)
    await update.message.reply_text(f"📝 *Eis seu poema:*\n\n_{poema_escolhido}_", parse_mode="Markdown")

# Comando /catalogo
async def catalogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 Abrir Catálogo", web_app=WebAppInfo(url=CATALOGO_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Clique no botão abaixo para acessar o catálogo de canais:",
        reply_markup=reply_markup
    )

#  Função principal
def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("❌ Token do bot não configurado.")

    application = ApplicationBuilder().token(token).build()

    # 📌 Registra comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("poema", poema))
    application.add_handler(CommandHandler("catalogo", catalogo))

    print(" Bot está rodando...")
    application.run_polling()

# executa o bot
if __name__ == "__main__":
    main()
