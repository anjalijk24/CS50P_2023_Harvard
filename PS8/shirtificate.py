#Assignment: implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file
#called shirtificate.pdf similar to this one for John Harvard, with these specifications:

    #The orientation of the PDF should be Portrait.
    #The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    #The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    #The shirt’s image should be centered horizontally.
    #The user’s name should be on top of the shirt, in white text.


from fpdf import FPDF


class PDF(FPDF):
    def shirtificate(self):
        # A4 paper dimensions
        a4_width = 210
        a4_height = 297

        # Calculate center position for the image
        image_width = 190
        image_height = 240
        x = (a4_width - image_width) / 2
        y = (a4_height - image_height) / 2

        # Add the image
        self.image("./shirtificate.png", x, y, image_width, image_height)

        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 20)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 20, "CS50Shirtificate", align="C")

        # Performing a line break:
        self.ln(10)


    def add_name(self, name):
        # Set color for the name to white
        self.set_text_color(255, 255, 255)
        # Move to the top of the shirt
        self.ln(85)
        # Center the text horizontally
        self.cell(0, 0, name, 0, 1, "C")



def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.shirtificate()                      # Call the method to render the image and title
    pdf.add_name(name + " took CS50")       # Add the user's name
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()

