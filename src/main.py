from typing import List, Tuple, Union

import pandas as pd
from src.utils.purchase_details import Purchase
from src.utils.purchase_management import PurchaseManager
from src.utils.purchase_processing import DataProcessor



def main():
    purchase_manager = PurchaseManager()

    flag = True
    while flag:
        
        purchase_description = input('Enter Description Purchase')
        amount_paid = int(input(""))


        purchase = Purchase(purchase_description= ,
                            amount_paid= ,
                            payer_name= ,
                            consumer=
                            )



        purchase_manager.add_purchase(purchase)


        flag = False







if __name__ == "__main__":
    main()
