import cv2

import tflite_runtime.interpreter as tflite
from pycoral.adapters import common
from pycoral.adapters import classify
from pycoral.utils.dataset import read_label_file


def take_picture(camera_object, input_image_size=(224,224)):
    
    return_status, picture = camera_object.read()
    
    picture_rgb = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    picture_rgb = cv2.resize(picture_rgb, input_image_size)
    
       
    return picture_rgb

def initialize_model(model_path='model_unquant.tflite', coral_accelerator = 0):
    
    if (coral_accelerator==1):
        interpreter = edgetpu.make_interpreter(model_path_or_content=model_path)
    else:
        interpreter = tflite.Interpreter(model_path=model_path)

    interpreter.allocate_tensors()
    #size = common.input_size(interpreter)
    
    return interpreter

def model_prediction(interpreter, picture_array):
    
    common.set_input(interpreter, picture_array)
    interpreter.invoke()
    prediction, probability = classify.get_classes(interpreter, top_k=1)[0]
        
    return prediction, probability
