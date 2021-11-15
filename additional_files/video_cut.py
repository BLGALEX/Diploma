import cv2 as cv


class VideoTransformer:

    def __init__(self, fps=30, height=100, width=100, is_crop=False):
        self.fps = fps
        self.height = height
        self.width = width

        self.is_crop = is_crop

    def transform(self, path, inplace=False):
        cap = cv.VideoCapture(path)
        if not inplace:
            path, _ = path.split(sep='.')
            path += '_transformed'+'.'+_
        out = cv.VideoWriter(path, -1, self.fps, (self.width, self.height))
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                dim = (self.width, self.height)
                frame_re = cv.resize(frame, dim)
                out.write(frame_re)
            else:
                break
        cap.release()
        out.release()
        cv.destroyAllWindows()

    def get_cut(self, path):
        pass
