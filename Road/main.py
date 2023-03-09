import cv2 as cv
import numpy as np
import lanes


video = cv.VideoCapture("test.mp4")

if not video.isOpened():
    print('Error, video not found')

cv.waitKey(1)


while video.isOpened():
    abc, frame = video.read()
    if not abc:
    	break
    cv.namedWindow('video', cv.WINDOW_NORMAL)
    cv.resizeWindow('video', 1300, 800)
    copy_img = np.copy(frame)
    
    try:
       
        frame = lanes.canny(frame)
        frame = lanes.mask(frame)
        lines = cv.HoughLinesP(frame, 2, np.pi / 180, 100, np.array([()]), minLineLength=20, maxLineGap=5)        
        averaged_lines = lanes.average_slope_intercept(frame, lines)    
        line_image = lanes.display_lines(copy_img, averaged_lines)

        resul = cv.addWeighted(copy_img, 0.8, line_image, 1, 1)       
        cv.imshow("video", resul)
			    	
    except:
    	pass
    
    
    
    
    # cv.imshow('video', resul)
    # cv.imshow("video", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv.destroyAllWindows()

video.release()
cv.destroyAllWindows()
