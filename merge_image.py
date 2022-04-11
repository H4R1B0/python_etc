import os
from PIL import Image

path_dir = ''


def merge(images, path, title):
    image_list = []
    full_width, full_height = 0, 0
    
    for image in images:
        image_path = path +'/'+ image
        im = Image.open(image_path)
        width, height = im.size
        image_list.append(im)
        full_width = max(full_width, width)
        full_height += height

    canvas = Image.new('RGB', (full_width, full_height), 'white')

    cursor_y = 0
    for im in image_list:
        width, height = im.size
        canvas.paste(im, (0, cursor_y))
        cursor_y += height

    canvas.save(title + '.png')
    #제목 파일 생성

path_dir = input() #합칠 이미지들이 들어있는 폴더 주소
folder_list = os.listdir(path_dir) #이미지들이 담겨있는 폴더 리스트
#index = 74
#각 폴더마다 리스트 불러오기
for folder in folder_list:    
    folder_path = path_dir +'/'+ folder
    file_list = os.listdir(folder_path)
    print(file_list)
    merge(file_list, folder_path, folder[7:])
    #merge(file_list, folder_path, folder[10:])
    #index = index + 1
