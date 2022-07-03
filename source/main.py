import argparse
import os
from ctypes import FormatError
from pathlib import Path
from evs.FileEstimation import FileEstimator


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'


class Interface():
    def __init__(
        self,
        pathes: list[str | Path],
        cnn: str,
        split: bool,
        verbose: int = 0
    ):
        self.pathes = pathes
        self.cnn = cnn
        self.split = True
        self.verbose = verbose
        self._run_checks()

    def start_evaluation(self):
        if self.verbose > 0:
            print('Starting estimation of video stabilization..')
        model = FileEstimator(model_type=self.cnn, split_four=self.split, verbose=self.verbose)
        for path in self.pathes:
            score = model.evaluate(path)
            print(f'{path} \n score: {score}')

    def _run_checks(self):
        self._assert_video_exists()

    def _assert_video_exists(self):
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
        '--pathes',
        nargs='+',
        metavar='video1.mp4',
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
        metavar='resnet50',
        type=str,
        default='resnet50',
        help='Pretrained cnn to estimate video stabilization.'
        ' Default resnet50.'
        ' Avialable: seresnet18, resnet50'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        metavar='1',
        type=int,
        default=1,
        help='0 - only score, 1 - all logs'
    )

    args = parser.parse_args()

    interface = Interface(
        pathes=args.pathes,
        cnn=args.estimation_cnn,
        split=args.split_video,
        verbose=args.verbose
    )
    interface.start_evaluation()
