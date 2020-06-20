from asteroid import DPRNNTasNet

model = DPRNNTasNet.from_pretrained('mpariente/DPRNNTasNet_WHAM!_sepclean')


def main(args):
    convert(args[0])


def convert(filename):
    model.separate('./audio-data/'+filename)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
