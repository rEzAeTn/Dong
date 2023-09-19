

# import pandas as pd
from src.utils.purchase_details import Purchase
from src.utils.purchase_management import PurchaseManager
from src.utils.purchase_processing import DataProcessor
from src.utils.inputs import Inputs


def main():
    get_input = Inputs()
    purchase_manager = PurchaseManager()
    
    
    while True:
        input_names = get_input.get_names()
        input_purchase_description = get_input.get_purchase_description()
        input_amount_paid = get_input.get_amount_paid()
        input_payer_name = get_input.get_payer_name()
        input_consumer = get_input.get_consumer_name()

        create_purchase = Purchase(purchase_description=input_purchase_description ,
                                   amount_paid=input_amount_paid,
                                   payer_name=input_payer_name,
                                   consumer=input_consumer
                                   )
        
        purchase_manager.add_purchase(create_purchase)

        suggest = input("View Status Summary, `Y or ...`")
        if suggest.upper() == "Y":
            data_frame = purchase_manager.create_dataframe()

            data_processor = DataProcessor(data_frame)
            total_spent = data_processor.calculate_total_spent()
            total_share = data_processor.calculate_total_share()
            balances = data_processor.calculate_balances()
            summary_report_dataframe = data_processor.create_summary_report_dataframe()

            print(data_frame)
            print()
            print(f'total spent --> {total_spent}')
            print(f'total share --> {total_share}')
            print(f'Balances    --> {balances}')
            print()
            print(summary_report_dataframe)
            print()
            
            continue










if __name__ == "__main__":
    main()

