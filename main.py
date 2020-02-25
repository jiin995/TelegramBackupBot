import logging
import sys
from datetime import datetime
from telegram.ext import Updater
from ConfigManager import ConfigManager

#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)


updater = Updater(token=ConfigManager.get_token(), use_context=True)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        for chat in ConfigManager.get_backup_chats():
            updater.bot.send_document(chat_id=chat["chat_id"], document=open(sys.argv[1], 'rb'),
                                  caption="Ciao "+chat["username"]+"  \nEcco il nuovo Backup: "+ConfigManager.get_backup_name()+" "+datetime.now().strftime("%d/%m/%Y") +
                                  "\n#" +ConfigManager.get_backup_name().replace(" ", "_") +
                                  "\n#Backup_"+datetime.now().strftime("%d_%m_%Y"))
