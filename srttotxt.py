from sys import argv
from os.path import exists 


# this function clears from subtitles file (.srt) all timecode data
# giving as an otuput pure text (.txt file format)

def srtToTxt (srt_file, txt_file = '', overwrite = False):

    try:
        if srt_file[-4:] == '.srt':

            if txt_file == '':
                txt_file = srt_file[:-3] + 'txt'

            with open (srt_file, 'r', encoding = 'utf-8') as src_file:
                 srt_text = src_file.readlines()

                 if exists(txt_file) and overwrite == False:
                     print (f'output file "{txt_file}" already exists')
                     print ('specify another name or set overwrite as "True"')

                 else:
                     with open (txt_file, 'w', encoding = 'utf-8') as output_file:
                         for item in srt_text:

                             if item[0].isalpha():
                                 output_file.write(item)

        else:
            print('invalid file type, need ".srt"')

    except TypeError as error:
        print (f'"{srt_file}" is invalid file name')

    except FileNotFoundError as error:
        print (f'{error}')


def main (argvs):
    if len(argvs) == 1:
        files = input('>>> ').split(' ')

    else:
        files = argvs[1:]

    try:
        srtToTxt(files[0], files[1])

    except IndexError:
        srtToTxt(files[0])


main(argv)
