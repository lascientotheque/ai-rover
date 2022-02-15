#!/usr/bin/env python
# coding: utf-8

# # Télécommande sur page Web
# 
# 

# In[1]:


import time

import cv2

#from gpiozero import Motor
import gpiozero

#from flask import Flask, Response, render_template
import flask  


# In[2]:


left_motor = gpiozero.Motor(7, 8)
right_motor = gpiozero.Motor(9, 10)

motor_speed = 0.5


# In[3]:


def display_video():
    
    camera_object = cv2.VideoCapture(0)
    
    while True:
    
        ret, picture = camera_object.read()
        picture_rgb = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    
        ret, jpeg = cv2.imencode('.jpg', picture_rgb)
        pic = jpeg.tobytes()
        
        #Flask streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + pic + b'\r\n\r\n')


# In[4]:


app = flask.Flask("Remote control")


# In[5]:


@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return flask.Response(display_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/forward')
def forward():
    left_motor.forward(motor_speed)
    right_motor.forward(motor_speed)
    return ""
    
@app.route('/backward')
def backward():
    left_motor.backward(motor_speed)
    right_motor.backward(motor_speed)
    return ""
    
@app.route('/left')
def left():
    right_motor.forward(motor_speed)
    left_motor.stop()
    return ""
    
@app.route('/right')
def right():
    left_motor.forward(motor_speed)
    right_motor.stop()
    return ""
    
@app.route('/stop')
def stop():
    left_motor.stop()
    right_motor.stop()
    return ""


# In[6]:


app.run(host='0.0.0.0', port=2204, threaded=True, debug=False)


# In[ ]:




