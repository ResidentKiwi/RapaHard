from telegram.ext import Updater, CommandHandler

# Função para lidar com o comando /hello
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Estou funcionando.")

def main():
    # Token do seu bot do Telegram
    token = '6953854001:AAEmG7hr0u9-spr-Q6-MpfHOMF1bnjdmzp0'

    # Inicializa o Updater com o token
    updater = Updater(token, use_context=True)

    # Obtém o dispatcher para registrar manipuladores
    dp = updater.dispatcher

    # Adiciona um manipulador para o comando /hello
    dp.add_handler(CommandHandler("hello", hello))

    # Inicia o bot
    updater.start_polling()

    # Aguarda o bot ser encerrado manualmente
    updater.idle()

if __name__ == '__main__':
    main()
