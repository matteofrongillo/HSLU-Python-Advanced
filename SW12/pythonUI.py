import sqlite3
conn = sqlite3.connect("SW12/exerciseDB.db")

class DatabaseInterface:
    def __init__(self):
        self.main_menu = """+----------+-------------------------------------------------+
| Choice   | Description                                     |
+----------+-------------------------------------------------+
| 1        | List vendors                                    |
+----------+-------------------------------------------------+
| 2        | List items (by name)                            |
+----------+-------------------------------------------------+
| 3        | Fetch order options (by ItemID)                 |
+----------+-------------------------------------------------+
| 4        | Scan item (by order number)                     |
+----------+-------------------------------------------------+
| 5        | Exit                                            |
+----------+-------------------------------------------------+
"""

    def display_menu(self):
        print(self.main_menu)

    def list_vendors(self):
        sub_menu = """+----------+-------------------------------------------------+
| 1        | List vendors                                    |
+----------+-------------------------------------------------+"""
        print(sub_menu)
        print("\nList of vendors:")
        # print("\n \nNot yet implemented... \n \n \n")
        # TODO: Implement the code here
        cursor = conn.cursor()
        sql_query = """
        SELECT vendorID, name, url
        FROM vendors
        """
        cursor.execute(sql_query)
        print("+----------+------------------+------------------------------+")
        print("| vendorID | name             | url                          |")
        print("+----------+------------------+------------------------------+")
        for vendor in cursor.fetchall():
            print(f"| {vendor[0]:<8} | {vendor[1]:<16} | {vendor[2]:<28} |\n+----------+------------------+------------------------------+")
        cursor.close()

    def list_items(self):
        sub_menu = """+----------+-------------------------------------------------+
| 2        | List items (by name)                            |
+----------+-------------------------------------------------+"""
        print(sub_menu)
        item_name = input("\nEnter the item name: ")
        print(f"\nList of items containing '{item_name}' in the name:")
        #print("\n \nNot yet implemented... \n \n \n")
        # TODO: Implement the code here
        cursor = conn.cursor()
        sql_query = """
        SELECT inventoryID, name, category, units
        FROM inventory
        """
        cursor.execute(sql_query)
        print("+-------------+-----------------+--------------------+-------+")
        print("| inventoryID | name            | category           | units |")
        print("+-------------+-----------------+--------------------+-------+")

        sql_query = cursor.fetchall()
        for item in sql_query:
            if item_name.lower() in item[1].lower():
                print(f"| {item[0]:<11} | {item[1]:<15} | {item[2]:<18} | {item[3]:<5} |\n+-------------+-----------------+--------------------+-------+")
                if item[3] <= 10:
                    print(f"  Warning: {item[1]} ONLY {item[3]} LEFT!!\n \n \n")

        cursor.close()

    def get_orders(self):
        sub_menu = """+----------+-------------------------------------------------+
| 3        | Fetch order options (by ItemID)                 |
+----------+-------------------------------------------------+"""
        print(sub_menu)
        item_id = input("\nEnter the ItemID: ")
        print(f"\nOrder options for ItemID {item_id}:")
        print("\n \nNot yet implemented... \n \n \n")
        # TODO: Implement the code here

    def scan_item(self):
        sub_menu = """+----------+-------------------------------------------------+
| 4        | Scan item (by order number)                     |
+----------+-------------------------------------------------+"""
        print(sub_menu)
        order_nr = input("\nEnter the order number: ")
        print(f"\nScanning item with order number {order_nr}...")
        print("\n \nNot yet implemented... \n \n \n")
        # TODO: Implement the code here

    def end_menu(self):
        sub_menu = """+----------+-------------------------------------------------+
| 5        | Exit                                            |
+----------+-------------------------------------------------+"""
        print(sub_menu)
        print("\nProgram terminated. Goodbye!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nChoose an option (1-5): ")

            if choice == "1":
                self.list_vendors()
            elif choice == "2":
                self.list_items()
            elif choice == "3":
                self.get_orders()
            elif choice == "4":
                self.scan_item()
            elif choice == "5":
                self.end_menu()
                break
            else:
                print("\nInvalid input. Please choose a valid option (1-5).\n")

# Start main program
if __name__ == "__main__":
    print("Welcome to the Database Interface! Please choose an option:")
    interface = DatabaseInterface()
    interface.run()
