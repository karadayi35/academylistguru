from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Grup kimliğini tanımla (örneğin -1002188591527)
GROUP_CHAT_ID = -1002188591527  # Buraya grup kimliğini ekleyin

# /site ve !site komutu çalıştırıldığında yanıt verecek fonksiyon
async def site_command(update: Update, context: CallbackContext):
    # Sadece belirlenen grupta komutun çalışmasına izin ver
    if update.message.chat_id != GROUP_CHAT_ID:
        return
    
    # Butonlar
    buttons = [
        [InlineKeyboardButton(text="👑Stake 10 USDT Bonus Al", url="https://stake.com/?c=9dd9dbc553")],
        [InlineKeyboardButton(text="👑Slottica %200 Yatırım Bonusu", url="https://gopartner.link/?a=205678&c=184089&s1=6028")],
        [InlineKeyboardButton(text="👑Mostbet Toplam 150,000 TL Bonus", url="https://t.ly/eAL_1")],
        [InlineKeyboardButton(text="🎲Lightning Rulet İstatistik", url="https://t.me/rouletteacademystatistics")],
        [InlineKeyboardButton(text="🎲Baccarat Tahmin Bot", url="https://t.me/academybaccarat_bot")],
        [InlineKeyboardButton(text="🎲Rulet Tahmin Bot", url="https://t.me/rouletteacademyprediction_bot")],
        [InlineKeyboardButton(text="🎲Sponsor Güvenilir Siteler", url="https://rouletteacademyturkey.vercel.app/")],
    ]

    # Butonları inline keyboard formatına dönüştür
    keyboard = InlineKeyboardMarkup(buttons)

    # Yanıt olarak butonları gönder
    await update.message.reply_text('Aşağıdaki butonlar ile istediğiniz sayfaya gidebilirsiniz:', reply_markup=keyboard)

# Ana fonksiyon
def main():
    # Bot tokenini buraya ekle
    TOKEN = 'YOUR BOT TOKEN HERE'

    # Botu oluştur
    application = Application.builder().token(TOKEN).build()

    # /site komutunu dinle
    application.add_handler(CommandHandler('site', site_command))

    # !site yazıldığında dinle (mesaj işleyici)
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^!site$'), site_command))

    # Botu çalıştır
    application.run_polling()

if __name__ == '__main__':
    main()
