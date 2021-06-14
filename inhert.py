class Oneplus:
    Name_of_Manufacturer = "Oppo Inc."
    contact = 'www.oneplus.com/contact'

    def contact_detail(self):
        print("To contact us log on to", self.contact)
        
class Earbuds(Oneplus): 
    def __init__(self):
        self.yom = 2017
        
    def manufacturer_detail(self):
        print("This product was manufactured on {} by {}".format(self.yom, self.Name_of_Manufacturer))
        

earbuds = Earbuds()
earbuds.manufacturer_detail()
earbuds.contact_detail()

    