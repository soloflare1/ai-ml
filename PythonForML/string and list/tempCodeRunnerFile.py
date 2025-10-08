
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
full_name = f'{order_data["customer"]["first_name"]}
              {order_data["customer"]["last_name"]}'
print(full_name)