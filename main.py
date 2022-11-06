import os
import interactions
from interactions.ext.lavalink import VoiceClient


print("hello world")
client = VoiceClient(
    token=os.environ["TOKEN"],
    default_scope=int(os.environ["GUILD"]),
    intents=interactions.Intents.DEFAULT
    )

client.load("exts.music")

client.start()
