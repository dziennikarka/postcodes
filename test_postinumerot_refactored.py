import postinumerot_refactored
import http_pyynto

RAW_DATA = {
    '74701': 'KIURUVESI',
    '35540': 'JUUPAJOKI',
    '02580': 'SIUNTIO',
    '74700': 'KIURUVESI'
}

INVERSED_DATA = {
    'KIURUVESI': ['74701', '74700'],
    'JUUPAJOKI': ['35540'],
    'SIUNTIO': ['02580']
}

DIFFIRENT_NAMES_DATA = {
    '74704': 'SMARTPOST',
    '73464': 'SMARTPOST',
    '44884': 'SMART POST',
    '89604': 'SMARTPSOT',
    '00100': 'HELSINKI',
    '00102': 'HEL SINKI',
    '55604': 'YLIVIESKA',
    '55605': 'YLI-VIESKA'
}

INVERSED_DIFFERENT_NAMES = {
    'SMARTPOST': ['74704', '73464', '44884', '89604'],
    'HELSINKI': ['00100', '00102'],
    'YLIVIESKA': ['55604', '55605']
}

# probable better to put in a separate test module test_http_pyynto


def test_http_request():
    connection_check = http_pyynto.search_indexes()
    assert len(connection_check) > 0


def test_zipcodes_inversed():
    result = postinumerot_refactored.group_by_cities(RAW_DATA)
    assert result == INVERSED_DATA


def test_one_zipcode():
    place = 'SIUNTIO'
    place_one_zipcode = postinumerot_refactored.search_by_city(
        place, INVERSED_DATA)
    assert place_one_zipcode == '02580'


def test_several_zipcodes():
    place = 'KIURUVESI'
    place_several_zipcodes = postinumerot_refactored.search_by_city(
        place, INVERSED_DATA)
    assert place_several_zipcodes == '74700, 74701'


def test_typo():
    place = 'SUNTIO'
    place_typo = postinumerot_refactored.search_by_city(place, INVERSED_DATA)
    assert place_typo == None


def test_print_none():
    result = None
    zipcode_not_found = postinumerot_refactored.to_print(result)
    assert zipcode_not_found == 'Not found'


def test_print_zipcodes():
    result = '74700, 74701'
    zipcode_list = postinumerot_refactored.to_print(result)
    assert zipcode_list == ('Postinumerot: ' + result)


def test_multiple_names():
    zipcode_multiple_names = postinumerot_refactored.group_by_cities(
        DIFFIRENT_NAMES_DATA)
    assert zipcode_multiple_names == INVERSED_DIFFERENT_NAMES
