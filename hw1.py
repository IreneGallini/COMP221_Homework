import imageTools
import math


pic = imageTools.Picture("alba.jpeg") # load the original picture
width = pic.getWidth()
height = pic.getHeight()

edgeImg = imageTools.Picture(width, height) # create new image for output

# define the sobel kernels
x_kernel = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

y_kernel = [
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
]

# loop through pixels
for y in range(1, height - 1):
    for x in range(1, width - 1):
        
        # sums for x and y filters 
        sumXRed = 0
        sumXGreen = 0
        sumXBlue = 0
        
        sumYRed = 0
        sumYGreen = 0
        sumYBlue = 0
        
        # iterate over the 3x3 neighbors
        for ky in range(-1, 2):
            for kx in range(-1, 2):
                # get neighboring pixel color
                r, g, b = pic.getColor(x + kx, y + ky)
                
                # kernel weights (offset indices by 1)
                xw = x_kernel[ky + 1][kx + 1]
                yw = y_kernel[ky + 1][kx + 1]
                
                # weighted values for x filter
                sumXRed += r * xw
                sumXGreen += g * xw
                sumXBlue += b * xw
                
                # weighted values for y filter
                sumYRed += r * yw
                sumYGreen += g * yw
                sumYBlue += b * yw
        
        # average the three color channel sums
        Gx = (sumXRed + sumXGreen + sumXBlue) / 3.0
        Gy = (sumYRed + sumYGreen + sumYBlue) / 3.0
        
        # gradient magnitude 
        G = math.sqrt(Gx**2 + Gy**2)
        
        # value stays within valid pixel range 
        G = int(min(max(G, 0), 255))
        
        # set the grayscale color in the edge image
        edgeImg.setColor(x, y, (G, G, G))

# save edge image 
edgeImg.save("edgeName.jpg")
print("Edge detection complete! Image saved as edgeName.jpg")