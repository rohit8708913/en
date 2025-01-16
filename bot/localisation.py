from bot.get_cfg import get_config

class Localisation:
    START_TEXT = "Hᴇʟʟᴏ, \n<blockquote><b>𝚃𝚑𝚒𝚜 𝙸𝚜 𝙰 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚅𝚒𝚍𝚎𝚘 𝙴𝚗𝚌𝚘𝚍𝚎𝚛 𝙱𝚘𝚝. 𝙼𝚊𝚍𝚎 𝙱𝚢 @rohit_1888.</b>. \n\n<b>𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚎𝚗𝚍 𝙼𝚎 𝙰𝚗𝚢 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙱𝚒𝚐 𝚅𝚒𝚍𝚎𝚘 𝙵𝚒𝚕𝚎 𝙸 𝚆𝚒𝚕𝚕 𝙲𝚘𝚖𝚙𝚛𝚎𝚜𝚜 𝙸𝚝 𝙰𝚜 𝚂𝚖𝚊𝚕𝚕 𝚅𝚒𝚍𝚎𝚘 𝙵𝚒𝚕𝚎.</b> \n\n/help 𝙵𝚘𝚛 𝙼𝚘𝚛𝚎 𝙳𝚎𝚝𝚊𝚒𝚕𝚜.</blockquote> \n✨ 𝙴𝚗𝚓𝚘𝚢❣️❣️....."
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "Dᴏᴡɴʟᴏᴀᴅɪɴɢ...📥" 
    
    UPLOAD_START = "Uᴘʟᴏᴀᴅɪɴɢ...📤"
    
    COMPRESS_START = "Tʀʏɪɴɢ ᴛᴏ Eɴᴄᴏᴅᴇ...📀"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS =  "𝙼𝚊𝚍𝚎 𝙱𝚢➛ @rohit_1888"

    COMPRESS_PROGRESS = "<blockquote>⏳ ETA: {}\n🚀 Pʀᴏɢʀᴇꜱꜱ: {}%</blockquote>"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Cʟᴇᴀʀᴇᴅ Sᴜᴄᴄᴇꜱꜰᴜʟʟʏ...✅"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Mᴇᴅɪᴀ Cʟᴇᴀʀᴇᴅ Sᴜᴄᴄᴇꜱꜰᴜʟʟʏ...✅"
    
    SAVED_RECVD_DOC_FILE = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ...✅"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "Nᴏ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Fᴏᴜɴᴅ...💔"
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Encoder Logs ."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nMaintained By @rohit_1888"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
