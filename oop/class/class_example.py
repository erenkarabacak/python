class Computer():

    def __init__(self, brand="Msi", processor=3.4, ram=8, graphic_card="gtx1050"):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.graphic_card = graphic_card

    def show_computer(self):
        print("Brand {0}, Processor {1} Ghz, Ram {2} Gb, Graphic Card {3}".format(self.brand,self.processor,self.ram,self.graphic_card))


    def upgrade_ram(self,new_ram):
        print("Ram is Upgrading..")
        self.ram += new_ram

    def upgrade_processor(self,new_processor):
        print("Processor is upgrading..")
        self.processor += new_processor

    def upgrade_gpu(self,new_gpu):
        print("Graphic Card is changing")
        self.graphic_card = new_gpu
computer1 = Computer(brand="Msi", processor=3.5, ram=8, graphic_card="gtx1070")
computer1.show_computer()
computer1.upgrade_ram(6)
computer1.upgrade_gpu("gtx1080")
computer1.show_computer()