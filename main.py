from asteroid import DPRNNTasNet
model = DPRNNTasNet.from_pretrained('mpariente/DPRNNTasNet_WHAM!_sepclean')
model.separate('./audio-data/audio-8bit.wav')