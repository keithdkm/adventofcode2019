from collections import Counter
with open('Day_8\input.txt') as f:
    image_data = f.read().strip()
h = 6
w = 25
# image_data = '0222112222120000'
# h = 2
# w = 2

layers = [image_data[s:s+h*w] for s in range(0,len(image_data),h*w)]

# layers_digit_counts = sorted((Counter(layer) for layer in layers), key = lambda x: x['0'])
# print(layers_digit_counts)
# print (layers_digit_counts[0]['1']*layers_digit_counts[0]['2'])


all_pixels =  zip(*layers)
pixels = [''.join(p) for p in all_pixels]

image = ''
for pixel in pixels:
    
    for layer_color in pixel:
        if layer_color !='2':
            if layer_color == '0':
                image += " "
            else: 
                image += '#'
            break
            

for line in range(0,len(image),w):
    print(image[line:line+w])
        


