
import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresión regular para detectar mensajes que contienen "Hola"
expresion_regular = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
expresionReguPreg= re.compile(r"como estas|como te encuentras|que tal|que onda", re.IGNORECASE)
expresionReguQueHaces= re.compile(r"que haces|que estas haciendo|que haces", re.IGNORECASE)
expresionReguQuienSoy= re.compile(r"quien soy|como me llamo|como me llamo", re.IGNORECASE)
expresionReguQuienEres= re.compile(r"quien eres|como te llamas|como te llamas", re.IGNORECASE)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}!, el dia de hoy que haremos?",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def adios_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /adios is issued."""
    await update.message.reply_text("Adios!")
    context.application.stop_polling()
     

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    user = update.effective_user
    message_text = update.message.text
    if expresion_regular.search(message_text):
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif expresionReguPreg.search(message_text):
        await update.message.reply_text("Estoy bien, gracias por preguntar. ¿Y tú?")
    elif expresionReguQueHaces.search(message_text):
        await update.message.reply_text("Estoy hablando contigo. ¿Y tú?")
    elif expresionReguQuienSoy.search(message_text):
        await update.message.reply_text(f"claro, eres {user.username} y estas hablando conmigo. ¿En que puedo ayudarte?")
    elif expresionReguQuienEres.search(message_text):
        await update.message.reply_text("soy un bot de telegram, programado para tener conversaciones contigo. ¿En que puedo ayudarte?")
    else:
        await update.message.reply_text("No entendí tu mensaje.")
    
    

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("#Token").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("adios", adios_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()




