import sox

tfm = sox.Transformer()
info = sox.file_info.info('./original-audio/original-metadata.wav')

tfm.set_output_format(rate=info['sample_rate'], bits=info['bitrate'], channels=info['channels'], encoding='floating-point')
status = tfm.build(
    input_filepath='./original-audio/main-audio.wav',
    output_filepath='./original-audio/main-audio-transform.wav'
)

#
# {'channels': 1,
#  'sample_rate': 8000.0,
#  'bitrate': 32,
#   'num_samples': 44293,
#  'encoding': 'Floating Point PCM',
#  'silent': False}
# print(sample_rate)
print(status)
