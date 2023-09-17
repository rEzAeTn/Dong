class Inputs():
    def __init__(self):
        pass


    def get_names(self):
        names = []
        while True:
            name = input('enter name')
            if name.upper() == "Q":
                break
            names.append(name)
        
        unique_names = set(map(str.title, names))
        return unique_names


    def get_purchase_description(self):
        pass


    def get_amount_paid(self):
        pass


    def get_payer_name(self):
        pass


    def get_consumer(self):
        pass