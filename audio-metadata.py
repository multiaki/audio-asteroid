import audio_metadata

# metadata = audio_metadata.load('original-audio/original-metadata.wav')
metadata = audio_metadata.load('original-audio/original-audio.wav')

metadata

# <WAVEStreamInfo({
#     'audio_format': <WAVEAudioFormat.IEEE_FLOAT>,
#     'bit_depth': 32,
#     'bitrate': '256 Kbps',
#     'channels': 1,
#     'duration': '00:06',
#     'sample_rate': '8.0 KHz',
# })>
# <WAVEStreamInfo({
#     'audio_format': <WAVEAudioFormat.PCM>,
#     'bit_depth': 16,
#     'bitrate': '706 Kbps',
#     'channels': 1,
#     'duration': '00:18',
#     'sample_rate': '44.1 KHz',
# })>