NGROK_AUTH_TOKEN = ""
# copy the auth token from https://dashboard.ngrok.com/get-started/your-authtoken
# you don't need to fill ngrok auth token for debugging on local

CONSUMER_KEY = "TmEIQGc2DP9jzZ8pZqpWtXjiZ"
CONSUMER_SECRET = "jHjMSq7sihpUHukjmmnrgDklXC4jiLHKyybabyEKdrAaXMq8e5"
ACCESS_KEY = "1649029946-Cxngle6KTNtJWVZgRX8NM8rX8R00MECnxsvxBzx"
ACCESS_SECRET = "poSJIxRalGtjkHD5NbTtGIM86oICEs4Up2bNdAwg66hZT"
ENV_NAME = "ARHBOT"
# create Account Activity API (AAPI) dev env on https://developer.twitter.com/en/account/environments
# ENV_NAME is the same as Dev environment label
# Check your AAPI subcription renewal date on https://developer.twitter.com/en/account/subscriptions

Admin_id = ["1567637126568878080"] # list of str
# Admin id is like sender id. To check it, send a menfess from your admin account.
# IF YOU WANT TO TEST THE CONFIG, REMEMBER THIS! USERS IN ADMIN_ID PASS ALL USER'S FILTERS, you should delete your id on Admin_id

Timezone = 7

Notify_queue = True
# bool, True: Send the menfess queue to sender
# The first tweet in queue won't be notified to sender (the delay is very quick).
Notify_queueMessage = "ⓘ  Menfess kamu berada pada urutan ke-{}, akan terkirim sekitar pukul {}.\n\nKirimkan pesan '/cancel' untuk " \
                      "membatalkan menfess kamu sebelum terkirim."
# Please keep the "{}" format -> .format(queue, time)

Notify_sent = True
# bool, True: Send menfess tweet link to sender when menfess sent
Notify_sentMessage = "ⓘ  Menfess kamu telah berhasil terkirim! \n\nhttps://twitter.com/{}/status/"
# Please keep the "{}" format -> .format(bot_username) + postid

Notify_sentFail1 = "⚠️ Maaf menfess kamu gagal terkirim, mungkin ada kesalahan pada sistem \nSilahkan coba kembali atau laporkan kepada admin"
# Used when error is happened in system

Interval_perSender = True # bool
Interval_time = 5 # int
# Interval time (in minute) of sending menfess per sender, Admin pass this filter
Notify_intervalPerSender = "❗Oopss! take a rest ☕ \nUntuk menghindari spam silakan kirim menfess lagi setelah pukul {}"
# Please keep the "{}".format(time)

Delay_time = 34 # int, seconds
# Twitter API limits user to post tweet. System will delay 36s per/tweet. You can add it by input
# seconds in Delay_time. e.g Delay_time = 24, it means system will delay 60 seconds per tweet
# I advice you to fill Delay_time to avoid being banned from twitter

# Welcome message to new followers
Greet_newFollower = True
Notif_newFollower = "ⓘ  Hai! Terima kasih udah follow base ini 🖤 \nUntuk mendapatkan follback dari base ini silahkan tunggu max 1x24 jam\n\n📌 Jika ada pertanyaan tentang bot atau ingin paid promote silahkan hubungi admin @arhspace \n\nTerima kasih! 🙏"

Keyword_deleter = True # Trigger word deleter
# bool, True: Delete keyword from menfess before uploaded

# send notif to user that followed by bot
Greet_followed = True
Notif_followed = "ⓘ  Hai! Kamu udah di follback oleh base ini. Jangan lupa ikutin peraturan base ini sebelum mengirim menfess yaa!\n\nKirimkan pesan '/menu' untuk melihat fitur bot."

Minimum_lenMenfess = 5 # length of the menfess
Maximum_lenMenfess = 1120
Notify_lenMenfess = f"⚠️ Untuk mengirimkan menfess minimum jumlah karakter : {Minimum_lenMenfess} dan maksimum jumlah karakter : {Maximum_lenMenfess}"

