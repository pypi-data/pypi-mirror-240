__version__ = '0.1.1'

#Default credentials
mqtt_config = {"broker":"test.mosquitto.org","port":1883,"user":None,"passw":None,"basepath":"datadirectory"}

# This function implements basic mqtt functionality.
# Our own alternative Subscribe function will let you handle the incomming data with a callback function.
# The Get function will Subscribe and then allow you to automatically unsibscribe once we recieve data. A good option for statics files.

import paho.mqtt.client as mqtt
import json
import traceback
#import sys
import time
#from IPython.display import Image, display, clear_output
#import numpy as np
import datetime
import pytz

import imghdr
import io
import threading
import pandas as pd

def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter

_is_notebook = is_notebook()

if  _is_notebook:
    from IPython.display import Image, display, clear_output



def payload_is_jpg(data):

        o = io.BytesIO(data)

        if imghdr.what(o) == "jpeg":
            return True

        return False

lastpayload = None

def default_handler(topic,payload):
    global lastpayload
    lastpayload = payload
    if payload_is_jpg(payload):
        display(Image(payload))
        return


    print(topic)
    print("_"*len(topic))

    try:
        data = json.loads(payload)

        print(json.dumps(data,indent=2))
        #return json.dumps(data,indent=2)
        return
    except:
        pass

    try:

        print(payload.decode("utf-8"))
        #return payload.decode("utf-8")
        return
    except:
        pass

    print(payload)
    #return payload
    return

class GetObject():
    def __init__(self,topic,handler = None):
      self.event = threading.Event()
      self.topic = topic
      self.payload = None

      if handler == None:
        self.handler = self.update
      else:
        self.handler = handler

    def update(self,topic,payload):
      self.payload = payload
      self.event.set()


class MqttProccessor(mqtt.Client):
    def __init__(self,broker=mqtt_config["broker"],port=mqtt_config["port"],user=mqtt_config["user"],passw=mqtt_config["passw"],basepath=mqtt_config["basepath"]):
        super().__init__()

        self.basepath = basepath
        self.broker = broker

        self.default_timezone = pytz.timezone('Europe/Stockholm')
        self.retain = True
        self.retained = {}

        self.debug_msg = []
        self.debug = False
        self.lasttopic = ""

        self.subscriptions = {}
        self.gets = []

        self.username_pw_set(username=user,password=passw)
        self.connect(broker, port, 60)

        self.loop_start()

    def on_connect(self, mqttc, obj, flags, rc):
        #Subscribing to all topics that we are currently using.
        for topic in self.subscriptions.keys():
          self.subscribe(topic)

    def Subscribe(self,topic,handler=default_handler,buffer = False):
        #Already subscribed to topic?
        if topic in self.subscriptions.keys():
          if not handler in self.subscriptions[topic]:
            self.subscriptions[topic].append(handler)

            if not buffer:
              self.subscribe(topic)
            elif topic in self.retained.keys():
              if callable(handler):
                handler(topic,self.retained[topic])
        else:
          self.subscriptions[topic] = [handler]
          self.subscribe(topic)

    def Get(self,topic,blocking = True, handler=default_handler, timeout = 10):
      #Add to gets list unsubscribe directly when message is recived.

      get_obj = GetObject(topic,handler)

      self.gets.append((topic,get_obj))

      self.Subscribe(topic,get_obj.update)

      if blocking:
        if get_obj.event.wait(timeout = timeout) == False:
          print("Timeout")
          self.Unsubscribe(topic,get_obj.update)


        if handler == None:
          return get_obj.payload
        elif callable(get_obj.handler):
          return get_obj.handler(topic,get_obj.payload)

        return None

    def GetDataFrame(self,topic, timeout = 10):
      data = self.Get(topic,blocking = True, handler=None, timeout = timeout,)
      df = pd.read_json(data.decode("utf-8"),lines=True,orient= "records")
      df.index = pd.to_datetime(df["time"],unit="s")
      return df

    def GetDataFrameAt(self,topic,ts, timeout = 10):
      data = self.Get(self.GetTimeIndexPath(topic,ts),blocking = True, handler=None, timeout = timeout,)
      df = pd.read_json(data.decode("utf-8"),lines=True,orient= "records")
      df.index = pd.to_datetime(df["time"],unit="s")
      return df

    def Unsubscribe(self,topic,handler=default_handler):
        if not topic in self.subscriptions.keys():
          return

        if not handler in self.subscriptions[topic]:
          return

        self.subscriptions[topic].remove(handler)

        #Should we unsubscribe?
        if len(self.subscriptions[topic]) == 0:

          #Avoid error while iterating in on_message.
          subscriptions = self.subscriptions.copy()
          del subscriptions[topic]
          self.subscriptions = subscriptions

          self.unsubscribe(topic)

    def on_message(self, mqttc, obj, msg):
      try:

        if self.debug>0:
          print(str(int(time.time())) + " Update recived: " + msg.topic)
          self.debug_msg.append(str(int(time.time())) + " Update recived: " + msg.topic)
          self.debug_msg = self.debug_msg[-10:]

        if self.retain:
          self.retained[msg.topic] = msg.payload

        ToBeUnsubscribed = []

        #Call all handlers attached to the topic.
        if msg.topic in self.subscriptions.keys():
          for handler in self.subscriptions[msg.topic]:

            if callable(handler):
                handler(msg.topic,msg.payload)

            if (msg.topic,handler) in self.gets:
              ToBeUnsubscribed.append((msg.topic,handler))

        for (topic,handler) in ToBeUnsubscribed:
          self.gets.remove((topic,handler))
          self.Unsubscribe(topic,handler)

        self.lasttopic = msg.topic;
      except:
        traceback.print_exc()


    def find(self,name,handler=default_handler,basepath = None):
        if basepath ==None:
            basepath = self.basepath + "/"
        #print(basepath + "?find=\"" + name +"\"")
        self.Get(basepath + "?find=\"" + name +"\"",handler)

    def ls(self,topic,handler=default_handler):
        self.Get(topic + "/",handler)

    def GetLogAt(self,topic,epoc_time,handler=default_handler):

        self.Get(self.GetTimeIndexPath(topic,epoc_time),handler)

    def GetFilesAt(self,topic,epoc_time,handler=default_handler):

        self.Get(self.GetTimeIndexPath(topic,epoc_time)+ "/",handler)

    def GetTimeIndexPathFromDataTime(self,topic,localtime):
        return topic + "/TimeIndex/" + str(localtime.year) + "/" +  str(localtime.month).zfill(2) + "/" + str(localtime.day).zfill(2) + "/" + str(localtime.hour).zfill(2)

    def GetTimeIndexPath(self,topic,epoc_time):
        date_time = datetime.datetime.fromtimestamp( epoc_time )
        localtime = date_time.astimezone(self.default_timezone)
        return self.GetTimeIndexPathFromDataTime(topic,localtime)
