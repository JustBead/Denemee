import random
import telebot
import json

# Telegram bot token'ınızı buraya girin
TOKEN = '8026541050:AAEfrfEPvy3Ep5V4NSbQcw4zTJhQ89d9VmY'
bot = telebot.TeleBot(TOKEN)

# Fake profil veritabanı (200 Türk kullanıcı adı)
fake_profiles = [
    "@ahmet_yilmaz", "@selin_ozdemir", "@murat_karaman", "@zeynep_demir", "@omer_sahin",
    "@seda_balcı", "@enes_uzun", "@ayse_kaya", "@berke_gunes", "@gokhan_aksoy",
    "@mustafa_karabulut", "@hande_simsek", "@fatma_ozkan", "@mehmet_akbaba", "@esra_dogan",
    "@cengiz_ozdemir", "@sevim_kaan", "@burak_tuna", "@melike_bayram", "@ali_hasan",
    "@yusuf_ozdemir", "@zeynep_davutoglu", "@serkan_akin", "@gizem_aslan", "@furkan_ozkan",
    "@selma_kurt", "@hasan_terzi", "@tuğba_bayraktar", "@gokce_yıldırım", "@beyza_karataş",
    "@huseyin_gezgin", "@serap_koc", "@adem_kara", "@tuğçe_tosun", "@erhan_kaplan",
    "@cem_karaca", "@gokhan_sarac", "@betül_eren", "@salih_demirtaş", "@kader_yılmaz",
    "@mahmut_yıldız", "@elif_aslan", "@ramazan_ozdemir", "@mert_sarıkaya", "@tugba_ozturk",
    "@buket_kılıç", "@bilal_eren", "@ozge_güzel", "@kaan_kaplan", "@halil_demir",
    "@nurcan_ozdemir", "@ömer_tarkan", "@necdet_sungur", "@sibel_alp", "@murat_yılmaz",
    "@sude_sarı", "@ercan_köse", "@duru_koc", "@sultan_özdemir", "@kemal_demir",
    "@nazlı_karaca", "@ali_fatih", "@gizem_karataş", "@hüseyin_ertem", "@serdar_yılmaz",
    "@melek_dursun", "@evren_karaca", "@sevim_yılmaz", "@eyüp_ozdemir", "@haluk_karaman",
    "@özge_gürel", "@hamza_durmuş", "@dilek_uzun", "@özlem_baltacı", "@selim_tosun",
    "@ramazan_karakoç", "@ayhan_demirci", "@mustafa_tosun", "@ayşegül_uzun", "@kaan_özdemir",
    "@gülsüm_güzel", "@serdar_akyüz", "@yeliz_kaplan", "@mehmet_özkan", "@ömer_kurt",
    "@büşra_karataş", "@ferhat_dogan", "@nebahat_ozkan", "@kerem_çalışkan", "@tamer_aydin",
    "@ayse_tosun", "@mustafa_sarıkaya", "@nazlı_özdemir", "@süleyman_koç", "@ayça_ozdemir",
    "@ilker_yılmaz", "@murat_sarıkaya", "@bahar_turan", "@kadir_uzun", "@seda_karataş",
    "@gözde_yıldız", "@serkan_terzi", "@hamza_özdemir", "@melike_karaman", "@bilal_bayraktar",
    "@gülhan_karaca", "@hatice_şahin", "@onur_kanat", "@aşkın_özdemir", "@yıldız_karataş",
    "@kubilay_özdemir", "@sefa_sarıkaya", "@ayhan_sarıkaya", "@betül_kaplan", "@cemre_erdem",
    "@yusuf_karakoç", "@hasan_kanat", "@sinan_karaca", "@fatih_özdemir", "@gülbeyaz_dönmez",
    "@aysegül_şahin", "@ercan_şen", "@tuncay_yıldız", "@sibel_aydın", "@mustafa_turan",
    "@özlem_sarı", "@fatma_kurt", "@kemal_şahin", "@gökhan_özdemir", "@ayşegül_yılmaz",
    "@zafer_kaplan", "@özge_yıldız", "@ekrem_durmuş", "@bahar_bayraktar", "@mehmet_şen",
    "@selman_özdemir", "@gizem_şahin", "@barış_ozdemir", "@turkan_karaca", "@meltem_sarı",
    "@süleyman_ozdemir", "@tulay_karataş", "@gokhan_turan", "@turkhan_karaca", "@ferit_özdemir",
    "@nevzat_sarı", "@serap_karakaş", "@berke_karadağ", "@ayhan_karataş", "@büşra_sarı",
    "@hüseyin_karaca", "@meltem_kurt", "@ömer_öztürk", "@murat_özdemir", "@cengiz_şahin",
    "@yunus_karataş", "@kadir_çelik", "@zeynep_terzi", "@fatih_sarı", "@sinan_terzi",
    "@berna_karaca", "@buket_özdemir", "@ayşegül_karataş", "@serdar_çelik", "@kadir_karaca",
    "@selin_terzi", "@gökhan_çelik", "@sibel_karakoç", "@gülden_özdemir", "@büşra_karaman",
    "@zeynep_sarı", "@faruk_şahin", "@abdullah_bayraktar", "@serap_özdemir", "@feyza_aksoy",
    "@sevim_terzi", "@necati_özdemir", "@ebru_karaca", "@emre_bayram", "@ayşegül_karaman",
    "@onur_özdemir", "@ahmet_özdemir", "@cemre_karaca", "@doğa_özdemir", "@irfan_karakoç",
    "@hüseyin_şahin", "@bahar_ozdemir", "@ismail_yılmaz", "@mustafa_terzi", "@neslihan_özdemir"
]

# Örnek veri (Kullanıcılar ve plan bilgisi)
users_data = {
    "user_id": {
        "name": "user_name",
        "plan": "free",
        "paid": False,
    }
}

# Başlangıçta kullanıcılar için tanımlı olmayan komutlar
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Merhaba, botumuza hoş geldiniz! Yardım almak için /help yazabilirsiniz.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Yardım menüsüne hoş geldiniz. Kullanabileceğiniz komutlar:\n"
                                      "/stalk - Stalk yapanları gör\n"
                                      "/price - Fiyat menüsü\n"
                                      "/payment - Ödeme yap")

@bot.message_handler(commands=['stalk'])
def stalk(message):
    # Kullanıcının planına göre stalk yapan profillerin gösterilmesi
    if users_data[message.chat.id]["plan"] == "free":
        selected_profiles = random.sample(fake_profiles, 5)
        blurred_profiles = [profile[:3] + "*" * 5 for profile in selected_profiles]
        response = f"Bu kişiler seni stalkladı: \n" + " ".join(blurred_profiles)
    else:
        selected_profiles = random.sample(fake_profiles, 5)
        response = f"Bu kişiler seni stalkladı: \n" + " ".join(selected_profiles)
    
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['price'])
def price(message):
    bot.send_message(message.chat.id, "Fiyatlar:\n1. Günlük Plan: 10 TL (0.55 USD)\n2. Haftalık Plan: 50 TL (2.75 USD)\n3. Aylık Plan: 200 TL (11 USD)")

@bot.message_handler(commands=['payment'])
def payment(message):
    bot.send_message(message.chat.id, "Ödeme yapmak için aşağıdaki adımları takip edin.")

@bot.message_handler(commands=['justadmin'])
def admin_login(message):
    bot.send_message(message.chat.id, "Admin paneline giriş yapın. Kullanıcı adı ve şifreyi girin.")
    # Giriş ekranı için ekleme yapılabilir

# Botu başlat
bot.polling()
