NGROK_AUTH_TOKEN = ""
# copy the auth token from https://dashboard.ngrok.com/get-started/your-authtoken
# you don't need to fill ngrok auth token for debugging on local

CONSUMER_KEY = "WMKscjqBVKLrL2oLnHvsbGctd"
CONSUMER_SECRET = "xzVm5A65jXMjXaerVGCAosYzywzOIYlVu7jDmegimAe4Jtv9CE"
ACCESS_KEY = "1567637126568878080-lP6ShJ8euijBClTfRI5yDtBCUFYYQ6"
ACCESS_SECRET = "pzJj0DDPLSmY5jvgahF3aMuPzTXfKGquRdNedc3tC619r"
ENV_NAME = "arh"
# create Account Activity API (AAPI) dev env on https://developer.twitter.com/en/account/environments
# ENV_NAME is the same as Dev environment label
# Check your AAPI subcription renewal date on https://developer.twitter.com/en/account/subscriptions

Admin_id = ["1578392535369596932"] # list of str
# Admin id is like sender id. To check it, send a menfess from your admin account.
# IF YOU WANT TO TEST THE CONFIG, REMEMBER THIS! USERS IN ADMIN_ID PASS ALL USER'S FILTERS, you should delete your id on Admin_id

Timezone = 7

Notify_queue = True
# bool, True: Send the menfess queue to sender
# The first tweet in queue won't be notified to sender (the delay is very quick).
Notify_queueMessage = "[ARHSPACE 🌟]\n\nHi! Menfess kamu berada pada urutan ke-{}, akan terkirim sekitar pukul {}.\n\nKirimkan '/cancel' untuk " \
                      "membatalkan menfess kamu sebelum terkirim."
# Please keep the "{}" format -> .format(queue, time)

Notify_sent = True
# bool, True: Send menfess tweet link to sender when menfess sent
Notify_sentMessage = "Yeay! Menfess kamu telah berhasil terkirim! \nhttps://twitter.com/{}/status/"
# Please keep the "{}" format -> .format(bot_username) + postid

Notify_sentFail1 = "‼️⚠️ Maaf ada kesalahan pada sistem :( \nTolong screenshot & laporkan kepada admin yaa"
# Used when error is happened in system

Interval_perSender = True # bool
Interval_time = 5 # int
# Interval time (in minute) of sending menfess per sender, Admin pass this filter
Notify_intervalPerSender = "[ARHSPACE 🌟]\n\n❗Oopss! take a rest~ ☕ \nMengirim menfess dibatasi untuk sementara waktu supaya tidak terjadi spam!\n\nSilakan coba lagi yaa setelah pukul {}"
# Please keep the "{}".format(time)

Delay_time = 24 # int, seconds
# Twitter API limits user to post tweet. System will delay 36s per/tweet. You can add it by input
# seconds in Delay_time. e.g Delay_time = 24, it means system will delay 60 seconds per tweet
# I advice you to fill Delay_time to avoid being banned from twitter

# Welcome message to new followers
Greet_newFollower = True
Notif_newFollower = "[ARHSPACE 🌟]\n\nHai~~~ Makasih banyak kamu udah follow base ini 🥰🖤 \nUntuk mendapatkan follback dari base ini silahkan tunggu max 1x24 jam yaa\n\n📌 Jika ada pertanyaan silahkan hubungi admin @hi_arh\n\n🤝 Jika ingin paid promote bisa banget hubungi @promote_arh \n\nTerima kasih! 🙏"

Keyword_deleter = False # Trigger word deleter
# bool, True: Delete keyword from menfess before uploaded

# send notif to user that followed by bot
Greet_followed = True
Notif_followed = "[ARHSPACE 🌟]\n\nYeay! Kamu udah difollow base ini. Jangan lupa baca, pahami dan ikutin peraturan sebelum mengirim menfess yaa! 🥰\n\nKirimkan '/menu' untuk melihat fitur base."

Minimum_lenMenfess = 5 # length of the menfess
Maximum_lenMenfess = 1120
Notify_lenMenfess = f"[ARHSPACE 🌟]\n\n⚠️ Untuk mengirimkan menfess minimum jumlah karakter : {Minimum_lenMenfess} dan maksimum jumlah karakter : {Maximum_lenMenfess}"

Only_QRTBaseTweet = False
Notif_QRTBaseTweet = "❗ Kamu hanya bisa mengirim url tweet dari base ini :("

Only_twitterUrl = True
Notif_twitterUrl = "❗ Kamu hanya bisa mengirim url yang berasal dari twitter :("

