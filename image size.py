def image_size(width, height, colourDepth):
    pixels = width * height
    size = pixels * colourDepth
    return size

def sound_size(duration, sampleSize, sampleFrequency):
    ssize = sampleSize * sampleFrequency * duration
    return ssize

def text_size(text):
    return len(text) * 7

calculate = input("What do you want to calculate? (image/sound/text): ").lower()

if calculate == "image":
    width = int(input("Enter the width of the image in pixels: "))
    height = int(input("Enter the height of the image in pixels: "))
    colourDepth = int(input("Enter the colour depth in bits: "))
    print("The image size is: ", image_size(width,height,colourDepth))

elif calculate == "sound":
    duration = int(input("Enter the duration of the sound in seconds: "))
    sampleSize = int(input("Enter the sample size in bits: "))
    sampleFrequency = int(input("Enter the sample frequency in Hz: "))
    print("The sound size is: ", sound_size(duration, sampleSize, sampleFrequency))

elif calculate == "text":
    text = input("Enter the text: ")
    print("The text size is: ", text_size(text))

else:
    print("Invalid input. Please enter 'image' or 'sound'.")