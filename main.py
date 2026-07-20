from ssd1306 import SSD1306_I2C
from machine import I2C, Pin
import time
import framebuf
import neopixel

pixel_pin = 16
led_count = 1
np = neopixel.NeoPixel(machine.Pin(pixel_pin), led_count)
np[0] = (10, 0, 0)
np.write()

#速度控制（秒/帧）
FRAME_DELAY = 0.1452

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=1000000)
oled = SSD1306_I2C(128, 64, i2c)

try:
    with open('frame_count.txt', 'r') as f:
        total_frames = int(f.read().strip())
except Exception as e:
    print("读取 frame_count.txt 失败:", e)
    total_frames = 0
if total_frames == 0:
    print("没有有效帧数，退出")
else:
    print(f"准备播放动画，共 {total_frames} 帧，每帧延迟 {FRAME_DELAY} 秒")
frame_size = 1024

try:
    with open('video.bin', 'rb') as f:
        start = time.ticks_ms()
        for i in range(total_frames):
            data = f.read(frame_size)
            if not data or len(data) < frame_size:
                print(f"第 {i+1} 帧数据不完整，停止")
                break
            fb = framebuf.FrameBuffer(bytearray(data), 128, 64, framebuf.MONO_VLSB)
            oled.framebuf.blit(fb, 0, 0)
            oled.show()
            time.sleep(FRAME_DELAY)
        elapsed = time.ticks_diff(time.ticks_ms(), start) / 1000
        print(f"播放完成，耗时 {elapsed:.2f} 秒，实际平均帧率 {total_frames / elapsed:.1f} fps")

except Exception as e:
    print("播放过程中出错:", e)
    import sys
    sys.print_exception(e)
