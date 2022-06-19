import os
import io
from pathlib import Path

dirname = "D:\\pycharmTests\\HW with files\\win_test"
dir_files = os.listdir(dirname)
full_path_out_file = "D:\\pycharmTests\\HW with files\win_test\\result.txt"

full_paths = map(lambda name: os.path.join(dirname, name), dir_files)
file_rows_cnt_dict = {}
for file in full_paths:
    with io.open(file, encoding="utf-8") as cur_file:
        cur_lines = cur_file.readlines()
        cnt = len(cur_lines)
        if cnt in file_rows_cnt_dict.keys():
            tmp_test = []
            tmp1 = file_rows_cnt_dict.get(cnt)
            for tmp_file_path in tmp1:
                tmp_test.append(tmp_file_path)
            tmp_test.append(file)
            tmp_list = tmp_test
        else:
            tmp_list = [file]
        file_rows_cnt_dict.update({cnt: tmp_list})
sort_dict = dict(sorted(file_rows_cnt_dict.items()))

with open(full_path_out_file, 'w', encoding="utf-8") as res_file:
    for key in sort_dict:
        files = sort_dict[key]
        for file in (files):
            with open(file, encoding="utf-8") as inp_file:
                res_file.write(Path(inp_file.name).name + '\n')
                res_file.write(f'{key}\n')
                text = inp_file.read()
                res_file.write(text + '\n')
