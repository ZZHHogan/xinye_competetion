import cv2
import json


train_path = "E:/Datasets/xinyegoods/dataset/train/"
json_train = train_path + 'b_annotations.json'


with open(json_train, 'r', encoding='utf8')as fp:
    trainJson = json.load(fp)
#     for i in range(len(trainJson['images'])):
#         images_id = trainJson['images'][i]['id']
#         images_file_name = trainJson['images'][i]['file_name']
#         width = trainJson['images'][i]['width']
#         height = trainJson['images'][i]['height']
#         print("images id : ", images_id)
#         print("images file_name : ", images_file_name)
#         print("width, height : ", width, height)
#
#         image_path = train_path + 'a_images/' + images_file_name
#         with open('xinye.txt', 'a') as f:
#             f.write(image_path)
#             for j in range(len(trainJson['annotations'])):
#                 if trainJson['annotations'][j]['image_id'] == i:
#                     bbox = trainJson['annotations'][j]['bbox']
#                     label = str(trainJson['annotations'][j]['category_id'])
#                     f.write(' ' + str(int(bbox[0])) + ',' + str(int(bbox[1])) + ',' +
#                             str(int(bbox[0] + bbox[2])) + ',' + str(int(bbox[1] + bbox[3])) + ',' + label)
#             f.write('\n')

    for i in range(len(trainJson['categories'])):
            # print("categories id : ", trainJson['categories'][i]['id'])
            # print(i)
            print(trainJson['categories'][i]['name'])