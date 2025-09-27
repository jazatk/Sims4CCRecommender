from recommender import recommend_cc

user_input = input("Enter tags (comma-separated): ")
split_tags = user_input.split(',') # Turn user input into list
user_tags = []

for tag in split_tags:
    cleaned_tag = tag.strip().lower() # Remove any spaces in tags
    if cleaned_tag != '':
        user_tags.append(cleaned_tag)


results = recommend_cc(user_tags)

print("\nRecommended CC:")
if results:
    for item in results:
        print(f"{item['name']}: {item['link']}") # Print CC name and link from data file
else:
    print("No matches found. Try using different tags.")