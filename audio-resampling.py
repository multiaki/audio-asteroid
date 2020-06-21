import wave
wf = wave.open('./original-audio/original-audio.wav', 'wb')
wf.setnchannels(1)
wf.setsampwidth()
wf.setframerate(44100)
wf.writeframes(8000)
wf.setcomptype('NONE')
wf.close()

