import os

import cv2
import glob


def imgs2video(imgs_dir, save_name):
    
    fps = 10 # 1秒2桢
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    video_writer = cv2.VideoWriter(save_name, fourcc, fps, (800, 800))

    imgs = glob.glob(os.path.join(imgs_dir, '*.jpg'))
    print(imgs_dir)
    for i in range(len(imgs)):
        imgname = os.path.join(imgs_dir, '%d.jpg' % (i))
        print("deal:",imgname)
        frame = cv2.imread(imgname)
        video_writer.write(frame)
        #cv2.imshow("img",frame)
        #cv2.waitKey(fps)

    video_writer.release()
    print(save_name)

if __name__ == "__main__":
    main_path = os.getcwd()
    video_file = 6000
    video_path = os.path.join(main_path,'results/%d'%(video_file))
    video_save_path = os.path.join(main_path,'videos','%d.avi'%(video_file))
    imgs2video(video_path,video_save_path)
    
