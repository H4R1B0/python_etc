#pip install Pillow
from PIL import Image
import os


# 이미지 리스트 -> PDF
def img_to_pdf(folder_path, file_list):
    im = Image.open(folder_path + '\\' + file_list[0])  # 첫번째 이미지 기준
    im = im.convert('RGB')

    img_pdf_list = []  # pdf로 만들 이미지 배열

    # img_pdf_list에 이미지 추가
    for i in range(1, len(file_list)):
        img = Image.open(folder_path + '\\' + file_list[i])
        img_pdf_list.append(img.convert('RGB'))
        # print(folder_path+'\\'+file_list[i])

    # pdf로 저장
    im.save('result.pdf', save_all=True, append_images=img_pdf_list)


folder_path = input('폴더 경로 입력 : ')  # 합칠 이미지 폴더 경로 입력
file_list = os.listdir(folder_path)  # 폴더 안 파일 불러오기

img_to_pdf(folder_path, file_list)
