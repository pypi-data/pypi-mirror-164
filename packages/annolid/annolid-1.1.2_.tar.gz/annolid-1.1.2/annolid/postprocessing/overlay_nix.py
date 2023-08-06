import pandas as pd
import cv2 

df = pd.read_csv("~/Downloads/tNovel_Object_Test_1_3000iters_mask_rcnn_tracking_results_with_segmenation_nix.csv")

cap = cv2.VideoCapture("/Users/chenyang/Downloads/Novel Object Test 1_tracked.mp4")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
xac, yac = None, None
event = 'grooming'

while True:
    frame_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
    if cap.grab():
        flag, frame = cap.retrieve()
        
        if not flag:
            break
        else:
            # cv2.putText(frame, f"Timestamp: {frame_timestamp}",
            #         (25, 25), cv2.FONT_HERSHEY_SIMPLEX,
            #         0.65, (255, 255, 255), 2)
            
            df_cur = df[df['timestamps'].astype(str) == str(frame_timestamp)]
            if not df_cur.empty:
                xac = df_cur['pos:animal_nose:x'].values[0]
                yac = df_cur['pos:animal_nose:y'].values[0]
                # glitter y
                yac = (yac - height) * -1
            print(xac,yac)
            if xac and yac:
                cv2.putText(frame, f"{event}",
                        (xac,yac), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (255, 0, 0), 2)
            cv2.imshow('video', frame)
    if cv2.waitKey(10) == 27:
        break