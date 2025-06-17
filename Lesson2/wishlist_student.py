from wishlist import wish_list

while True:
    if len(wish_list) < 50:
        print(f'There is less than 50 items in the wishlist.\nThe current length is {len(wish_list)}')
        item = input("Item to add to the wishlist: ")
        if item not in wish_list:
            wish_list.append(item)
        else:
            print(f"Item '{item}' is already in wishlist\n")
    else:
        break

for wish in wish_list:
    print(f'Wish: {wish}')
"""
1. Import the wishlist Python file
2. Check the length (it needs to be 50)
3. If the length is not 50, append the additional items needed
4. Print the wish list 
"""
