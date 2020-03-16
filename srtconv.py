import re
from csv import writer as csv_writer
from os.path import exists



def srt_txt(srt_content: str, noblanklines=True) -> str:

    txt_text = []
    for item in srt_content:
        if not item[0].isdigit():
            if noblanklines:
                txt_text.append(item[:-1])
            else:
                txt_text.append(item)

    if noblanklines:
        return ' '.join(txt_text)
    else:
        return ''.join(txt_text)


def srt_csv(srt_content: str) -> list:

    csv_list = []
    index = 0
    while index < len(srt_content):
        text = ''
        dialogue_list_line = []

        if srt_content[index][0].isdigit() and ':' not in srt_content[index]:
            index += 1

        elif srt_content[index][0].isdigit() and ':' in srt_content[index]:
            dialogue_list_line.append(srt_content[index][:8])
            index += 1

            while index < len(srt_content) and srt_content[index] != '\n':
                text += (srt_content[index][:-1] + ' ')
                index += 1
            if index < len(srt_content) and srt_content[index] == '\n':
                index += 1

            dialogue_list_line.append(text)
            csv_list += [dialogue_list_line]

        else:
            index += 1

    return csv_list


def load_srt(srt_file) -> list:

    try:
        if srt_file.endswith('.srt'):
            with open(srt_file, 'r', encoding='utf-8') as src_file:
                srt_text = src_file.readlines()
        else:
            raise TypeError

    except FileNotFoundError:
        raise FileNotFoundError

    return srt_text


def save_txt(txt_file: str, txt_content: str, overwrite=False):

    if exists(txt_file) and not overwrite:
        raise FileExistsError
    else:
        with open(txt_file, 'w', encoding='utf-8') as output_file:
            output_file.write(txt_content)


def save_csv(csv_file: str, csv_content: list, overwrite=False):

    if exists(csv_file) and not overwrite:
        raise FileExistsError
    else:
        with open(csv_file, 'w', encoding='utf-8') as output_file:
            write = csv_writer(output_file, delimiter=',', quotechar='"')
            write.writerow(['time code', 'text'])
            for item in csv_content:
                write.writerow(item)
