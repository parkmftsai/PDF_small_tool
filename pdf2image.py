import pdf2image  
pages = pdf2image.convert_from_path('1.pdf')  
  
for i in range(0, len(pages)):  
    pages[i].save(f'image{i+1}.png', 'PNG')  
