from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

# Função para /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou um bot divertido. Use /poema para criar poemas ou outros comandos para explorar mais!")

# Função para /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Comandos disponíveis:
/start - Inicia o bot
/help - Lista os comandos disponíveis
/poema - Gera um poema aleatório
    """)

# Função principal do comando /poema
async def poema(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poemas = [
        "Nas sombras do cosmos, a eternidade passa,\nA solidão ecoa, mas o espírito não fracassa.",
        "Os mundos giram como histórias sem fim,\nCada estrela, um novo começo para mim.",
        "Ao céu escuro dou meu olhar,\nProcurando redenção onde o amor possa estar.",
        "Caminhei por terras que o tempo esqueceu,\nAinda buscando algo que sempre foi meu."
    ]
    poema_escolhido = random.choice(poemas)
    await update.message.reply_text(f"Eis seu poema:\n\n{poema_escolhido}")

# Função principal para inicializar o bot
def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")  # O token vem das variáveis de ambiente
    if not token:
        raise RuntimeError("O token do bot não foi configurado corretamente.")

    application = ApplicationBuilder().token(token).build()

    # Handlers dos comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("poema", poema))

    # Roda o bot
    print("Bot está rodando...")
    application.run_polling()  # NÃO precisa ser await ou estar dentro de asyncio.run()

if __name__ == "__main__":
    main()
