countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
#  Loop through the countries and extract all the countries containing the word land.

for i in countries : 
  if 'land' in i : 
    print(i)

  # reverse the order using loop
  fruit = ['banana', 'orange', 'mango', 'lemon']
  rev = []
  for i in range(len(fruit)) : 
    rev.append(fruit[len(fruit)-i-1])
  print(rev)

  # What are the total number of languages in the data
  # Find the ten most spoken languages from the data
  # Find the 10 most populated countries in the world
# assume we have a dictionary having all this data asked in this question
''' that's a demo object from a dictionary
{
  "name": "Afghanistan",
  "capital": "Kabul",
  "languages": [
      "Pashto",
      "Uzbek",
      "Turkmen"
  ],
  "population": 27657145,
  "flag": "https://restcountries.eu/data/afg.svg",
  "currency": "Afghan afghani"
}
'''
# 1 - loop in dictionary(having mulriple objects), each object have a key 'languages' which is a list 
     # we have to print total number of languages in dictionary
totalLang = 0
for i in countries : 
  print(i['languages'])  # this will print all the languages in the dictionary
  print(i['languages'].__len__())  # this will print the number of languages in the dictionary
  totalLang += i['languages'].__len__()

print(totalLang)  # this will print the total number of languages in the dictionary

# 2. most spoken one - we'll save evey language in a list and then count the frequency of each language,
    #  print the highest frequency one
topLang = {}
for i in countries : 
  for i in i['languages'] : 
    topLang[i] = topLang.get(i, 0) + 1  # if language is not in dictionary, add it with value 1, else increment its value
print(topLang)  # this will print the dictionary with languages and their frequencies

# 3. Find the 10 most populated countries in the world
mostPop = {}
for i in countries : 
  for i in i['population'] : 
    mostPop[i] = mostPop.get(i, 0) + 1

print(mostPop)  # this will print the total number of populations in the dictionary
