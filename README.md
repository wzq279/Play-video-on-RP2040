准备<br>
====
1.树莓派PICO(RP2040)<br>
2.128*64分辨率，使用SSD1306的屏幕，I2C与SPI均可<br>
3.Thonny软件<br>

使用方法<br>
====
1.按住PICO上的bootset按钮，并连接数据线至电脑，电脑会识别到RPI-RP2，将RPI_PICO-20260406-v1.28.0.uf2复制进去，然后拔掉数据线，再重新连接<br>
<br>
3.在电脑上修改 视频转换.py 中的 INPUT_DIR ， OUTPUT_BIN ， OUTPUT_TXT ，并运行转换<br>
<br>
2.打开Thonny，将 ssd1306.py , main.py 和制作好的 video.bin , frame_count.txt 上传至PICO<br>
<br>
4.大功告成！<br>

注意事项<br>
====
1.PICO的存储容量有限，转换后的 video.bin 尽量小于1.3MB，否则存不下<br>
<br>
2.转换的视频应为黑白的，否则会出现奇妙小bug<br>
<br>
3.未完待续...<br>

作者: Bilibili: https://space.bilibili.com/3546622338271451<br>
<br>
      Github: https://github.com/wzq279<br>
----
演示视频: https://www.bilibili.com/video/BV15Cjw6zEKz<br>
