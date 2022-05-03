import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Script for video stabilization estimation'
    )
    parser.add_argument('path', metavar='videofile', type=str,
                        help='path to videofile to estimate')

    args = parser.parse_args()
    print(args.path)