Verify_beforeSent = True
Verify_beforeSentData = {
    'text'      : '[ARHSPACE 🌟] \n\nSebelum menfess nya dikirim pastiin kamu udah baca dan pahami semua peraturan base ini ya!\n\nKamu yakin mau mengirim menfess ini? 🤔',
    'options'   : [
        {
            'label'         : '👍 Iya',
            'description'   : 'Melanjutkan untuk mengirim menfess', # max 72 chars (include space)
            'metadata'      : 'exec|self._verif_menfess("accept", sender_id)'
        },
        {
            'label'         : '❌ Batal',
            'description'   : 'Membatalkan untuk mengirim menfess', # max 72 chars (include space)
            'metadata'      : 'exec|self._verif_menfess("reject", sender_id)'
        }
    ]
}
# Please keep the metadata, Read metadata documentation at README.md

Sender_requirements = True
# bool, True: sender should passes the following requirements:   (admin pass this filter)
Only_followed = True
Notif_notFollowed = "[ARHSPACE 🌟] \n\nHmmmm, duhh maaf nih, mungkin kamu belum follow 😒 atau belum di follow back base ini jadi kamu belum bisa ngirim menfess dehh 😔"
# Minimum_followers and Minimum_day is (automatically) required when Sender_requirements is True.
Minimum_followers = 1 # int
# Minimum-account-created-at
Minimum_day = 2 # e.g 100, it means sender account must be created at 100 days ago
Notify_senderRequirements = f"[ARHSPACE 🌟] \n\nYahhh 😭 Maaf yaa kamu belum memenuhi syarat base ini, kamu harus punya {Minimum_followers} followers dan umur akun kamu harus \
lebih dari {Minimum_day} hari biar bisa ngirim menfess.\nCoba lagi yaa di lain waktu ☹️🙏"

Private_mediaTweet = False
# bool, True: Delete username on the bottom of the attached video tweet.
# Usually when sender want to attach video (from tweet), they will attach a media url
# But the username of the (VIDEO) OWNER is mentioned on the bottom of video. With this
# when sender attach (media and/or media tweet) and if total of media ids are more than
# 4 or the space is not available, THE REST OF THE MEDIA WILL BE ATTACHED TO THE
# SUBSEQUENT TWEETS IN SORTED ORDER.

Watermark = True
# bool, True: Add watermark text to menfess's photo
Watermark_data = {
    'image'     : 'twitter_autobase/watermark/ARHP.png', # bool (True: default image, False: no image) or image file path (str) 
    'text'      : '', # if you won't to add text, fill it with empty string ''
    'font'      : 'twitter_autobase/watermark/FreeMono.ttf', # font file path
    'textColor' : (100,0,0,1), # RGBA
    'textStroke': (0,225,225,1), # RGBA
    'ratio'     : 0.15, # ratio between watermark and photo (float number under 1)
    'position'  : ('right', 'bottom'), # (x, y) | x: 'left', 'center', 'right' | y: 'top', 'center', 'bottom'
}

Account_status = True
# bool, True: Turn on the automenfess. If it turned into False, this bot won't
# post menfess. You can switch it using '/switch on/off' command from DM
Notify_accountStatus = "[ARHSPACE 🌟]\n\n❗Automenfess sedang dimatikan oleh admin, silakan cek tweet terbaru atau \
hubungi admin untuk informasi lebih lanjut"

Off_schedule = False
# schedule automenfess to turned off
Off_scheduleData = {
    'start'         : ('21', '06'), # ('hour', 'minute')
    'different_day' : True,
    'end'           : ('04', '36'), # ('hour', 'minute')
}
Off_scheduleMsg = f"Automenfess dimatikan setiap pukul {Off_scheduleData['start'][0]}:{Off_scheduleData['start'][1]} \
sampai dengan pukul {Off_scheduleData['end'][0]}:{Off_scheduleData['end'][1]}"

Trigger_word = ["fess!", "blablabla!", "🌟"]
Notify_wrongTrigger = {
    'user'      : True, # send notif to user
    'admin'     : False, # send wrong trigger menfess to admin
    'message'   : "[ARHSPACE 🌟]\n\nHmmm 🤔?\nMaaf trigger tidak diketahui, silahkan gunakan trigger 🌟 untuk mengirim menfess di base ini.\n\nKirimkan '/menu' untuk melihat fitur base\n\n📌 Jangan lupa follow kami yaa!\nJika ada pertanyaan silahkan hubungi admin @hi_arh\n\nTerima kasih!",
}

