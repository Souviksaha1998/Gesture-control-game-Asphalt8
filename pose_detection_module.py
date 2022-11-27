import  cv2
import mediapipe as mp
import time
import math
from controller import *





#initialization

draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()




def image_read(image,draws=False,detection=True):
    image_in_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if detection:
        result = pose.process(image_in_RGB)
        if result.pose_landmarks:
            for i in result.pose_landmarks.landmark:
                if draws:
                    # draw.draw_landmarks(image,i,mp_pose.POSE_CONNECTIONS,draw.DrawingSpec((0,0,255),3,2),draw.DrawingSpec((0,255,0),3,2))
                    draw.draw_landmarks(image,i,mp_pose.POSE_CONNECTIONS)
        return result,image
    return None



def findPose(img,raw,draws=False,detection=True):
    if detection:
        lmlist = []
        if img.pose_landmarks:
            
            for id , lm in enumerate(img.pose_landmarks.landmark):
                h,w,c = raw.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draws:
                    draw.draw_landmarks(raw,img.pose_landmarks,mp_pose.POSE_CONNECTIONS,draw.DrawingSpec((0,0,255),3,2),draw.DrawingSpec((0,255,0),3,2))
                    cv2.circle(raw,(cx,cy),5,(0,255,0),cv2.FILLED)
                    
        return lmlist
    return None




def main():     
                print("Program will start after 5sec..")
                time.sleep(5)
                cap = cv2.VideoCapture(0)
                ptime = 0
                              
                while True:
                    _ , frame = cap.read()
                    frame = cv2.flip(frame,1)
                    
                    
                    posed_detect , raws = image_read(frame,False)
                    lmlist = findPose(posed_detect,raws,False)
                    
                    
                        
                    if lmlist:
                        cx1 , cy1 = lmlist[15][1] , lmlist[15][2] #right hand wrist
                        cx2 , cy2 = lmlist[16][1] , lmlist[16][2] #left hand wrist
                         
                        
                        cv2.circle(raws,(cx1,cy1),10,(255,0,255),-1)
                        cv2.circle(raws,(cx2,cy2),10,(255,0,255),-1)
                        
      
                        p = math.atan2(cy1 - cy2, cx1 - cx2)
                        dist = math.sqrt( (cx2 - cx1)**2 + (cy2 - cy1)**2 )
                    
                    
                            
                        # cv2.putText(raws,str(int(dist)),(20,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                        
                        angle = int(math.degrees(p))
                        
                        # cv2.putText(raws,f'{str(int(angle))}',(cx-10,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                        if (cx1 and cy1) and (cx2 and cy2):
                            if int(dist) < 150:
                                print("Backward...")
                                cv2.putText(raws,'Backward...',(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                                backward()
                            
                                
                            elif int(dist) > 550:
                                print("Nitro...")
                                cv2.putText(raws,'Nitro....',(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                          
                                nitro()
                                
                            else:
                                if angle > 17:
                                    print("right hand up !!")
                                    cv2.putText(raws,'Right Move',(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                                    right()
                                        
                                                    
                                                        
                                
                                elif angle < -17:
                                    print("left movement!!")
                                    cv2.putText(raws,'Left Move',(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                                    left()
                                        
                                
                                elif 17 >= angle > -17               :
                                    print("Running..")
                                    cv2.putText(raws,'Running...',(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                                    forward()
                                
                     
                                
                            
                                
                    
                        
                            
                        ctime = time.time()
                        fps = 1/(ctime-ptime)
                        ptime = ctime
                        im = raws
                        cv2.putText(im,f'FPS : {str(int(fps))}',(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                        cv2.imshow('imge',im)
                        
                        
                        
                        if cv2.waitKey(1) == 27:
                            break
                        
                cap.release()
                cv2.destroyAllWindows()
            
             
        
    
if __name__ == '__main__':
    main()
    
    