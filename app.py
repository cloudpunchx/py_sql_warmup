import mariadb
import dbcreds

conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database
                        )
cursor = conn.cursor()

def choose_sales_person():
    cursor.execute("SELECT * FROM sales_person")
    sales_people = cursor.fetchall()
    print(sales_people)
    global sales_person_id
    sales_person_id = input("Choose Your Sales Person: ")

def make_purchase():
    choose_sales_person()
    global sales_person_id
    print("Make Purchase with Sales Person", sales_person_id)
    cursor.execute("SELECT * FROM item")
    sale_items = cursor.fetchall()
    print(sale_items)
    selected_item = input("Select an Item ID to Purchase: ")
    selected_item = int(selected_item)
    sales_person_id = int(sales_person_id)
    values = (sales_person_id, selected_item)
    cursor.execute("INSERT INTO item_sale (sales_person_id, item_id) VALUES (?, ?)", values)
    conn.commit()
    print("Successfully purchased item!")


def shopping():
    print("Welcome to the Seinfeld Shop!")
    is_valid = False
    while not is_valid:
        print("Make a Selection: \
            \n1. Make A Purchase\
            \n2. Exit the App")
        selection = input("Enter Selection: ")
        if selection == '1':
            make_purchase()
        elif selection == '2':
            print("Thank you for shopping at the Seinfeld Shop!")
            is_valid = True
        else:
            print("Make a selection from 1-2")

shopping()