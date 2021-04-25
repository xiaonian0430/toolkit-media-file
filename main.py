# encoding: utf-8
"""
@author: Xiao Nian
@contact: xiaonian030@163.com

@version: 1.0
@license: Apache Licence
@file: main.py
@time: 2021-04-25 13:00

"""
import os
import subprocess


def create_dir(path):
    os.makedirs(path, exist_ok=True)


def generate_m3u8(input_path, input_text):
    target_path = 'public_job/m3u8/' + input_text
    target_seg_path = target_path + '/segment'
    create_dir(target_seg_path)
    mp4_path = target_path + '/' + input_text + '.mp4'
    ts_path = target_path + '/' + input_text + '.ts'
    m3u8_path = target_seg_path + '/' + input_text + '.m3u8'
    m3u8_segment_path = target_seg_path + '/' + input_text + '_%03d.ts'
    other_2_mp4 = 'ffmpeg -i ' + input_path + ' -c:v copy -c:a copy ' + mp4_path
    mp4_2_ts = 'ffmpeg -i ' + mp4_path + ' -c copy -bsf:v h264_mp4toannexb ' + ts_path
    ts_2_m3u8 = 'ffmpeg -i ' + ts_path + ' -c copy -map 0 -f segment -segment_time 1 -segment_list ' + m3u8_path + ' ' + m3u8_segment_path
    subprocess.call(other_2_mp4, shell=True)
    subprocess.call(mp4_2_ts, shell=True)
    subprocess.call(ts_2_m3u8, shell=True)


def run():
    # 启动程序
    print('start')
    input_dir = 'public_job/input'
    for parent, dir_names, file_names in os.walk(input_dir):
        for file_name in file_names:
            input_path = input_dir + '/' + file_name
            input_text = os.path.splitext(file_name)[0]
            generate_m3u8(input_path, input_text)


if __name__ == "__main__":
    run()
