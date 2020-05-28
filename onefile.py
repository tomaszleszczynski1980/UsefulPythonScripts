def mergeFiles(filesNames: list, destinationFilename: str, srtFilter=False):

    counter = 1

    try:
        with open(destinationFilename, 'w') as wfile:

            for filename in filesNames:

                with open(filename, 'r') as rfile:
                    lines = rfile.readlines()

                    for line in lines:
                        if srtFilter:
                            if line[0].isdigit():
                                line = str(counter)
                                counter += 1

                        wfile.write(line)
                    
    except FileNotFoundError:
        return False

    return True


def main():
    filesNames = input('Input files names (comma separated): ')
    filesNames = filesNames.split(', ')
    destinationFilename = input('Input destination file: ')

    success = mergeFiles(filesNames, destinationFilename)

    if success:
        print('Merge successful')
    else:
        print('Error')


if __name__ == '__main__':
    main()
