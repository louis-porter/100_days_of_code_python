import colorgram

rgb_colors = []
colors = colorgram.extract(r'C:\Users\Owner\Desktop\100DaysOfCode\Day 18 - GUI\image.jpg', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

