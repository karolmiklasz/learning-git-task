shopping_dict={
    "piekarnia" : ["chleb","bułki","pączek"],
    "warzywniak" : ["marchew","seler","rukola"]
}
total_items = 0
for shop,items in shopping_dict.items():
    shop_upper = shop.capitalize()
    items_upper = [item.capitalize() for item in items]
    total_items += len(items)
    print(f"Idę do {shop_upper}, kupuję tu następujące rzeczy: {items_upper}.")