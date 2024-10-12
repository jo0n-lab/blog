import matplotlib.pyplot as plt
from PIL import Image
import glob
import re

# 이미지 파일 경로 설정 (static/images/ 경로 내의 png 파일들을 모두 찾음)
# 숫자를 기준으로 정렬하는 함수 정의
def natural_sort_key(file):
    # 숫자가 포함된 부분을 찾아서 정렬 기준으로 삼음
    return [int(text) if text.isdigit() else text for text in re.split(r'(\d+)', file)]

# 이미지 파일 경로 설정 (static/images/ 경로 내의 png 파일들을 모두 찾음)
image_files = sorted(glob.glob('./static/images/bar_*.png'), key=natural_sort_key)

# 이미지 객체 리스트 생성
images = [Image.open(img) for img in image_files]

# GIF 저장 (첫 번째 이미지를 기반으로 나머지 이미지를 추가)
gif_path = './static/images/animated_bar_chart.gif'
images[0].save(gif_path, save_all=True, append_images=images[1:], duration=10, loop=0)

print(f"GIF 생성 완료: {gif_path}")