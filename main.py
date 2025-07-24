import os
import telebot
from telebot import types

# 🔐 Pega o token do ambiente (definido no Railway)
TOKEN = '7634578800:AAGZ1gnc_lR4U4n1qiOPpQHgDxirBT1UYN4'
bot = telebot.TeleBot(TOKEN)

# 📋 Lista de botões com nomes e comandos
comandos = [
    ("Apple TV", "/appletv"),
    ("YouTube", "/youtube"),
    ("Paramount", "/paramount"),
    ("Prime Vídeo", "/primevideo"),
    ("Netflix", "/netflix"),
    ("Crunchyroll", "/crunchyroll"),
    ("Disney Plus", "/disneyplus"),
    ("HBO Max", "/hbomax"),
    ("Viki Rakuten Plus", "/vikirakutenplus"),
    ("Mubi", "/mubi"),
    ("Looke", "/looke"),
    ("Duolingo", "/duolingo"),
    ("Kocowa", "/kocowa"),
    ("Grupo VIP WhatsApp", "/grupovip")
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

    if nome_servico == "appletv":
        resposta = (
            "🍏 *Apple TV*\n"
            "Login: storeflix00@icloud.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso premium garantido"
        )
    elif nome_servico == "youtube":
        resposta = (
            "📺 *YouTube*\n"
            "Login: storeflix9@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ YouTube Premium disponível"
        )
    elif nome_servico == "paramount":
        resposta = (
            "🎞️ *Paramount+*\n"
            "Login: storeflix9@gmail.com\n"
            "Senha: Gcay1234\n"
            "📅 Plano ativo"
        )
    elif nome_servico == "primevideo":
        resposta = (
            "🎬 *Prime Vídeo*\n"
            "Login: storeflix9@gmail.com ou Seu Telefone\n"
            "Senha: Gcay1234\n"
            "✅ Plano familiar disponível"
        )
    elif nome_servico == "netflix":
        resposta = (
            "🍿 *Netflix*\n"
            "Login: jetflixnet@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Conta Premium 4 telas disponível"
        )
    elif nome_servico == "crunchyroll":
        resposta = (
            "🍣 *Crunchyroll*\n"
            "Login: crunchyuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso à animação ilimitada"
        )
    elif nome_servico == "disneyplus":
        resposta = (
            "🏰 *Disney Plus*\n"
            "Login: disneyuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso total aos clássicos e originais Disney"
        )
    elif nome_servico == "hbomax":
        resposta = (
            "📽️ *HBO Max*\n"
            "Login: hbo_user@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Filmes e séries exclusivos disponíveis"
        )
    elif nome_servico == "vikirakutenplus":
        resposta = (
            "📱 *Viki Rakuten Plus*\n"
            "Login: vikiuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso a dramas asiáticos premium"
        )
    elif nome_servico == "mubi":
        resposta = (
            "🎥 *Mubi*\n"
            "Login: mubiuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Filmes independentes e exclusivos"
        )
    elif nome_servico == "looke":
        resposta = (
            "📡 *Looke*\n"
            "Login: lookeuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso a filmes e séries brasileiros"
        )
    elif nome_servico == "duolingo":
        resposta = (
            "🗣️ *Duolingo*\n"
            "Login: duolingo_user@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Aprenda idiomas de forma divertida!"
        )
    elif nome_servico == "kocowa":
        resposta = (
            "🎬 *Kocowa*\n"
            "Login: kocowa_user@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Dramas coreanos e conteúdos exclusivos"
        )
    elif nome_servico == "grupovip":
        resposta = (
            "💬 *GRUPO VIP WHATSAPP*\n"
            "Participe agora do nosso grupo exclusivo no WhatsApp!\n"
            "👉 [Clique aqui para entrar](https://chat.whatsapp.com/JWZeb7hkSF255MqmqPVRSW)"
        )
    else:
        resposta = f"🔐 Gerando conta para: *{nome_servico.upper()}*..."

    bot.send_message(call.message.chat.id, resposta, parse_mode='Markdown', disable_web_page_preview=True)

# ▶️ Iniciar o bot
print("🤖 Bot rodando...")
bot.polling(none_stop=True)
