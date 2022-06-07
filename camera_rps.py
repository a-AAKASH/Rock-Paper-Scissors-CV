import numpy as np

def get_prediction(prediction):
    pred = np.argmax(prediction[0], axis=0)
    if pred == 0:
        print('Rock')
        return 'Rock'
    elif pred == 1:
        print('Paper')
        return 'Paper'
    elif pred == 2:
        print('Scissors')
        return 'Scissors'
    else:
        print('Nothing')
        return 'Nothing'

