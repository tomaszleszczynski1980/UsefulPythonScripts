"""
    Srt to txt conversion.
    
    Function srtTooTxt clears from subtitles file (.srt) all timecode data.
    Can be imported as module or run as separate python3 script.

    Args:
        srt file (path) -> string.
    
    Returns:
        Answer - message
        Writes pure text (.txt file format).
    
    Raises:
        TypeError if input file is not srt
        FileNotFoundError if input file not found.
"""

from os.path import exists


def srtToTxt(srt_file, txt_file='', overwrite=False, noblanklines=True):
    txt_text = []
    try:
        if srt_file.endswith('.srt'):
            if txt_file == '':
                txt_file = srt_file[:-3] + 'txt'

            with open(srt_file, 'r', encoding='utf-8') as src_file:
                srt_text = src_file.readlines()

            if exists(txt_file) and overwrite == False:
                answer = f'output file "{txt_file}" already exists specify another name or set overwrite as "True"'

            else:  # format conversion
                for item in srt_text:
                    if not item[0].isdigit():
                        if noblanklines:
                            txt_text.append(item[:-1])
                        else:
                            txt_text.append(item)

                with open(txt_file, 'w', encoding='utf-8') as output_file:
                    if noblanklines:
                        output_file.write(' '.join(txt_text))
                    else:
                        output_file.write(''.join(txt_text))

                answer = f'{srt_file} converted to {txt_file}'

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
        print(srtToTxt(files[0], files[1]))
    except IndexError:
        print(srtToTxt(files[0]))


if __name__ == '__main__':
    from sys import argv

    main(argv)