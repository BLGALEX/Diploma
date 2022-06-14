import argparse


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
    
