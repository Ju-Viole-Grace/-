import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("빠트릴 준비")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕.흐음,넌 명단에 없군.")
    if message.content.startswith("!파이크"):
        await message.channel.send("나 말이지. 간단하게 설명하자면 \n유령이 되어 다가가다가\n작살로 찔러서\n바다의 물살을 복수할 놈들에게 맛보여준 다음에\n깊은 바다로 끌어 내려 **처형**시키는거지.\n남은 전리품들은 너네가 알아서 가지라고.")
    if message.content.startswith("!가렌"):
        await message.channel.send("그 데마시아의 장군? **단단해.**\n날 침묵시키더니\n믹서기마냥 갈더군.\n때려봤지만,이상한 방패가 날 가로막았어.\n결국 하늘에서 검이 날라오더군.\n그래도,*날 따라오지는 못하던데?*")
    if message.content.startswith("!갈리오"):
        await message.channel.send("흐음.그 조각상 말이군.\n어디선가 날아와 ~~데드풀이 좋아할 법한~~슈퍼 히어로 랜딩을 하더니\n날 들이 박았어.\n엄청난 모래바람속에서 그녀석을 따라가게 되었고,\n조각상이다 보니깐 주먹 한방이 아프더라고.\n*단단하지만 않으면 좋겠는데..*")
    if message.content.startswith("!갱플랭크"):
        await message.channel.send("그 **선장**녀석.\n멀리서 배럴을 터트리더니\n 어디선가 대포알이 떨어졌어.배도 참 많더라고.\n물살의 맛을 보여줄려 했더니 *만능 귤로* 씹어버렸어.\n이상한 총도 쏘던데,뭔지 모르겠어.따끔거리기만 해.\n한물 간듯 한데, 협곡에서는 안보이더군.")
    if message.content.startswith("!뮤트"):
        await message.channel.send("?mute @GPM567#3006 1st")
    if message.content.startswith("!언뮤트"):
        await message.channel.send("?unmute @GPM567#3006")
    if message.content.startswith("!이즈리얼"):
        await message.channel.send("통칭 노랑머리지.\n서폿 입장으로써 QW난사하다가 비전쓰고 끌리는거 보면 미치겠더라고.")
    if message.content.startswith("!이즈"):
        await message.channel.send("~~**많고 많은 마법사 들중 내가 제일 잘났 지**~~")
    if message.content.startswith("!많고많은마법사들중내가제일잘났지"):
        await message.channel.send("그런 건 상대편한테나 하라고. ***처형시키기 전에.***")
client.run("NjkwMDkyMjY2MDUxNjAwNTcx.XnMZsQ.0_vcKEidGIF4WSjsdjKs7JxMlXo")