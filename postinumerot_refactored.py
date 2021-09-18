import http_pyynto

# reading the data
zipcodes = http_pyynto.search_indexes()

# function that groups data by cities


def group_by_cities(indexes):
    # creating a new dictionary with cities as keys
    cities_indexes = {}

    # reversing the dectionary
    for number, place in indexes.items():

        # ----------------------NORMALIZATION OF DATA----------------------------------
        # checking if the place contains spaces
        if ' ' in place:
            place = place.replace(' ', '')

        if '-' in place:
            place = place.replace('-', '')

        # correcting typo in smartpost
        # for now this just works for smartpost as a special case
        if place == 'SMARTPSOT':
            place = 'SMARTPOST'
        # -----------------------NORMALIZATION OF DATA ENDS HERE------------------------

        # creating an empty list if the city is not in the dictionary
        if place not in cities_indexes:
            cities_indexes[place] = []

        cities_indexes[place].append(number)
    return cities_indexes

# function that searches for zipcodes and sorts them based on the city


def search_by_city(city, post_cities):
    if city in post_cities:
        post_cities[city].sort()
        return ', '.join(post_cities[city])
    else:
        return None

# function that prints the results


def to_print(result):
    if(result == None):
        return 'Not found'
    else:
        return 'Postinumerot: ' + result


def main():
    # asking user for a name of the city
    city = input('Kirjoita postitoimipaikka: ').strip().upper()

    # inversing the data so that cities = keys
    post_cities = group_by_cities(zipcodes)

    # searching the zipcodes for a particular city
    zipcodes_list = search_by_city(city, post_cities)

    # printing out the result
    print(to_print(zipcodes_list))


if __name__ == '__main__':
    main()
