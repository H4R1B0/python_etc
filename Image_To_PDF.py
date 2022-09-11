from PIL import Image
import os

#이미지 리스트 -> PDF
def img_to_pdf(folder_path,num,file_list):
    folder_path = folder_path+'\\'+num #이미지를 열 폴더 경로
    im = Image.open(folder_path+'\\'+file_list[0]) #첫번째 이미지 기준
    im = im.convert('RGB')

    img_pdf_list = [] #pdf로 만들 이미지 배열
    
    #img_pdf_list에 이미지 추가
    for i in range(1,len(file_list)):
        img = Image.open(folder_path+'\\'+file_list[i])
        img_pdf_list.append(img.convert('RGB'))
        #print(folder_path+'\\'+file_list[i])
    
    #pdf로 저장
    im.save('제목 ' + num +'권.pdf',save_all=True, append_images = img_pdf_list)

folder_path = input('폴더 경로 입력 : ') #합칠 이미지 폴더 경로 입력
folder_list = os.listdir(folder_path) #폴더 안 폴더들 불러오기
folder_list.sort()

#폴더들 불러오기
for i in folder_list:
    print(i+'권 작업 시작')
    file_list = os.listdir(folder_path+'\\'+i) #폴더 안 이미지들 불러오기
    img_to_pdf(folder_path,i,file_list)
    print(i+'권 작업 끝')
#print(file_list)

#img_to_pdf(file_list)
