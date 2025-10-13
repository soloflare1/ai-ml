data = {
    "student" : {
        "name": "naba",
        "id" : 5,
        "contact" : {
            "email" : ["naba@example.com", "naba2@example.com"],
            "phone" : "123-456-7890"
        }
    },
    "courses" : [
        {"course_name": "OS", "credits" : 3},
        {"course_name": "SDP", "credits" : 3}
    ]
}

# Accessing nested data structures
# we can access the nested data using keys and indices
# specify the path to the data we want to access by chaining keys and indices
# For example, to access the email of the student:
print(data["student"]["contact"]["email"][0]) # Output: naba@example.com



# Given thee following nested dic representing a customer order, extract & print the
# following information:
#     1.The customer's full name.
#     2.The total price of all items in the order.
#     3.A list of the names of all items in the order.

order_data = {
    "customer" : {
        "first_name" : "Bob",
        "last_name" : "Johnson"
    },
    
    "items" : [
        {"item_name" : "Book",
         "price" :500.00
        },
        {"item_name" : "Pen", 
         "price" :5
        },
        {"item_name" : "Pencil", 
         "price" :50.00
        }
    ]
}

# 1. customer's full name
full_name = f'{order_data["customer"]["first_name"]} {order_data["customer"]["last_name"]}'
print(full_name)

# 2. Total price of all items
total_price = sum(item["price"] for items in order_data["items"])
print("Total order price : ", total_price)