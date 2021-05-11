MAX_HEIGHT = 1.9
MIN_HEIGHT = 1.6

def main():
    # TODO write your solution here
    height = float(input('Enter your height in meters: '))
    if height >= MIN_HEIGHT and height <= MAX_HEIGHT:
        print('Correct height to be an astronaut')
    elif height < MIN_HEIGHT:
        print('Below minimum astronaut height')
    else: # if height > 1.9:
        print('Above maximum astronaut height')

if __name__ == "__main__":
    main()