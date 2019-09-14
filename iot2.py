import cv2

background = None
accum_wt = 0.5

roi_top = 50
roi_bottom = 200
roi_left = 100
roi_right = 500

def cal_avg(frame, accum_wt):
	
	global background
	
	if background is None:
		background = frame.copy().astype('float')	
		return None
		
	cv2.accumulateWeighted(frame,background,accum_wt)
	
def segment(frame, thresh_min = 50):
	diff = cv2.absdiff(background.astype('uint8'),frame)
	
	#thresholded=cv2.Canny(diff,50,200)
	ret, thresholded = cv2.threshold(diff,thresh_min,255,cv2.THRESH_BINARY)
	
	_,cont,_ = cv2.findContours(frame.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	if len(cont) is None:
		return None
		
	else:
		hand_segment = cont
		
		return (thresholded, hand_segment)
		
		
cap = cv2.VideoCapture(0)

frame_count = 0

while True:
	ret, frame = cap.read()
	frame_copy = frame.copy()
	roi = frame[roi_top:roi_bottom,roi_left:roi_right]
	gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray,(7,7), 0)
	
	if frame_count <60:
		cal_avg(gray,accum_wt)
		if frame_count <= 59:
			cv2.putText(frame_copy, "WAIT", (200,300),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,0,255), 2)
			
			cv2.imshow("Live", frame_copy)
			
	else:
		hand = segment(gray)
		
		if hand is not None:
			thresholded , hand_seg = hand
			_,cont,_ = cv2.findContours(thresholded, cv2.cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
			
			if len(cont) != 0:
				for c in cont:
					if cv2.contourArea(c) > 100:
						cv2.putText(frame,"ALERT 1",(200,300),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 2)
						(x,y,w,h) = cv2.boundingRect(c)
						cv2.rectangle(roi,(x,y),(x+y,w+h),(255,0,0),3)
		cv2.rectangle(frame,(100,50),(500,200), (0,255,0), 3)
		cv2.imshow("Live",frame)
		
		
		#cv2.imshow("Live2",gray)
	frame_count +=1
	
	if cv2.waitKey(1) & 0xFF == 27:
		break
		
cap.release()
cv2.destroyAllWindows()						
	
	
	
	
	
	
