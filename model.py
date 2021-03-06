import camera_rps
import time 
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

duration = 5 ##the amount of time the computer will wait for you to show your choice among Rock,Paper or Scissors

while True: 
    ret, frame = cap.read() 

    start_time = time.time() ##starting time for the script
    diff = (time.time() - start_time)
    
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data) 
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    camera_rps.get_prediction(prediction) # Using the function defined in camera_rps to get the prediction for the sign shown in camera. 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # end_time = time.time() ##ending time for the script
    # time_elapsed = end_time - start_time ## the difference will give the total time the script has started
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        while (diff <= duration):
            user_choice = prediction

    
    # print("Time elapsed: ",time_elapsed)


#timing the script run
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

