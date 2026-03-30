# ============================================================
# Part 2 — Restaurant Menu & Order Management System
# ============================================================

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# ============================================================
# Task 1: Explore the Menu
# ============================================================


categories = ["Starters", "Mains", "Desserts"]

print("\n========== FULL MENU ==========")

for category in categories:
    print(f"\n===== {category} =====")

    
    for dish, details in menu.items():
        if details["category"] == category:

            
            availability = "[Available]" if details["available"] else "[Unavailable]"

            
            print(f"  {dish:<16} ₹{details['price']:>8.2f}   {availability}")


total_items     = len(menu)
available_items = sum(1 for d in menu.values() if d["available"])


most_expensive      = max(menu, key=lambda d: menu[d]["price"])
most_expensive_price = menu[most_expensive]["price"]

# List comprehension — collect all items priced under 150
cheap_items = [(dish, details["price"])
               for dish, details in menu.items()
               if details["price"] < 150]

print(f"\n--- Menu Statistics ---")
print(f"Total items     : {total_items}")
print(f"Available items : {available_items}")
print(f"Most expensive  : {most_expensive} (₹{most_expensive_price:.2f})")
print(f"\nItems under ₹150:")
for dish, price in cheap_items:
    print(f"  {dish:<16} ₹{price:.2f}")


# ============================================================
# Task 2: Cart Operations
# ============================================================

cart = []

# Function to add an item to the cart 
def add_to_cart(item_name, quantity):

    
    if item_name not in menu:
        print(f"  ✗ '{item_name}' does not exist in the menu.")
        return

    
    if not menu[item_name]["available"]:
        print(f"  ✗ '{item_name}' is currently unavailable.")
        return

    # Check if item is already in the cart
    existing = next((entry for entry in cart if entry["item"] == item_name), None)

    if existing:
        # Item already in cart — just increase quantity
        existing["quantity"] += quantity
        print(f"  ✓ Updated '{item_name}' quantity to {existing['quantity']}")
    else:
        # Item not in cart — add new entry
        cart.append({
            "item":     item_name,
            "quantity": quantity,
            "price":    menu[item_name]["price"]
        })
        print(f"  ✓ Added '{item_name}' x{quantity} to cart")

# Function to remove an item from the cart
def remove_from_cart(item_name):

    
    existing = next((entry for entry in cart if entry["item"] == item_name), None)

    if existing:
        cart.remove(existing)
        print(f"  ✓ Removed '{item_name}' from cart")
    else:
        print(f"  ✗ '{item_name}' is not in the cart.")

# Function to update quantity of an item in the cart
def update_quantity(item_name, new_quantity):

    existing = next((entry for entry in cart if entry["item"] == item_name), None)

    if existing:
        existing["quantity"] = new_quantity
        print(f"  ✓ Updated '{item_name}' quantity to {new_quantity}")
    else:
        print(f"  ✗ '{item_name}' is not in the cart.")


def print_cart():
    if not cart:
        print("  Cart is empty.")
        return
    print("  Current cart:")
    for entry in cart:
        print(f"    {entry['item']:<16} x{entry['quantity']}  ₹{entry['price'] * entry['quantity']:.2f}")

#Simulating the sequence
print("\n========== CART OPERATIONS ==========")

print("\n-- Step 1: Add Paneer Tikka x2 --")
add_to_cart("Paneer Tikka", 2)
print_cart()

print("\n-- Step 2: Add Gulab Jamun x1 --")
add_to_cart("Gulab Jamun", 1)
print_cart()

print("\n-- Step 3: Add Paneer Tikka x1 (should update to 3) --")
add_to_cart("Paneer Tikka", 1)
print_cart()

print("\n-- Step 4: Try to add Mystery Burger (does not exist) --")
add_to_cart("Mystery Burger", 1)
print_cart()

print("\n-- Step 5: Try to add Chicken Wings (unavailable) --")
add_to_cart("Chicken Wings", 1)
print_cart()

print("\n-- Step 6: Remove Gulab Jamun --")
remove_from_cart("Gulab Jamun")
print_cart()

# --- Final Order Summary ---
print("\n========== Order Summary ==========")

subtotal = sum(entry["price"] * entry["quantity"] for entry in cart)
gst      = round(subtotal * 0.05, 2)
total    = round(subtotal + gst, 2)

