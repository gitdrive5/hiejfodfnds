import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "tgnvsbot") 

DB_NAME = os.environ.get("DB_NAME","")     

DB_URL = os.environ.get("DB_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "600"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/df475b3dd8fea1634db46.png")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
