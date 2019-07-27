from time import sleep
from io import BytesIO
from datetime import datetime
from picamera import PiCamera

def take_photo():
    date_str = "{0:%Y/%m/%d %H:%M:%S}".format(datetime.now())
    with PiCamera() as camera:
        my_stream = BytesIO()
        camera.iso = 800
        camera.flash_mode = 'on'
        camera.annotate_text = date_str
        camera.capture(my_stream, 'jpeg')
    return my_stream