for entry in cart:
    line_total = entry["price"] * entry["quantity"]
    print(f"{entry['item']:<20} x{entry['quantity']}    ₹{line_total:.2f}")

print("-" * 38)
print(f"{'Subtotal:':<28} ₹{subtotal:.2f}")
print(f"{'GST (5%):':<28} ₹{gst:.2f}")
print(f"{'Total Payable:':<28} ₹{total:.2f}")
print("=" * 38)


# ============================================================
# Task 3: Inventory Tracker with Deep Copy
# ============================================================

import copy


inventory_backup = copy.deepcopy(inventory)

print("\n========== INVENTORY TRACKER ==========")


print("\n-- Demonstrating Deep Copy --")
inventory["Paneer Tikka"]["stock"] = 999  # temporary change
print(f"  inventory stock for Paneer Tikka        : {inventory['Paneer Tikka']['stock']}")
print(f"  inventory_backup stock for Paneer Tikka : {inventory_backup['Paneer Tikka']['stock']}")
print("  ✓ Backup is unaffected — deep copy works correctly")


inventory["Paneer Tikka"]["stock"] = 10


print("\n-- Deducting Stock Based on Final Cart --")

for entry in cart:
    item_name = entry["item"]
    qty_needed = entry["quantity"]

    # Get current stock for this item
    current_stock = inventory[item_name]["stock"]

    if current_stock >= qty_needed:
        # Enough stock — deduct normally
        inventory[item_name]["stock"] -= qty_needed
        print(f"  ✓ {item_name:<16} : deducted {qty_needed}, remaining stock = {inventory[item_name]['stock']}")
    else:
        # Not enough stock — deduct only what's available
        print(f"  ⚠ {item_name:<16} : insufficient stock. Only {current_stock} available, deducting {current_stock}")
        inventory[item_name]["stock"] = 0

# --- Step 3: Reorder alerts ---
print("\n-- Reorder Alerts --")

for item_name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"  ⚠ Reorder Alert: {item_name} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# --- Step 4: Print both inventories to confirm they differ ---
print("\n-- Final Inventory vs Backup --")
print(f"\n  {'Item':<16} {'Current Stock':>15} {'Backup Stock':>14}")
print("  " + "-" * 46)

for item_name in inventory:
    current = inventory[item_name]["stock"]
    backup  = inventory_backup[item_name]["stock"]

    # Mark items where stock has changed
    changed = " ← changed" if current != backup else ""
    print(f"  {item_name:<16} {current:>15} {backup:>14}{changed}")


# ============================================================
# Task 4: Daily Sales Log Analysis
# ============================================================

print("\n========== SALES LOG ANALYSIS ==========")


print("\n-- Revenue Per Day --")


daily_revenue = {}

for date, orders in sales_log.items():
    
    daily_total = sum(order["total"] for order in orders)
    daily_revenue[date] = daily_total
    print(f"  {date} : ₹{daily_total:.2f}")


best_day         = max(daily_revenue, key=lambda d: daily_revenue[d])
best_day_revenue = daily_revenue[best_day]
print(f"\n  Best Selling Day : {best_day} (₹{best_day_revenue:.2f})")


item_counts = {}

for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

most_ordered_item  = max(item_counts, key=lambda x: item_counts[x])
most_ordered_count = item_counts[most_ordered_item]
print(f"  Most Ordered Item: {most_ordered_item} (appears in {most_ordered_count} orders)")


print("\n-- Adding New Day: 2025-01-05 --")

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]


print("\n-- Updated Revenue Per Day --")
daily_revenue = {}

for date, orders in sales_log.items():
    daily_total = sum(order["total"] for order in orders)
    daily_revenue[date] = daily_total
    print(f"  {date} : ₹{daily_total:.2f}")


best_day         = max(daily_revenue, key=lambda d: daily_revenue[d])
best_day_revenue = daily_revenue[best_day]
print(f"\n  Updated Best Selling Day : {best_day} (₹{best_day_revenue:.2f})")

print("\n-- All Orders (Numbered) --")

counter = 1
for date, orders in sales_log.items():
    for order in orders:
        # Join items list into a comma separated string
        items_str = ", ".join(order["items"])
        print(f"  {counter}. [{date}] Order #{order['order_id']:<3} — ₹{order['total']:.2f} — Items: {items_str}")
        counter += 1
