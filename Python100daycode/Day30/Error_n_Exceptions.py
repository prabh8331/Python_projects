#Exception Handling


### Index error exception handling example 
 
# fruits = eval(input())  #this will convert formatted string to list
#["Apple", "Pear", "Orange"]

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
        # print(fruit + " pie")
    except IndexError as error_message:
        print("Fruit pie")
        print(f"Error: {error_message}")
    else:
        print(fruit+ " pie")

# Exception handling is very important skill, (if not a little bit neglected by developer because it's not fun thinking about edge cases and handling them each time) but this is important skill on road to become a professional developer.

make_pie(4)


### Key error exception handling example 

# facebook_posts = eval(input())
facebook_posts = [{'Likes': 21, 'Comments': 2},
                  {'Likes': 13, 'Comments': 2, 'Shares': 1},
                  {'Likes': 33, 'Comments': 8, 'Shares': 3},
                  {'Comments': 4, 'Shares': 2},
                  {'Comments': 1, 'Shares': 1},
                  {'Likes': 19, 'Comments': 3}
                  ]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes = total_likes + 0

print(total_likes)
## exception handling is incredibly effective and incredibly useful,  although it is sometimes neglected by developers
# but by hopefully learning more exceptions and thinking about exception handling using try/accept blocks,
# you're getting to grips around a really key part of development, which is error and exception handling.