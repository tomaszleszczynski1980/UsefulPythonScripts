def getHourMinuteSecondFrames(timecode: str):

    timecodeNoFrames = timecode[:8]
    timecodeFrames = timecode[9:]

    timecodeSplit = timecodeNoFrames.split(':')

    hour = int(timecodeSplit[0])
    minute = int(timecodeSplit[1])
    second = int(timecodeSplit[2])

    return hour, minute, second, timecodeFrames


def updateTimecode(timecodeIn: tuple, startTimecode: tuple):

    second = timecodeIn[2] + startTimecode[2]

    minute = timecodeIn[1] + startTimecode[1]
    if second > 59:
        minute += 1
        second -= 60

    hour = timecodeIn[0] + startTimecode[0]
    if minute > 59:
        hour +=1
        minute -= 60

    ret_str = str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2) + ',' + timecodeIn[3]

    return ret_str


def globalizeTimecode(filename: str, start_timecode: str):

    start_timecode = start_timecode.split(':')
    
    try:
        start_hour = int(start_timecode[0])
        start_minute = int(start_timecode[1])
        start_second = int(start_timecode[2])

        if (start_minute < 0 or start_minute > 59) or (start_second < 0 or start_second > 59):
            raise ValueError

        startTimecode = start_hour, start_minute, start_second

        
        with open(filename, 'r') as file:
            lines = file.readlines()

            with open('globalTC_' + filename, 'w') as newfile:

                for line in lines:

                    if len(line) > 2:
                        if line[0].isdigit() and line[1].isdigit() and line[2] == ':':

                            linesplit = line.split(' ')
                            timecodeIn = linesplit[0]
                            sign = linesplit[1]
                            timecodeOut = linesplit[2]

                            timecodeIn = updateTimecode(getHourMinuteSecondFrames(timecodeIn), startTimecode)
                            timecodeOut = updateTimecode(getHourMinuteSecondFrames(timecodeOut), startTimecode)
                            
                            line = timecodeIn + ' ' + sign + ' ' + timecodeOut

                    newfile.write(line)

                print(f'Timecodes in {filename} successfuly updated to "globalTC_{filename}"') 

    except IndexError:
        print('Invalid timecode')

    except ValueError:
        print('hh:mm:ss must be two digits positive integers (00-59)')

    except FileNotFoundError:
        print('File not found')
        

def main():

    filename = input('Filename >')
    start_timecode = input('start timecode hh:mm:ss >')
    
    globalizeTimecode(filename, start_timecode)


if __name__ == '__main__':
    main()
