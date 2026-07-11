from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=8862783946:AAFcvru8_iXVBW1R0vwHiao2Ma9VC38phlE)


async def send_signal(result, final, rug):

    message = f"""
🚀 Xiarou Scanner AI

━━━━━━━━━━━━━━

AI SCORE : {final['ai_score']}/100

SIGNAL : {final['signal']}

CONFIDENCE : {final['confidence']}%

━━━━━━━━━━━━━━

Risk : {rug['risk_level']}

Liquidity : ${result['liquidity']:,}

Volume : ${result['volume']:,}

FDV : ${result['fdv']:,}

24H : {result['change']}%

━━━━━━━━━━━━━━

Reason

"""

    for r in result["reasons"]:
        message += f"\n✅ {r}"

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )
