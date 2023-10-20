from tkinter import *
from tkinter import filedialog as fd
from PIL import Image as Img, ImageTk, ImageOps

WATERMARK_PATH = './tomato.png'
OUTPUT_PATH = './output.png'


class App:
    def __init__(self):
        self.original_file = ''
        self.original_img = None
        self.output_img = None
        self.original_canvas = None
        self.output_canvas = None
        self.create_gui()

    def select_original(self):
        self.original_file = fd.askopenfilename()
        self.original_img = ImageTk.PhotoImage(Img.open(self.original_file))
        self.original_canvas.create_image(300, 200, image=self.original_img)

    def watermark_image(self):
        image_1 = Img.open(self.original_file).convert('RGBA')
        image_2 = Img.open(WATERMARK_PATH).convert('RGBA')
        mask = ImageOps.invert(Img.open(WATERMARK_PATH).convert('L'))

        image_2.putalpha(50)
        image_2.putalpha(mask)
        image_1.paste(image_2, (
            round(image_1.size[0] / 2) - round(image_2.size[0] / 2),
            round(image_1.size[1] / 2) - round(image_2.size[1] / 2)
        ), mask=mask)
        image_1.save(OUTPUT_PATH)

        self.output_img = PhotoImage(file=OUTPUT_PATH)
        self.output_canvas.create_image(300, 200, image=self.output_img)

    def create_gui(self):
        # Create window
        window = Tk()
        window.title('Image Watermark')
        window.config(padx=20, pady=20)

        # Create widgets
        original_label = Label(text='Original')
        select_button = Button(text='Select Image', command=self.select_original)
        self.original_canvas = Canvas(width=600, height=400, bg="#191919")
        output_label = Label(text='Output')
        convert_button = Button(text='Watermark Image', command=self.watermark_image)
        self.output_canvas = Canvas(width=600, height=400, bg="#191919")

        # Place widgets
        original_label.grid(row=0, column=0, sticky='sw', pady=5)
        select_button.grid(row=0, column=1, sticky='ne', pady=5)
        self.original_canvas.grid(row=1, column=0, columnspan=2, sticky='news')
        output_label.grid(row=2, column=0, sticky='sw', pady=5)
        convert_button.grid(row=2, column=1, sticky='ne', pady=5)
        self.output_canvas.grid(row=3, column=0, columnspan=2, sticky='news')

        window.mainloop()


if __name__ == '__main__':
    app = App()
