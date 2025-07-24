import os
import telebot
from telebot import types

# 🔐 Pega o token do ambiente (definido no Railway)
TOKEN = '7634578800:AAGZ1gnc_lR4U4n1qiOPpQHgDxirBT1UYN4'
bot = telebot.TeleBot(TOKEN)

# 📋 Lista de botões com nomes e comandos
comandos = [
    ("YT Premium", "/ytpremium"),
    ("Paramount", "/paramount"),
    ("Crunchyroll", "/crunchyroll"),
    ("Prime Video", "/primevideo"),
    ("Viki Rakuten Plus", "/vikirakutenplus"),
    ("Duolingo", "/duolingo"),
    ("Kocowa", "/kocowa")
]

# 📥 Mensagem inicial com botões
@bot.message_handler(commands=['start'])
def boas_vindas(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    botoes = [types.InlineKeyboardButton(text=nome, callback_data=comando) for nome, comando in comandos]
    markup.add(*botoes)

    msg = "🎉 *BEM-VINDO AO GERADOR DE STREAMING PREMIUM JETFLIX!*\n\n"
    msg += "Clique em um dos serviços abaixo para receber acesso 👇"

    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='Markdown')

# 📦 Resposta para cada botão
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        bot.answer_callback_query(call.id, text="🔄 Processando...")
    except:
        pass

    nome_servico = call.data[1:]

    if nome_servico == "ytpremium":
        resposta = (
            "📺 *YT Premium*\n"
            "Login: jetflixofx@gmail.com\n"
            "Senha: Ema@2025\n"
            "✅ YouTube Premium disponível"
        )
    elif nome_servico == "paramount":
        resposta = (
            "🎞️ *Paramount*\n"
            "Login: jetflixofx@gmail.com\n"
            "Senha: Gcay1234\n"
            "📅 Plano ativo"
        )
    elif nome_servico == "crunchyroll":
        resposta = (
            "🍣 *Crunchyroll*\n"
            "Login: 1703fdf1ff41239ac08d0c7390ca6937@firemail.com.br\n"
            "Senha: 1703fdf1ff41239ac08d0c7390ca6937@firemail.com.br\n"
            "✅ Acesso à animação ilimitada"
        )
    elif nome_servico == "primevideo":
        resposta = (
            "🎬 *Prime Vídeo*\n"
            "Login: jetflixofx@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Plano familiar disponível"
        )
    elif nome_servico == "vikirakutenplus":
        resposta = (
            "📺 *Viki Rakuten Plus*\n"
            "Login: fada91fe2c2da10cf53636494c62b71f@firemail.com.br\n"
            "Senha: fada91fe2c2da10cf53636494c62b71f@firemail.com.br\n"
            "✅ Acesso completo"
        )
    elif nome_servico == "duolingo":
        resposta = (
            "📚 *Duolingo*\n"
            "Login: fada91fe2c2da10cf53636494c62b71f@firemail.com.br\n"
            "Senha: fada91fe2c2da10cf53636494c62b71f@firemail.com.br\n"
            "✅ Acesso a cursos premium"
        )
    elif nome_servico == "kocowa":
        resposta = (
            "📺 *Kocowa*\n"
            "Login: fada91fe2c2da10cf53636494c62b71f@firemail.com.br\n"
            "Senha: Xinespreto123@\n"
            "✅ Acesso a dramas asiáticos"
        )
    else:
        resposta = f"🔐 Gerando conta para: *{nome_servico.upper()}*..."

    bot.send_message(call.message.chat.id, resposta, parse_mode='Markdown', disable_web_page_preview=True)

# ▶️ Iniciar o bot
print("🤖 Bot rodando...")
bot.polling(none_stop=True)
