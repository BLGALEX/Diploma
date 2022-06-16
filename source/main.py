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
        description='Script for estimation of video stabilization.'
        'Single avialable video extention is .mp4'
    )
    parser.add_argument(
        '-p',
        '--path',
        metavar='videofile',
        type=str,
        help='.mp4 file path'
    )
    parser.add_argument(
        '-s',
        '--split_video',
        action='store_true',
        help='Divides each frame into four,'
        ' getting four new videos.'
        ' Evaluates each of them and averages the score.'
        ' Improves accuracy, increases evaluation time.'
    )
    parser.add_argument(
        '-e',
        '--estimation_cnn',
        metavar='seresnet18',
        type=str,
        default='seresnet18',
        help='Pretrained cnn to estimate video stabilization.'
        ' Default seresnet18.'
        ' Avialable: seresnet18, seresnet50, resnet50'
    )

    args = parser.parse_args()
    
