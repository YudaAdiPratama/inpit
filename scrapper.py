print ("")
print ("++++++---++++++++++++---++++++++++++---++++++++++++---+++++++++")
print ("+                   ___           ___                          +")
print ("-      ___         /  /\         /__/|                         -")
print ("+     /__/\       /  /:/_       |  |:|                         +")
print ("-     \  \:\     /  /:/ /\      |  |:|                         -")
print ("+      \  \:\   /  /:/ /:/_   __|__|:|                         +")
print ("-  ___  \__\:\ /__/:/ /:/ /\ /__/::::\____                     -")
print ("+ /__/\ |  |:| \  \:\/:/ /:/    ~\~~\::::/                     +")
print ("- \  \:\|  |:|  \  \::/ /:/      |~~|:|~~                      -")
print ("+  \  \:\__|:|   \  \:\/:/       |  |:|                        +")
print ("-   \__\::::/     \  \::/        |  |:|                        -")
print ("+       ~~~~       \__\/         |__|/                         +")
print ("-      ___           ___           ___           ___           -")
print ("+     /__/\         /  /\         /  /\         /__/\          +")
print ("-    |  |::\       /  /::\       /  /::\        \  \:\         -")
print ("+    |  |:|:\     /  /:/\:\     /  /:/\:\        \  \:\        +")
print ("-  __|__|:|\:\   /  /:/  \:\   /  /:/  \:\   _____\__\:\       -")
print ("+ /__/::::| \:\ /__/:/ \__\:\ /__/:/ \__\:\ /__/::::::::\      +")
print ("- \  \:\~~\__\/ \  \:\ /  /:/ \  \:\ /  /:/ \  \:\~~\~~\/      -")
print ("+  \  \:\        \  \:\  /:/   \  \:\  /:/   \  \:\  ~~~       +")
print ("-   \  \:\        \  \:\/:/     \  \:\/:/     \  \:\           -")
print ("+    \  \:\        \  \::/       \  \::/       \  \:\          +")
print ("-     \__\/         \__\/         \__\/         \__\/          -")
print ("++++++---++++++++++++---+++++++Yuda Adi Pratama+++++---++++++++++++---+++++++++")
print ("")

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

api_id = 36768769  #masukin 7 Digit Telegram API ID.
api_hash = '85c4b002cd166a42hgjfj61091e0028'   #masukin 32 karakter API Hash
phone = '+62'   #masukin nomer hp pakai kode negara.
client = TelegramClient(phone, api_id, api_hash)
async def main():

    await client.send_message('me', 'gasken !!!!')
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter verification code: '))


chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print('From Which Group Yow Want To Scrap A Members:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Please! Enter a Number: ")
target_group=groups[int(g_index)]

print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In file...')
with open("Scrapped.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
print('Members scraped successfully.......')
print('Happy Hacking......')