Sensitive_word = "/sensitive"
# Used when sender send sensitive content, order them to use this word
# But I advise against sending sensitive content, Twitter may ban your account,
# And using this bot for 'adult' base is strictly prohibited.
Blacklist_words = ['covid', 'blablabla'] 
# hashtags and mentions will be changed to "#." and "@."
Notify_blacklistWords = "[ARHSPACE 🌟]\n\n⚠️‼️ Maaf di menfess kamu terdapat blacklist words, jangan lupa baca peraturan base yaa!"
Notify_blacklistWordsAdmin = False # Will be sent to admin

# Please set Admin_cmd and User_cmd in lowercase
# Read README.md for the DMs examples
# You can move Admin_cmd to User_cmd and vice versa

Admin_cmd = {
    '/add_blacklist'    : 'self._add_blacklist(arg)', # /add_blacklist word1 word2 word-n
    '/rm_blacklist'     : 'self._rm_blacklist(arg)', # /rm_blacklist word1 word2 wordn
    '/display_blacklist': 'self._display_blacklist(sender_id)', # /display_blacklist
    '/who'              : 'self._who_sender(sender_id, urls)', # /who tweet_url
    '/add_admin'        : 'self._add_admin(arg)', # /add_admin username1 username2 username-n
    '/rm_admin'         : 'self._rm_admin(arg)', # /rm_admin username username2 username-n
    '/switch'           : 'self._switch_status(arg)', # /switch on | /switch off
    '/block'            : 'self._block_user(sender_id, urls)', # /block tweet_url
    '/unfoll'           : 'self._unfoll_user(sender_id, urls)', # /unfoll tweet_url
    '/follow'           : 'self._foll_user(arg)', #/follow username
}
# if arg argument exists on method call, the terminal message will be sent to sender (admin).
# You can prevent it by adding #no_notif after the method call.
# /who is only available for one day (reset every midnight or heroku dyno cycling)

User_cmd = {
    '/delete'           : 'self._delete_menfess(sender_id, urls)', # /delete tweet_url
    '/unsend'           : 'self._unsend_menfess(sender_id)', # /unsend
    '/menu'             : 'self._menu_dm(sender_id)', # /menu
    '/cancel'           : 'self._cancel_menfess(sender_id)', # /cancel
    '/display_blacklist': 'self._display_blacklist(sender_id)', # /display_blacklist
}
# /delete and /unsend is not available for user when bot was just started and user id not in db_sent
# /delete & db_sent are only available for one day (reset every midnight or heroku dyno cycling)
Notif_DMCmdDelete = {
    'succeed'   : 'Yeay! Menfess kamu sudah berhasil dihapus!',
    'failed'    : 'Duh! Menfess ini ngga bisa kamu hapus :('
}
# Notif_DMCmdDelete is only for user, '/unsend' using this notif too
Notif_DMCmdCancel = {
    'succeed'   : 'Yeay! Menfess kamu berhasil di-cancel',
    'failed'    : 'Duh! Menfess kamu ngga bisa di-cancel',
    'on_process': 'Duh! Menfess kamu lagi diproses, kirim "/unsend" setelah menfess terkirim',
}

# Max 20 options, Max 72 chars description, Please keep the metadata, Read metadata doc at README.md
# When user click the button, It is automatically sent to webhook (dont use if command has an argument e.g. /delete (url))
DMCmdMenu = {
    'text'      : '[ARHSPACE 🌟]\n\nHai 👋\nUntuk mengirimkan menfess kamu bisa gunakan trigger 🌟\nKamu juga bisa mengirim beberapa command secara langsung atau menulis manual:\n\n'
                  '/delete (url menfess) : Menghapus menfess dengan menyertakan url\n/unsend : Menghapus menfess terakhir yang telah terkirim\n\n📌 Jika ada pertanyaan silahkan hubungi admin @hi_arh\n\nTerima kasih! :)',
    'options'   : [
        {
            'label'         : 'Unsend',
            'description'   : 'Menghapus menfess terakhir yang telah terkirim',
            'metadata'      : 'exec|self._button_command(sender_id, "/unsend")'
        },
        {
            'label'         : 'Cancel',
            'description'   : 'Menghapus menfess sebelum terkirim',
            'metadata'      : 'exec|self._button_command(sender_id, "/cancel")' 
        },
	  {
            'label'         : 'Blacklist Words',
            'description'   : 'Menampilkan blacklist words',
            'metadata'      : 'exec|self._button_command(sender_id, "/display_blacklist")'
        },
    ]
}

Trigger_word
