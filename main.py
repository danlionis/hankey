import os
import interactions
from interactions.ext.lavalink import VoiceClient


client = VoiceClient(
    token=os.environ["TOKEN"],
    default_scope=int(os.environ["GUILD"]))


client.load("exts.music")

client.start()
