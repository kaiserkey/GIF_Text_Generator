from PIL import Image, ImageDraw, ImageFont
texto = "My Name is Daniel, but everybody calls me DanielSan!"
images = []
# Creamos una fuente
fuente = ImageFont.truetype("Roboto-Black.ttf", 25)

for i in range(len(texto)):
    concatenate_text = ""
    for char in range(len(texto[0:i])):
        concatenate_text += texto[char] + " "
    
    # Crear una imagen en blanco
    img = Image.new('RGBA', (1000, 60), color = (27,31,35,1))

    # Agregar el texto
    d = ImageDraw.Draw(img) 
    d.text((10,20), concatenate_text + texto[i], fill=(46, 221, 23), align="center", font=fuente)
    
    # Crear una lista de todas las imágenes que desea incluir en el GIF
    images.append(img)

# Crear una instancia de la clase ImageSequence
image_sequence = [img.copy() for img in images]

# Crear el GIF
image_sequence[0].save('mi_gif.gif', format='GIF', save_all=True, append_images=image_sequence[1:], duration=150, loop=0)
print("GIF Creado Exitosamente!")