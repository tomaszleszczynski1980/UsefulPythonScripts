"""
    Srt to dialogue list conversion.

    Function srtToDL clears from subtitles file (.srt) subtitles screen number
    as well as other non-text except enter time-code.
    Can be imported as module or run as separate python3 script.

    Args:
        srt file (path) -> string.

    Returns:
        Dialogue list (.csv file format).

    Raises:
        TypeError if input file is not srt
        FileNotFoundError if input file not found.
"""

import csv
from os.path import exists


def srtToDL(srt_file, csv_file='', overwrite=False):

    try:
        if srt_file.endswith('.srt'):
            if csv_file == '':
                csv_file = srt_file[:-3] + 'csv'

            with open(srt_file, 'r', encoding='utf-8') as src_file:
                srt_text = src_file.readlines()

            if exists(csv_file) and not overwrite:
                answer = f'output file "{csv_file}" already exists specify another name or set overwrite as "True"'
            else:     # format conversion
                csv_list = []
                index = 0

                while index < len(srt_text):
                    text = ''
                    dialogue_list_line = []

                    if srt_text[index][0].isdigit() and ':' not in srt_text[index]:
                        index += 1
                        
                    elif srt_text[index][0].isdigit() and ':' in srt_text[index]:
                        dialogue_list_line.append(srt_text[index][:8])
                        index += 1

                        while index < len(srt_text) and srt_text[index] != '\n':
                            text += (srt_text[index][:-1] + ' ')
                            index += 1
                        if index < len(srt_text) and srt_text[index] == '\n':
                            index += 1

                        dialogue_list_line.append(text)
                        csv_list += [dialogue_list_line]
                            
                    else:
                        index += 1

                with open(csv_file, 'w', encoding='utf-8') as out_file:  # output file save
                    write = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    write.writerow(['time code', 'text'])
                    for item in csv_list:
                        write.writerow(item)

                answer = f'{srt_file} converted to {csv_file}'

        else:
            answer = 'invalid file type, need ".srt"'

    except TypeError:
        answer = f'"{srt_file}" is invalid file name'
    except FileNotFoundError as error:
        answer = f'{error}'

    return answer


def main(argvs):
    if len(argvs) == 1:
        files = input('srt file path>>> ').split(' ')
    else:
        files = argvs[1:]
    try:
        print(srtToDL(files[0], files[1]))
    except IndexError:
        print(srtToDL(files[0]))


if __name__ == '__main__':
    from sys import argv

    main(argv)
