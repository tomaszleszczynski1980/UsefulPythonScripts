"""
    Srt to txt conversion.
    
    Function srtTooTxt clears from subtitles file (.srt) all timecode data.
    Can be imported as module or run as separate python3 script.

    Args:
        srt file (path) -> string.
    
    Returns:
        Pure text (.txt file format).
    
    Raises:
        TypeError if input file is not srt
        FileNotFoundError if input file not found.
"""


def srtToTxt (srt_file, txt_file='', overwrite=False):
    try:
        if srt_file.endswith('.srt'):
            if txt_file == '':
                txt_file = srt_file[:-3] + 'txt'

            with open (srt_file, 'r', encoding='utf-8') as src_file:
                 srt_text = src_file.readlines()[1:]

                 if exists(txt_file) and overwrite == False:
                     print (f'output file "{txt_file}" already exists')
                     print ('specify another name or set overwrite as "True"')

                 else:
                     with open (txt_file, 'w', encoding='utf-8') as output_file:
                         for item in srt_text:
                             
                             if not item[0].isdigit():
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
