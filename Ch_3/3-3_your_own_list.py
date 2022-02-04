# 3-3 Your Own List

# Create my own list with examples of my favorite mode of transporation (bikes, obviously!).
# Then use it to print a series of statements about these items. 

bikes = ['kross', 'merida', 'kellys', 'romet']

# I'll just write about me buying my current bike, because why the hell not. In one print!

print(f"When I finally went to the bike shop, I was pretty set on getting a {bikes[3].title()} bike.\nI've already seen a few models from this manufacturer online, and I liked what I've seen.\nBut hey, being in a shop means that you can test the bikes yourself before buying anything, right?\nSo I've asked the clerk about some recommendations, and my preferred price range.\nAnd he said that for that price, I can get something better than a {bikes[3].title()}.\nThen he gave me three bikes to try out: a {bikes[0].title()}, a {bikes[1].title()} and a {bikes[2].title()}.\nAnd in the end, I've went with a bike from {bikes[2].title()}.\nIt's cool, I like it. LOL EOS")

# NOTE: Doing this in one print works, but readability seems mediocre at best. Then again, using 'print' for each line would introduce clutter. 
# ...This is fine, I guess.