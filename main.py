import cv2
import os
import sys

def imageLoader(path_arg):
    try:
        inter_path = path_arg
        real_path = ""
        for path in inter_path:
            real_path = real_path+path+" "

        processed_folder_path = real_path.strip()
        split_list = processed_folder_path.split("\\")
        output_folder_name = os.path.join("OUTPUT_GRAY", split_list[-1])
        os.makedirs(output_folder_name)

        items = os.listdir(processed_folder_path)

        if len(items) == 1:
            print(f"[!] Found {len(items)} image [!]")
        else:
            print(f"[!] Found {len(items)} images [!]")


        images_path_list = []
        for image in items:
            item_path = os.path.join(processed_folder_path, image)
            images_path_list.append(item_path)

        return (images_path_list, items, output_folder_name)
    
    except Exception as err:
        print("[!] CHECK DATA FOLDER PATH ARGUMENT [!]") 

def makeGrayScale(path_list, item_list, output_folder_name):
    for path, name in zip(path_list, item_list):
        img = cv2.imread(path)
        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        save_loc = os.path.join(output_folder_name,name)

        cv2.imwrite(save_loc, gray_img)
        cv2.imshow("image", gray_img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
        path_arg = sys.argv[1:]
        try:       
            image_path_list, image_name_list, output_folder_name = imageLoader(path_arg)
            makeGrayScale(image_path_list, image_name_list, output_folder_name)
        except Exception as Err:
             print(Err)