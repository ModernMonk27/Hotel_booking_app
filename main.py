import pandas as pd

from fpdf import FPDF

df = pd.read_csv("hotels.csv", dtype= str)


class Hotel:
    def __init__(self, hotelx):
        self.physc = hotelx
        self.ole = df.loc[df["id"] == self.physc , "name"].squeeze()

    def book(self):
        """ this method changes the availability of hotel in csv file to no"""

        df.loc[df["id"] == self.physc, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.physc, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Registration:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def get_ticket(self):
        content = f"""
        
        Thank You for booking....
        Here is your booking details
        
        name : {self.customer_name}
        
        hotel name : {self.hotel.ole}
        
        booking id : 4rftgb 
        
        Have a great stay 
        """
        return content

    def pdfgen(self):

        pdf = FPDF(orientation="P", format="A4", unit="mm")
        pdf.add_page()
        content = f"""

               Thank You for booking....
               Here is your booking details

               name : {self.customer_name}

               hotel name : {self.hotel.ole}

               booking id : 4rftgb 

               Have a great stay 
               """

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=80, h=6, txt=f"Thank You for booking....", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=80, h=6, txt=f"Here is your booking details", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=80, h=6, txt=f"name : {self.customer_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=80, h=6, txt=f"hotel name : {self.hotel.ole}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=80, h=6, txt=f"booking id : 4rftgbT", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=80, h=6, txt=f"Have a great stay ", ln=1)
        pdf.output("ticket.pdf")




print(df)

hotel_ID = input("Enter the hotel ID : ")

hotel = Hotel(hotelx=hotel_ID)

if hotel.available():
    hotel.book()
    customer_details = input("Enter your name : ")
    reserve = Registration(customer_details, hotel)
    reserve.pdfgen()

else:
    print("hotel is not free..!")
