from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from typing import Final
from datetime import datetime

TOKEN: Final = "6234901694:AAFY_UNu-0hRN5Is-a-o7b53lJXvq0akjjo"
BOT_USERNAME: Final = "@perwor_bot"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, This is PerWor Bot")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """ *******************************
            /start --- welcome
            /help --- for commands display
            /breakfast --- for today's breakfast
            /lunch --- for today's lunch
            /snacks --- for today's snacks
            /dinner --- for today's dinner
            
            *******************************
    """)


async def breakfast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = {
        "Week 1": {
            "Monday": """                         PONGAL, MYSORE BONDA(2),
                         Sambar, G Chutney
                         BBJ, Sprouted Grains
                         OMELETTE(1)/BANANA(1)
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Tuesday": """                         ONION DOSA,
                         Sambar, C Chutney
                         BBJ, Sprouted Grains
                         BOILED EGG(1)/ FRUIT*
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Wednesday": """                         IDLY, VADA(2),
                         Sambar, G Chutney
                         BBJ, Sprouted Grains
                         OMELETTE(1)/BANANA(1)
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Thursday": """                         POORI,
                         CHANNA MASALA
                         BBJ, Sprouted Grains
                         BOILED EGG(1)/ FRUIT*
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Friday": """                         SEMIYA UPMA, POHA,
                         MYSORE BONDA(2), P Chutney
                         BBJ, Sprouted Grains
                         OMELETTE(1)/BANANA(1)
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Saturday": """                         ALOO PARATHA,
                         CHANNA MASALA, RAITHA, PICKLE
                         BBJ, Sprouted Grains
                         BOILED EGG(1)/ FRUIT*
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Sunday": """                         Rava Dosa,
                         Sambar, C Chutney
                         BBJ, Sprouted Grains
                         Seasonal Cut Fruits
                         Tea, Coffee, Milk, Sugar, Salt"""
        },
        "Week 2": {
            "Monday": """                         PESARATTU, UPMA,
                         Sambar, RED COCNUT CHUTNEY
                         BBJ, Sprouted Grains
                         OMELETTE(1)/BANANA(1)
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Tuesday": """                         POORI,
                         POTATO MASALA
                         BBJ, Sprouted Grains
                         BOILED EGG(1)/ FRUIT*
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Wednesday": """                         MASALA DOSA,
                         Sambar, P Chutney
                         BBJ, Sprouted Grains
                         OMELETTE(1)/BANANA(1)
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Thursday": """                         CHOW CHOW BATH,
                         MYSORE BONDA(2), C CHUTNEY
                         BBJ, Sprouted Grains
                         BOILED EGG(1)/ FRUIT*
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Friday": """                         RAVA IDLY, VADA(2),
                         SAMBAR, P Chutney
                         BBJ, Sprouted Grains
                         OMELETTE(1)/BANANA(1)
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Saturday": """                         METHI PARATHA,
                         CHANNA MASALA, CURD(2 CUPS), PICKLE
                         BBJ, Sprouted Grains
                         BOILED EGG(1)/ FRUIT*
                         Tea, Coffee, Milk, Sugar, Salt""",
            "Sunday": """                         ONION UTHAPPAM,
                         Sambar, G Chutney
                         BBJ, Sprouted Grains
                         Seasonal Cut Fruits
                         Tea, Coffee, Milk, Sugar, Salt"""
        }
    }

    # Get the current week number (odd or even)
    week_number = datetime.now().isocalendar()[1] % 2

    # Get the current day of the week and the corresponding mess menu
    day_of_week = datetime.today().strftime('%A')
    todays_menu = menu[f"Week {week_number+1}"][day_of_week]
    await update.message.reply_text(todays_menu)


async def lunch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = {
        "Week 1": {
            "Monday": """CHAPATTI , DAL MAKHANI
                         BHINDI FRY WITH PEANUT *
                         RICE,SAMBAR,RASAM, CURD,PAPAD
                         LEMON PICKLE
                         SUGAR ,SALT ,GHEE,PODI
                         SALAD""",
            "Tuesday": """POORI , DUM ALOO
                          BEANS CARROT PORIYAL
                          RICE,VATHAKOLABMU,RASAM,CURD,FRYUMS
                          ,TOMATO PICKLE
                          SUGAR ,SALT ,GHEE,PODI
                          JUICE""",
            "Wednesday": """CHAPATTI , PANCHRATAN DAL
                            ONION PAKODA*, PERUGU PACHADI
                            RICE,BRINJAL MOCHAI GRAVY, RASAM,MASALA PAPAD
                            MANGO PICKLE
                            SUGAR ,SALT ,GHEE,PODI
                            SALAD""",
            "Thursday": """PHULKA , RAJMA DAL,
                           ALOO GOBI MATAR DRY
                           RICE,MASALA SAMBAR,RASAM,CURD,FRYUMS
                           MANGO PICKLE
                           SUGAR ,SALT ,GHEE,PODI
                           JUICE""",
            "Friday": """PHULKA, PUMPKIN KAALA CHANA
                         RICE, BEETROOT CHANA PORIYAL
                         RASAM, CURD,PAPAD
                         MIX VEG PICKLE, VATHAKOLAMBU
                         SUGAR ,SALT ,GHEE,PODI
                         SALAD""",
            "Saturday": """CHAPATTI , CORN PEAS MASALA
                           SPROUTED DAL,
                           RICE,RASAM, CURD,FRYUMS
                           MANGO PICKLE, BEETROOT PORIYAL
                           SUGAR ,SALT ,GHEE,PODI
                           JUICE""",
            "Sunday": """PHULKA , KADAI CHK * ( for NV),
                         PHULKA , PANEER BUTTER MASALA * ( for Veg),
                         VEG BIRYANI , ONION RAITHA
                         JUICE"""
        },
        "Week 2": {
            "Monday": """CHAPATTI , PEAS MASALA
                         ALOO MASALA WEDGES,
                         RICE,SAMBAR,RASAM, CURD,FRYUMS
                         TOMATO PICKLE
                         SUGAR ,SALT ,GHEE,PODI
                         SALAD""",
            "Tuesday": """PHULKA, VEG KURMA
                          BEETROOT CHANNA PORIYAL
                          RICE,VATHAKOLAMBU,RASAM,CURD,PAPAD
                          MANGO PICKLE
                          SUGAR ,SALT ,GHEE,PODI
                          JUICE""",
            "Wednesday": """CHAPATTI, MIXED DAL
                            BRINJAL PORIYAL
                            RICE,MIX VEG KARAKOZHAMBU,RASAM, CURD,FRYUMS
                            LEMON PICKLE
                            SUGAR ,SALT ,GHEE,PODI
                            SALAD""",
            "Thursday": """POORI , PUNJABI ALOO MATTAR
                           KOVAKAI FRY *,
                           RICE,ANDHRA TOMATO DAL,RASAM, CURD,PAPAD
                           PULICHAKEERAI PICKLE
                           SUGAR ,SALT ,GHEE,PODI
                           JUICE""",
            "Friday": """PHULKA, MIX VEG MATAR
                         LAUKI CHANA DAL, GOBI 65*
                         RICE,RASAM, CURD,FRYUMS
                         MIXVEG PICKLE
                         SUGAR ,SALT ,GHEE,PODI
                         SALAD""",
            "Saturday": """CHAPATTI , MIX VEG CURRY
                           CHILLI SOYA BEAN DRY, PERUGU PACHADI
                           RICE,SAMBAR,RASAM, CURD,MASALA PAPAD
                           MANGO PICKLE
                           SUGAR ,SALT ,GHEE,PODI
                           JUICE""",
            "Sunday": """PHULKA, ALOO GOBI MATTAR (for veg only)
                         PANEER BIRYANI, RAITHA (For veg)
                         CHK BIRYANI, PL. GRAVY, RAITHA
                         EGG
                         JUICE"""
        }
    }

    # Get the current week number (odd or even)
    week_number = datetime.now().isocalendar()[1] % 2

    # Get the current day of the week and the corresponding mess menu
    day_of_week = datetime.today().strftime('%A')
    todays_menu = menu[f"Week {week_number+1}"][day_of_week]
    await update.message.reply_text(todays_menu)


async def snacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = {
        "Week 1": {
            "Monday": """ONION PAKODA
                         Tea, Coffee, Milk, Sugar""",
            "Tuesday": """BANANA BAJJI(2) / C CHUTNEY
                         Tea, Coffee, Milk, Sugar""",
            "Wednesday": """DAHI VADA
                         Tea, Coffee, Milk, Sugar""",
            "Thursday": """SWEET CORN (half piece-6cm)
                         Tea, Coffee, Milk, Sugar""",
            "Friday": """MIX VEG MAGGI (130 gm ) / TOMATO SAUCE
                         Tea, Coffee, Milk, Sugar""",
            "Saturday": """MILLET SNACK**
                         Tea, Coffee, Milk, Sugar""",
            "Sunday": """ALOO SAMOSA(1-150 GMS)/ GREEN CHUTNEY
                         Tea, Coffee, Milk, Sugar"""
        },
        "Week 2": {
            "Monday": """ONION PAKODA
                         Tea, Coffee, Milk, Sugar""",
            "Tuesday": """MIRCHI BAJJI (2) / C CHUTNEY
                         Tea, Coffee, Milk, Sugar""",
            "Wednesday": """SWEET CORN
                         Tea, Coffee, Milk, Sugar""",
            "Thursday": """ALOO SAMOSA/ TOMATO SAUCE
                         Tea, Coffee, Milk, Sugar""",
            "Friday": """CHANNA CHAT
                         Tea, Coffee, Milk, Sugar""",
            "Saturday": """DAHI VADA
                         Tea, Coffee, Milk, Sugar""",
            "Sunday": """PANCAKE(W JAM)
                         Tea, Coffee, Milk, Sugar"""
        }
    }

    # Get the current week number (odd or even)
    week_number = datetime.now().isocalendar()[1] % 2

    # Get the current day of the week and the corresponding mess menu
    day_of_week = datetime.today().strftime('%A')
    todays_menu = menu[f"Week {week_number+1}"][day_of_week]
    await update.message.reply_text(todays_menu)


async def dinner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = {
        "Week 1": {
            "Monday": """CHOLE BATURE, ONION MIRCH SALAD
                         WHITE RICE, SNAKE GOURD KOOTU
                         BUTTER MILK
                         BANANA""",
            "Tuesday": """PHULKA, MEAL MAKER CURRY***
                          VEG FRIED RICE, VEG BALL MANCHURIAN (2)
                          TOMATO,CHILLI SAUCE
                          CURD RICE , SWEET BOONDI""",
            "Wednesday": """PHULKA, PALAK PANEER* Or ANDHRA CHK*
                            VEG BIRYANI , RAITHA
                            FRENCH FRIES(120gm)*
                            BANANA""",
            "Thursday": """KAL DOSA,G CHUTNEY
                           RICE,SAMBAR, ALOO PODIMAS
                           PAPAD, BUTTERMILK
                           GULAB JAMUN(2)""",
            "Friday": """LACHA PARATHA ,VEG KOFTA*(2)
                         RICE, RASAM
                         RAITA,MASALA PAPAD
                         BADAM MILK HOT*""",
            "Saturday": """PULKA, PANEER BUTTER MASALA
                           RICE,SAMBAR, BUTTERMILK
                           FRYUMS,
                           BREAD HALWA""",
            "Sunday": """CHAPATTI , VEG CURRY
                         RICE,DAL,RASAM, BUTTERMILK,FRYUMS
                         PICKEL,GHEE
                         SEASONAL CUT FRUITS*/BANANA"""
        },
        "Week 2": {
            "Monday": """CHAPATTI, TOOR DAL , VEG KURMA
                         RICE, RASAM, PAPAD,CURD
                         MANGO PICKLE
                         GULAM JAMUN(2)""",
            "Tuesday": """PHULKA, KADAI PANEER,
                          VEG BIRYANI, CURD RICE
                          PICKLE, RAITA
                          BOOST*""",
            "Wednesday": """SPECIAL DINNER""",
            "Thursday": """DOSA, C CHUTNEY
                           PLAIN RICE,MIXED DAL
                           ALOO PEAS DRY
                           BUTTER MILK, CRISPY BREAD HALWA""",
            "Friday": """PHULKA, MIX VEG KURMA
                         MIX VEG FRIED RICE
                         VEG BALL MANCHURIAN*,BANANA(1)
                         TOMATO,CHILLY SAUCE
                         CURD RICE""",
            "Saturday": """CHAPPATI, CHANNA PEAS PALAK
                           DAL KICHICHADI, CURD RICE
                           ALOO 65, TOMATO PICKLE
                           PAPAD,""",
            "Sunday": """IDLY , G CHUTNEY, PODI, GHEE
                         RICE, SAMBAR , PAPAD,CURD
                         RED GINGER PICKLE
                         BADUSHA/BANANA"""
        }
    }

    # Get the current week number (odd or even)
    week_number = datetime.now().isocalendar()[1] % 2

    # Get the current day of the week and the corresponding mess menu
    day_of_week = datetime.today().strftime('%A')
    todays_menu = menu[f"Week {week_number+1}"][day_of_week]
    await update.message.reply_text(todays_menu)

if __name__ == '__main__':
    print('Starting Bot.......')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('breakfast', breakfast))
    app.add_handler(CommandHandler('lunch', lunch))
    app.add_handler(CommandHandler('snacks', snacks))
    app.add_handler(CommandHandler('dinner', dinner))

    print('Polling.....')
    app.run_polling(poll_interval=6)
