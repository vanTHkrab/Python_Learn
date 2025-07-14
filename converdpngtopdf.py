from io import BytesIO
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter

def convert_images_to_pdf(image_paths, output_pdf):
    pdf = PdfFileWriter()
    for image_path in image_paths:
        img = Image.open(image_path)
        img_temp = BytesIO()
        img.save(img_temp, format='png')
        img_temp.seek(0)
        pdf.add_page(PdfFileReader(img_temp))
    with open(output_pdf, 'wb') as f:
        pdf.write(f)
