from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler
import logging
import os

# Configuração do logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Obtenha o token do ambiente ou de um arquivo de configuração externo
TOKEN = os.getenv("6324283139:AAFF-W5yIPzTbDEdLIhXTFB9P_4ppbR2ggM")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Este é o seu bot.')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Eu sou um bot simples. Como posso ajudar você?')

def inline_query(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query

    # Processa a consulta e obtém resultados
    results = [
        InlineQueryResultArticle(
            id='1',
            title='Título do Resultado',
            input_message_content=InputTextMessageContent('Conteúdo do Resultado'),
        ),
        # Adicione mais resultados conforme necessário
    ]

    # Envia os resultados da consulta
    update.inline_query.answer(results)

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # Adiciona os manipuladores de comando
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("hello", hello))

    # Adiciona o manipulador de consulta inline
    dp.add_handler(InlineQueryHandler(inline_query))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
    
