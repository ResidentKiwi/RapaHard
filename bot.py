from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("O bot está em funcionamento!🏓🤓")

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Comandos disponíveis:
/start - Inicia o bot
/help - Lista os comandos disponíveis
/poema - Gera um poema aleatório
/catalogo - Acessa o catálogo de canais
    """)

# Comando /poema
async def poema(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poemas = [
        "Nas sombras do cosmos, a eternidade passa,\nA solidão ecoa, mas o espírito não fracassa.",
        "Os mundos giram como histórias sem fim,\nCada estrela, um novo começo para mim.",
        "Ao céu escuro dou meu olhar,\nProcurando redenção onde o amor possa estar.",
        "Caminhei por terras que o tempo esqueceu,\nAinda buscando algo que sempre foi meu."
    ]
    poema_escolhido = random.choice(poemas)
    await update.message.reply_text(f"Eis seu poema:\n\n{poema_escolhido}")

# ✅ Comando /catalogo com botão para WebApp
async def catalogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                text="📦 Abrir Catálogo",
                web_app=WebAppInfo(url="https://SEU-USUARIO.github.io/NOME-DO-REPO/")  # <-- Substitua pelo link real
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Clique no botão abaixo para acessar o catálogo de canais:",
        reply_markup=reply_markup
    )

# Inicializa o bot
def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("O token do bot não foi configurado corretamente.")

    application = ApplicationBuilder().token(token).build()

    # Registra comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("poema", poema))
    application.add_handler(CommandHandler("catalogo", catalogo))  # ✅ Aqui está o novo comando

    print("Bot está rodando...")
    application.run_polling()

if __name__ == "__main__":
    main()
