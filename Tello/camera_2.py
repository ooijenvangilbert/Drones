import sys
import traceback
import tellopy

import cv2 
import numpy
import time


def main():
    drone = tellopy.Tello()

    try:
        drone.connect()
        drone.wait_for_connection(60.0)

        stream = drone.get_video_stream()


        while True:
            frame = stream.read()
            image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
            cv2.imshow('Original', image)
            cv2.imshow('Canny', cv2.Canny(image, 100, 200))
            cv2.waitKey(1)

                    

    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print(ex)
    finally:
        drone.quit()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()