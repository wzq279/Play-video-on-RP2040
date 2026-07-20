import os
import re
from PIL import Image

INPUT_DIR = "frames文件夹路径"
OUTPUT_BIN = "输出路径/video.bin"
OUTPUT_TXT = "输出路径/frame_count.txt"

THRESHOLD = 60

def extract_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

def main():
    images = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.bmp')]
    if not images:
        print("错误：没有 .bmp 文件")
        return
    images.sort(key=extract_number)
    print(f"找到 {len(images)} 张图片")

    frame_data = bytearray()
    for img_name in images:
        with Image.open(os.path.join(INPUT_DIR, img_name)) as img:
            #转为灰度图
            img = img.convert('L')
            if img.size != (128, 64):
                img = img.resize((128, 64), Image.Resampling.LANCZOS)

            #打包
            for page in range(8):
                for x in range(128):
                    byte = 0
                    for bit in range(8):
                        y = page * 8 + bit
                        gray = img.getpixel((x, y))
                        if gray > THRESHOLD:
                            byte |= (1 << bit)
                    frame_data.append(byte)

    with open(OUTPUT_BIN, 'wb') as f:
        f.write(frame_data)
    with open(OUTPUT_TXT, 'w') as f:
        f.write(str(len(images)))

    print(f"完成！共 {len(images)} 帧，数据大小 {len(frame_data)} 字节")

if __name__ == "__main__":
    main()
