import PIL.Image

# 18 ascii characters from blackest to whitest
ASCII_CHARS = ["@", "#", "S", "&", "8", "B", "Q", "0", "O", "Z", "C", "X", "L", "I", "i", ":", ".", " "]



# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# pixel to ascii
def pixels_to_ascii(image):
    pixels = image.getdata()
    scale = 256 // len(ASCII_CHARS)
    characters = "".join([ASCII_CHARS[pixel // scale] for pixel in pixels])
    return(characters)

def main(new_width=100):
    path = input("Enter image path:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Invalid path\n")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)]) # this will be saved
    

    print(ascii_image)
    
    # save
    with open("save.txt", "w") as f:
        f.write(ascii_image)
 
main()
