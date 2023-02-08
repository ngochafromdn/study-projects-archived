'''
These Python functions that implement some basic image manipulation algorithms, including gradient blending, mirror, pencil sketch, and scramble.
Name: Le Thi Hong Ha (ID:210205), Nguyen Hoang Ngoc Ha (ID: 210206).
Time : 24 hours'''
def gradient_blend():
    '''This function produces a collage using gradient blending'''
    from csc121.image import get_channel, write_jpg
    rick_red = get_channel('rick.jpg', 'red')
    rick_green = get_channel('rick.jpg', 'green')
    rick_blue = get_channel('rick.jpg', 'blue')
    
    ilsa_red = get_channel('ilsa.jpg', 'red')
    ilsa_green = get_channel('ilsa.jpg', 'green')
    ilsa_blue = get_channel('ilsa.jpg', 'blue')
    
    #Identify the height and width of the image
    h = len(ilsa_red)
    w = len(ilsa_red[0])
    blending_factor = 1 #the maximum value for a and b
    for r in range(h):
        for c in range(w):
            a = float(r/h)
            b = float(c/w)
            #Multiply the pixel of the Ilsa and Rick image by the maximum value between a and b
            if (a <= blending_factor and b<= blending_factor):
                rick_red[r][c] = int(rick_red[r][c] * max(a,b) + ilsa_red[r][c] * (1-max(a,b))) 
                rick_green[r][c] = int(rick_green[r][c] * max(a,b) + ilsa_green[r][c] * (1-max(a,b)))
                rick_blue[r][c] = int(rick_blue[r][c] * max(a,b) + ilsa_blue[r][c] * (1-max(a,b)))
    write_jpg(rick_red, rick_green, rick_blue, 'blended.jpg')

def mirror():
    '''This function mirrors an image along the vertical axis'''
    from csc121.image import get_channel, write_jpg
    #Input the image
    image = str(input("Enter the name of the image:"))
    image_red = get_channel(image, 'red')
    image_green = get_channel(image, 'green')
    image_blue = get_channel(image, 'blue')
    
    #Identify the height and width of the image
    height = len(image_red)
    width = len(image_red[0])
    
    for row in range(height):
        for col in range(width//2):
            image_red[row][width - 1 - col] = image_red[row][col]
            image_green[row][width - 1 - col] = image_green[row][col]
            image_blue[row][width - 1 - col] = image_blue[row][col]
    write_jpg(image_red, image_green, image_blue, 'mirrored.jpg')

def pencil_sketch():
    '''This function applies an effect that makes it look as though it was sketched with a pencil'''
    from csc121.image import get_channel, write_jpg
    #Input the image
    image = str(input("Enter the name of the image:"))
    image_red = get_channel(image, 'red')
    image_green = get_channel(image, 'green')
    image_blue = get_channel(image, 'blue')
    
    #Identify the height and width of the image
    height = len(image_red)
    width = len(image_red[0])
    for row in range(height-1):
        for col in range(width-1):
            #Compute the gray number of three pixel: here, right and bottom
            here = (image_red[row][col] + image_green[row][col] + image_blue[row][col]) //3
            right = (image_red[row][col+1] + image_green[row][col+1] + image_blue[row][col+1]) //3
            bottom = (image_red[row+1][col] + image_green[row+1][col] + image_blue[row+1][col]) //3
            #Compare the absolute values of the differences between here - right and here - bottom with 8
            if (abs(here - right) > 8 and abs(here-bottom) > 8):
                image_red[row][col] = 0
                image_green[row][col] = 0
                image_blue[row][col] = 0
            else:
                image_red[row][col] = 255
                image_green[row][col] = 255
                image_blue[row][col] = 255
    write_jpg(image_red, image_green, image_blue, 'sketched.jpg')

def tile_image():
    '''This function produces a “scrambled” version of the original, in the style of a 3×3 sliding tile puzzle'''
    import random
    from csc121.image import get_channel, write_jpg
    image = str(input("Enter the name of the image:"))
    image_red = get_channel(image, 'red')
    image_green = get_channel(image, 'green')
    image_blue = get_channel(image, 'blue')
    
    #Identify the height and width of the image
    height = int(len(image_red))
    width = int(len(image_red[0]))
    for i in range(1,10,1): #create 4 random variables to randomly change the position of 9 pieces of image
        a=random.randint(0,2)
        b=random.randint(0,2)
        c=random.randint(0,2)
        d=random.randint(0,2)
        for row in range(1,height//3,1):
            for col in range(1,width//3,1):
                (image_red[row+height//3*a][col+width//3*b],image_red[row+height//3*c][col+width//3*d])= (image_red[row+height//3*c][col+width//3*d],image_red[row+height//3*a][col+width//3*b])
                (image_green[row+height//3*a][col+width//3*b],image_green[row+height//3*c][col+width//3*d])= (image_green[row+height//3*c][col+width//3*d],image_green[row+height//3*a][col+width//3*b])
                (image_blue[row+height//3*a][col+width//3*b],image_blue[row+height//3*c][col+width//3*d])= (image_blue[row+height//3*c][col+width//3*d],image_blue[row+height//3*a][col+width//3*b])
    write_jpg(image_red, image_green, image_blue, 'tiled.jpg')
    