Only_QRTBaseTweet = False
Notif_QRTBaseTweet = "❗ Kamu hanya bisa mengirim url tweet dari base ini :("

Only_twitterUrl = False
Notif_twitterUrl = "❗ Kamu hanya bisa mengirim url yang berasal dari twitter :("

Verify_beforeSent = True
Verify_beforeSentData = {
    'text'      : 'ⓘ  Sebelum menfess nya dikirim pastiin kamu udah baca dan pahami semua peraturan base ini ya!\n\nKamu yakin mau mengirim menfess ini? 🤔',
    'options'   : [
        {
            'label'         : '👍 Kirim',
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
# bool, True: sender should passes the following requirements: (admin pass this filter)
Only_followed = True
Notif_notFollowed = "ⓘ  Maaf kamu belum bisa mengirim menfess sebelum follow base ini atau kamu belum di follback oleh base ini 😔"
# Minimum_followers and Minimum_day is (automatically) required when Sender_requirements is True.
Minimum_followers = 2 # int
# Minimum-account-created-at
Minimum_day = 100 # 100, it means sender account must be created at 100 days ago
Notify_senderRequirements = f"ⓘ  Maaf yaa kamu belum memenuhi syarat base ini, kamu harus punya {Minimum_followers} followers dan umur akun kamu harus \
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
Notify_accountStatus = "❗Automenfess sedang dimatikan oleh admin, silakan cek tweet terbaru atau \
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

Trigger_word = ["fess!", "🖤"]
Notify_wrongTrigger = {
    'user'      : True, # send notif to user
    'admin'     : False, # send wrong trigger menfess to admin
    'message'   : "ⓘ  Hello! Selamat datang di base kami :) \n\nUntuk bisa kirim menfess silahkan gunakan trigger word 🖤\nKamu bisa juga kirimkan pesan /menu untuk melihat fitur bot\n\n📌 Jangan lupa follow base kami yaa dan jangan lupa baca RULES!\n\nJika ada pertanyaan silahkan hubungi admin @arhspace\n\nTerima kasih! 🙏🏼\n\nhttps://p.arh.my.id/",
}

Sensitive_word = "/sensitive"
# Used when sender send sensitive content, order them to use this word
# But I advise against sending sensitive content, Twitter may ban your account,
# And using this bot for 'adult' base is strictly prohibited.
Blacklist_words = ['covid', 'blablabla', 'nigga'] 
# hashtags and mentions will be changed to "#." and "@."
Notify_blacklistWords = "‼️ Maaf di menfess kamu terdapat blacklist words, jangan lupa baca peraturan base yaa!"
Notify_blacklistWordsAdmin = True # Will be sent to admin

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
    'succeed'   : 'ⓘ  Menfess kamu sudah berhasil dihapus!',
    'failed'    : 'ⓘ  Menfess ini udah ga bisa kamu hapus :('
}
# Notif_DMCmdDelete is only for user, '/unsend' using this notif too
Notif_DMCmdCancel = {
    'succeed'   : 'ⓘ  Menfess kamu berhasil di-cancel',
    'failed'    : 'ⓘ  Menfess kamu udah ga bisa di-cancel',
    'on_process': 'ⓘ  Menfess kamu lagi diproses, kirim "/unsend" apabila ingin batal kirim sebelum menfess terkirim',
}

# Max 20 options, Max 72 chars description, Please keep the metadata, Read metadata doc at README.md
# When user click the button, It is automatically sent to webhook (dont use if command has an argument e.g. /delete (url))
DMCmdMenu = {
    'text'      : 'ⓘ Hello 👋\nUntuk mengirimkan menfess kamu bisa gunakan trigger word 🖤\nKamu juga bisa mengirim beberapa command secara langsung melalui botton atau menulis manual:\n\n'
                  'Contoh : /delete (url menfess) : Untuk menghapus menfess dengan menyertakan url\n/unsend : Untuk menghapus menfess terakhir yang telah terkirim\n\n📌 Jika ada pertanyaan silahkan hubungi admin @arhspace\n\nTerima kasih! :)',
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
