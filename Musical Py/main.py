from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav('Portal_still_alive.mp3')
play(song)