import argparse
from ctypes import FormatError
from pathlib import Path
import os


class Interface():
    def __init__(
        self,
        pathes: list[str | Path],
        cnns: list[str],
        transformers: list[str]
    ):
        self.pathes = pathes
        self.cnns = cnns
        self.transformers = transformers
        self.assert_video_exists()

    def evaluate(self):
        print('Starting estimation of video stabilization..')
        for cnn in self.cnns:
            for transforer in self.transformers:
                for path in self.pathes:
                    pass

    def assert_video_exists(self):
        for video in self.pathes:
            if not os.path.exists(video):
                raise FileNotFoundError(f'Can not find {video}')
            if video[-4:] != '.mp4':
                raise FormatError(f'{video} \n Only .mp4 files supports')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Script for video stabilization estimation'
    )
    parser.add_argument('path', metavar='videofile', type=str,
                        help='path to videofile to estimate')

    args = parser.parse_args()
    print(args.path)
