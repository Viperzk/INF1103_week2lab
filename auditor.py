total_inventory = 0
processed_entries = 0
rejected_entries = 0
overstock_limit = 0 #treshold alert

print("Enter stock quantity per delivery or type 'quit'")

while True:
    user_input = input("Stock quantity: ").strip()
    if user_input.lower() == 'quit':
        print("\nInvalid")
        break


    
