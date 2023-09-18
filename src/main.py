

# import pandas as pd
from src.utils.purchase_details import Purchase
from src.utils.purchase_management import PurchaseManager
from src.utils.purchase_processing import DataProcessor
from src.utils.inputs import Inputs



def main():
    purchase_manager = PurchaseManager()
    get_input = Inputs()

    names = get_input.get_names()
    purchase_description = get_input.get_purchase_description()
    amount_paid = get_input.get_amount_paid()
    payer_name = get_input.get_payer_name()
    consumer = get_input.get_consumer_name()

    print(names)
    print(purchase_description)
    print(amount_paid)
    print(payer_name)
    print(consumer)






if __name__ == "__main__":
    main()

