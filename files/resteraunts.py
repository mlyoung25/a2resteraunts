import json

def combine_files():
    combined_data = []

    # Iterate over the files
    for i in range(1, 10):
        filename = f'{i}.json'

        # Open each file
        with open(filename, 'r') as file:
            data = json.load(file)
            combined_data.append(data)

    # Write combined data to restaurants.txt
    with open('restaurants.json', 'w') as outfile:
        json.dump(combined_data, outfile)

# Call the function
combine_files()