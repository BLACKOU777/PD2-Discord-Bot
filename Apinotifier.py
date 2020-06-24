import requests, json, re, discord
from datetime import datetime, timedelta
from dhooks import Webhook

pd2_server = Webhook('https://discordapp.com/api/webhooks/710131681012482141/iDdoBvAUPC0WYHJYWKJ9Ogmna6hpwPR0ZySkK-VqXFvaG4WFYbymQ74E4qlH8HLEL-Rf')
test_server = Webhook('https://discordapp.com/api/webhooks/713960600572788807/5hYpO46jd5rkM1MU5xRLqZ_hTQ_9sInGNRrpaeK4V0qkJTIiLvWkjVfTHGyDTOVNrYy3')
hook = pd2_server
response = requests.get("https://www.speedrun.com/api/v1/notifications", headers={'X-API-Key': 's89karnzlc4hfnkkb6sg0nxls'})
r_json = response.json()
for data in r_json['data']:
    created = data['created']
    if created > str(datetime.now()):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', data['text'])
        embed = discord.Embed(title=cleantext, url=data['item']['uri'])
        embed.set_author(name="Speedrun.com", url="https://www.speedrun.com", icon_url="https://www.speedrun.com/themes/Default/1st.png")
        hook.send(content=None, embed=embed)
