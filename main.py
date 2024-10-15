from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot tokeni
BOT_TOKEN = '8174146834:AAFjiRmw1-2QBpL_E4YXWKhNywtTWPKnYtE'

# Grup kimliğini buraya yaz
GROUP_CHAT_ID = -1002188591527  # Bu senin gruptan aldığın chat_id


# !site veya /site komutu çalıştırıldığında yanıt verecek fonksiyon
def site_command(update: Update, context: CallbackContext):
    # Sadece belirli grupta komutun çalışmasına izin ver
    if update.message.chat_id != GROUP_CHAT_ID:
        return

    # Butonlar
    buttons = [
        [InlineKeyboardButton(text="👑Stake 10 USDT Bonus Al", url="https://stake.com/?c=9dd9dbc553")],
        [InlineKeyboardButton(text="👑Slottica %200 Yatırım Bonusu",
                              url="https://gopartner.link/?a=205678&c=184089&s1=6028")],
        [InlineKeyboardButton(text="👑Mostbet Toplam 150,000 TL Bonus", url="https://t.ly/eAL_1")],
        [InlineKeyboardButton(text="🎲Lightning Rulet İstatistik", url="https://t.me/rouletteacademystatistics")],
        [InlineKeyboardButton(text="🎲Baccarat Tahmin Bot", url="https://t.me/academybaccarat_bot")],
        [InlineKeyboardButton(text="🎲Rulet Tahmin Bot", url="https://t.me/rouletteacademyprediction_bot")],
        [InlineKeyboardButton(text="🎲Sponsor Güvenilir Siteler", url="https://rouletteacademyturkey.vercel.app/")],
    ]

    # Butonları inline keyboard formatına dönüştür
    keyboard = InlineKeyboardMarkup(buttons)

    # Yanıt olarak butonları gönder
    update.message.reply_text('Önerilen En Güvenilir Siteler', reply_markup=keyboard)


# !site yazıldığında algılayan mesaj işleyici
def handle_text(update: Update, context: CallbackContext):
    if update.message.text == '!site':
        site_command(update, context)


def main():
    # Botu başlat
    updater = Updater(BOT_TOKEN, use_context=True)

    # Dispatcher, botun komutları dinlemesi için kullanılır
    dp = updater.dispatcher

    # /site komutunu dinle (standart komut çalışır)
    dp.add_handler(CommandHandler('site', site_command))

    # !site yazıldığında algılayan mesaj işleyici
    dp.add_handler(MessageHandler(filters.TEXT & filters.Regex('^!site$'), handle_text))


    # Botu çalıştır
    updater.start_polling()

    # Botu sürekli çalıştır
    updater.idle()


if __name__ == '__main__':
    main()
