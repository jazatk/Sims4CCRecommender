def recommend_cc(user_tags):
    import csv
    results = []

    # Open .csv data file in reader mode
    csv_file = open('data/cc_data.csv', 'r')
    reader = csv.DictReader(csv_file) # Create dictionary with each column

    for row in reader:
        cc_tags = row['tags'].split(',') # Create list of tags
        match_found = False
        for tag in user_tags:
            for cc_tag in cc_tags:
                if tag.lower() == cc_tag.lower():
                    match = {'name': row['name'],'link': row['link']}
                    results.append(match) # Add name and link to cc to results list if its tag matches user-inputted tag
                    match_found = True
                    break  # Stop checking cc_tags
            if match_found:
                break  # Stop checking user_tags

    csv_file.close()
    return results