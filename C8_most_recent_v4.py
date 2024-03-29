# get data from user and store it in a list, then
# display the most recent three entries nicely

# set up empty list
all_calculations = []
MAX_CALCS = 5

# get five items of data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

print()

# show that everything made it to the list...
print()
print("**** Most Recent ****")
print(all_calculations)

# print items starting at the end of the list
if len(all_calculations) >= MAX_CALCS:
    print()
    print("**** Most Recent ****")
    for item in range(0, MAX_CALCS):
        print(all_calculations[len(all_calculations) - item - 1])

else:
    print()
    print("**** Items from Newest to Oldest ****")
    for item in all_calculations:
        print(all_calculations[len(all_calculations) - all_calculations.index(item) - 1])

