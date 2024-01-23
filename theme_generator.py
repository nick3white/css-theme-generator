import pywal, os, argparse

def remove_duplicates(colors):
    unique_colors = []
    for i in colors:
        if colors[i] not in unique_colors:
            unique_colors.append(colors[i])
    return unique_colors

def convert_hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def generate_css_file(filename, palette):
    image_filename = os.path.splitext(os.path.basename(filename))[0]
    css_filename = f"themes/{image_filename}.css"

    with open(css_filename, "w") as file:
        file.write(f".{image_filename} {{\n")
        file.write(f"  --wallpaper: url('{os.path.basename(filename)}');\n")
        file.write(f"  --background: {palette['background']};\n")
        file.write(f"  --foreground: {palette['foreground']};\n")

        for idx, value in enumerate(palette['colors']):
            rgb_color = convert_hex_to_rgb(value)
            file.write(f"  --color{idx}: {rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]};\n")

        file.write("}\n")

def generate_colors_from_images(filename):
    with open(filename, 'r') as file:
        image_list = file.read().splitlines()

    colors = []

    for image_filename in image_list:
        if os.path.isfile(image_filename):

            image = pywal.image.get(image_filename)
            image_colors = pywal.colors.get(image)
            unique_colors = remove_duplicates(image_colors['colors'])
            truncated_colors = {
                'wallpaper': image_colors['wallpaper'],
                'background': image_colors['special']['background'],
                'foreground': image_colors['special']['foreground'],
                'colors': unique_colors
            }
            
            generate_css_file(image_filename, truncated_colors)
        else:
            print(f"Image file '{image_filename}' does not exist.")

parser = argparse.ArgumentParser(description="Generate CSS files from images using Pywal")
parser.add_argument("input_filename", help="Path to the input text file containing image filenames")
args = parser.parse_args()

generate_colors_from_images(args.input_filename)
