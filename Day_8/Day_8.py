from collections import Counter
with open('Day_8\input.txt') as f:
    image_data = f.read().strip()
h = 6
w = 25

layers = [(image_data[s:s+h*w]) for s in range(0,len(image_data),h*w)]

layers_digit_counts = sorted((Counter(layer) for layer in layers), key = lambda x: x['0'])
print(layers_digit_counts)
print (layers_digit_counts[0]['1']*layers_digit_counts[0]['2'])
