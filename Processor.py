import sys
import cv2

from utils.Constants import ProcessorConstants as Constants


class Processor:

    def __init__(self, detector, verbose=False):
        print("Initializing the processor with detector: ", detector.getName())

        self.verbose = verbose
        self.process(detector)

    def process(self, detector):
        print("Starting processing...")

        for i in range(0, Constants.NUMBER_OF_FRAMES):
            if self.verbose:
                Processor.notifyProgress("Processing image: " + str(i + 1))
            path = Constants.FILE_PATH_TEMPLATE.replace('{NUMBER}', '%06d' % i)
            detector.process(path)
            cv2.waitKey(33)

        cv2.destroyAllWindows()

    @staticmethod
    def notifyProgress(message):
        sys.stdout.write("\r" + message)
        sys.stdout.flush()
