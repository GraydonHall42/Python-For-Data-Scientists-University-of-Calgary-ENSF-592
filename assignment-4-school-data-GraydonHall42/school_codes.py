# Graydon Hall


# dictionary with key: School Name, Value: School Code
school_codes_dict = {
    "Bowness High School": 9847,
    "Centennial High School": 1224,
    "Central Memorial High School": 9823,
    "Crescent Heights High School": 9815,
    "Dr. E. P. Scarlett High School": 9858,
    "Ernest Manning High School": 9826,
    "Forest Lawn High School": 9813,
    "Henry Wise Wood High School": 9836,
    "Jack James High School": 9856,
    "James Fowler High School": 9825,
    "John G Diefenbaker High School": 9860,
    "Lester B. Pearson High School": 9865,
    "Lord Beaverbrook High School": 9850,
    "Louise Dean School": 9626,
    "National Sport School": 9830,
    "Queen Elizabeth High School": 9806,
    "Robert Thirsk School": 1679,
    "Sir Winston Churchill High School": 9857,
    "Western Canada High School": 9816,
    "William Aberhart High School": 9829,
}

# dictionary with key: School Code, Value: School Name
school_names_dict = {value : key for (key, value) in school_codes_dict.items()}
