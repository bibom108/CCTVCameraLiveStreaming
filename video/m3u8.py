from vidgear.gears import CamGear
from vidgear.gears import StreamGear
import cv2

stream = CamGear(source='http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg').start()
stream_params = {"-input_framerate": stream.framerate, "-livestream": True}
streamer = StreamGear(output="hls_out.m3u8", format = "hls", **stream_params)

while True:
    frame = stream.read()
    if frame is None:
        break
    streamer.stream(frame)
    
stream.stop()
streamer.terminate()