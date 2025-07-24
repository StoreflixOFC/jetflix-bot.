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
    ("Canva Pro", "/canvapro"),
    ("Spotify", "/spotify"),
    ("CapCut", "/capcut"),
    ("Aplicativos Premium", "/aplicativospremium"),
    ("Listas IPTV", "/listasiptv"),
    ("IPTV Vitalício", "/iptvvitalicio"),
    ("Acervo de Logins", "/acervodelogins"),
    ("Gerador Infinito", "/geradorinfinito"),
    ("Grupo VIP WhatsApp", "/grupovip"),
    ("Super Brindes", "/superbrindes"),
    ("Presentes Grátis", "/presentesgratis")
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
    elif nome_servico == "canvapro":
        resposta = (
            "🎨 *Canva Pro*\n"
            "Login: canvauser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso total ao Canva Pro"
        )
    elif nome_servico == "spotify":
        resposta = (
            "🎵 *Spotify*\n"
            "Login: spotifyuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Spotify Premium disponível"
        )
    elif nome_servico == "capcut":
        resposta = (
            "🎬 *CapCut*\n"
            "Login: capcutuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Edição de vídeo sem limitações"
        )
    elif nome_servico == "aplicativospremium":
        resposta = (
            "📱 *Aplicativos Premium*\n"
            "Login: appuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso a uma seleção de aplicativos premium"
        )
    elif nome_servico == "listasiptv":
        resposta = (
            "📡 *Listas IPTV*\n"
            "Login: iptvuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso às melhores listas IPTV"
        )
    elif nome_servico == "iptvvitalicio":
        resposta = (
            "🌍 *IPTV Vitalício*\n"
            "Login: iptvlifeuser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso IPTV vitalício garantido"
        )
    elif nome_servico == "acervodelogins":
        resposta = (
            "📚 *Acervo de Logins*\n"
            "Login: acervouser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Acesso ao acervo completo de logins"
        )
    elif nome_servico == "geradorinfinito":
        resposta = (
            "🔄 *Gerador Infinito*\n"
            "Login: geradoruser@gmail.com\n"
            "Senha: Gcay1234\n"
            "✅ Gerador infinito de contas premium"
        )
    elif nome_servico == "grupovip":
        resposta = (
            "💬 *GRUPO VIP WHATSAPP*\n"
            "Participe agora do nosso grupo exclusivo no WhatsApp!\n"
            "👉 [Clique aqui para entrar](https://chat.whatsapp.com/JWZeb7hkSF255MqmqPVRSW)"
        )
    elif nome_servico == "superbrindes":
        resposta = (
            "🎁 *Super Brindes*\n"
            "Aproveite ofertas exclusivas de brindes grátis!\n"
            "👉 [Clique aqui para garantir seu brinde](https://jetflix.site)"
        )
    elif nome_servico == "presentesgratis":
        resposta = (
            "🎁 *PRESENTES GRÁTIS*\n"
            "Acesse presentes exclusivos e gratuitos!\n"
            "👉 [Clique aqui para receber seu presente grátis](https://jetflix.site)"
        )
    else:
        resposta = f"🔐 Gerando conta para: *{nome_servico.upper()}*..."

    bot.send_message(call.message.chat.id, resposta, parse_mode='Markdown', disable_web_page_preview=True)

# ▶️ Iniciar o bot
print("🤖 Bot rodando...")
bot.polling(none_stop=True)
