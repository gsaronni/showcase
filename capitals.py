print('Hey!')

print('Welcome to Capital City Challenge!')

print('Are you ready to play? Yes or No')

play = str(input())

while play.upper() != 'YES' and play.upper() != 'NO':
    print('Are you ready to play? Please type yes or no')
    play = str(input())

correct = 0
total = 0

africa = {
    'Ethiopia': 'Addis Ababa',
    'Tanzania': 'Dodoma',
    'Kenya': 'Nairobi',
    'Uganda': 'Kampala',
    'Mozambique': 'Maputo',
    'Madagascar': 'Antananarivo',
    'Malawi': 'Lilongwe',
    'Zambia': 'Lusaka',
    'Zimbabwe': 'Harare',
    'Somalia': 'Mogadishu',
    'South Sudan': 'Juba',
    'Rwanda': 'Kigali',
    'Burundi': 'Bujumbura',
    'Eritrea': 'Asmara',
    'Mauritius': 'Port Louis',
    'Djibouti': 'Djibouti',
    'Comoros': 'Moroni',
    'Seychelles': 'Victoria',
    'The Democratic Republic of the Congo': 'Kinshasa',
    'Angola': 'Luanda',
    'Cameroon': 'Yaounde',
    'Chad': 'N\'Djamena',
    'Republic of the Congo': 'Brazzaville',
    'Central African Republic': 'Bangui',
    'Gabon': 'Libreville',
    'Equatorial Guinea': 'Malabo',
    'Sao Tome and Principe': 'Sao Tome',
    'Egypt': 'Cairo',
    'Algeria': 'Algiers',
    'Sudan': 'Khartoum',
    'Morocco': 'Rabat',
    'Tunisia': 'Tunis',
    'Libya': 'Tripoli',
    'South Africa': 'Pretoria',
    'Namibia': 'Windhoek',
    'Botswana': 'Gaborone',
    'Lesotho': 'Maseru',
    'Swaziland': 'Mbabane',
    'Nigeria': 'Abuja',
    'Ghana': 'Accra',
    'Côte d\'Ivoire': 'Yamoussoukro',
    'Niger': 'Niamey',
    'Burkina Faso': 'Ouagadougou',
    'Mali': 'Bamako',
    'Senegal': 'Dakar',
    'Guinea': 'Conakry',
    'Benin': 'Porto-Novo',
    'Togo': 'Lome',
    'Sierra Leone': 'Freetown',
    'Liberia': 'Monrovia',
    'Mauritania': 'Nouakchott',
    'The Gambia': 'Banjul',
    'Guinea-Bissau': 'Bissau',
    'Cabo Verde': 'Praia'

}

asia = {
    'Yemen': 'Sanaa',
    'United Arab Emirates': 'Abu Dhabi',
    'Turkey': 'Ankara',
    'Syria': 'Damascus',
    'State of Palestine': 'East Jerusalem',
    'Saudi Arabia': 'Riyadh',
    'Qatar': 'Doha',
    'Oman': 'Muscat',
    'Lebanon': 'Beirut',
    'Kuwait': 'Kuwait City',
    'Jordan': 'Amman',
    'Israel': 'Tel Aviv',
    'Iraq': 'Baghdad',
    'Georgia': 'Tbilisi',
    'Cyprus': 'Nicosia',
    'Bahrain': 'Manama',
    'Azerbaijan': 'Baku',
    'Armenia': 'Yerevan',
    'Sri Lanka': 'Colombo',
    'Pakistan': 'Islamabad',
    'Nepal': 'Kathmandu',
    'Maldives': 'Male',
    'Iran': 'Tehran',
    'India': 'New Delhi',
    'Bhutan': 'Thimphu',
    'Bangladesh': 'Dhaka',
    'Afghanistan': 'Kabul',
    'Viet Nam': 'Hanoi',
    'East Timor (Timor-Leste)': 'Dili',
    'Thailand': 'Bangkok',
    'Singapore': 'Singapore',
    'Philippines': 'Manila',
    'Myanmar': 'Naypyidaw',
    'Malaysia': 'Kuala Lumpur',
    'Laos': 'Vientiane',
    'Indonesia': 'Jakarta',
    'Cambodia': 'Phnom Penh',
    'Brunei': 'Bandar Seri Begawan',
    'South Korea': 'Seoul',
    'North Korea': 'Pyongyang',
    'Mongolia': 'Ulaanbaatar',
    'Japan': 'Tokyo',
    'China': 'Beijing',
    'Uzbekistan': 'Tashkent',
    'Turkmenistan': 'Ashgabat',
    'Tajikistan': 'Dushanbe',
    'Kyrgyzstan': 'Bishkek',
    'Kazakhstan': 'Astana'
}

europe = {
    'Russia': 'Moscow',
    'Germany': 'Berlin',
    'United Kingdom': 'London',
    'France': 'Paris',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'Ukraine': 'Kiev',
    'Poland': 'Warsaw',
    'Romania': 'Bucharest',
    'Netherlands': 'Amsterdam',
    'Belgium': 'Brussels',
    'Greece': 'Athens',
    'Czech Republic': 'Prague',
    'Portugal': 'Lisbon',
    'Sweden': 'Stockholm',
    'Hungary': 'Budapest',
    'Belarus': 'Minsk',
    'Serbia': 'Belgrade',
    'Austria': 'Vienna',
    'Switzerland': 'Bern',
    'Bulgaria': 'Sofia',
    'Denmark': 'Copenhagen',
    'Finland': 'Helsinki',
    'Slovakia': 'Bratislava',
    'Norway': 'Oslo',
    'Ireland': 'Dublin',
    'Croatia': 'Zagreb',
    'Moldova': 'Chisinau',
    'Bosnia & Herzegovina': 'Sarajevo',
    'Albania': 'Tirana',
    'Lithuania': 'Vilnius',
    'Macedonia': 'Skopje',
    'Slovenia': 'Ljubljana',
    'Latvia': 'Riga',
    'Estonia': 'Tallinn',
    'Montenegro': 'Podgorica',
    'Luxembourg': 'Luxembourg City',
    'Malta': 'Valletta',
    'Iceland': 'Reykjavik',
    'Andorra': 'Andorra la Vella',
    'Monaco': 'Monaco',
    'Liechtenstein': 'Vaduz',
    'San Marino': 'San Marino'
}

americas = {
    'Argentina': 'Buenos Aires',
    'Bolivia': 'La Paz',
    'Brazil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogota',
    'Ecuador': 'Quito',
    'Guyana': 'Georgetown',
    'Paraguay': 'Asuncion',
    'Peru': 'Lima',
    'Suriname': 'Paramaribo',
    'Uruguay': 'Montevideo',
    'Venezuela': 'Caracas',
    'Belize': 'Belmopan',
    'Costa Rica': 'San Jose',
    'El Salvador': 'San Salvador',
    'Guatemala': 'Guatemala City',
    'Honduras': 'Tegucigalpa',
    'Mexico': 'Mexico City',
    'Nicaragua': 'Managua',
    'Panama': 'Panama City',
    'Antigua and Barbuda': 'Saint John\'s',
    'Bahamas': 'Nassau',
    'Barbados': 'Bridgetown',
    'Cuba': 'Havana',
    'Dominica': 'Roseau',
    'Dominican Republic': 'Santo Domingo',
    'Grenada': 'Saint George\'s',
    'Haiti': 'Port-au-Prince',
    'Jamaica': 'Kingston',
    'Saint Kitts and Nevis': 'Basseterre',
    'Saint Lucia': 'Castries',
    'Saint Vincent and the Grenadines': 'Kingstown',
    'Trinidad and Tobago': 'Port-of-Spain',
    'USA': 'Washington D.C',
    'Canada': 'Ottawa'
}

oceania = {
    'Australia': 'Canberra',
    'Papua New Guinea': 'Port Moresby',
    'New Zealand': 'Wellington',
    'Fiji': 'Suva',
    'Solomon Islands': 'Honiara',
    'Vanuatu': 'Port-Vila',
    'Samoa': 'Apia',
    'Kiribati': 'Tarawa Atoll',
    'Tonga': 'Nuku\'alofa',
    'Micronesia': 'Palikir',
    'Marshall Islands': 'Majuro',
    'Palau': 'Melekeok',
    'Tuvalu': 'Funafuti'

}

if play.upper() == 'NO':
    print('That\'s too bad. Come back when you are ready to play.')

    print('Bye!')

while play.upper() == 'YES':
    print('Excellent let\'s play!\n\nPlease choose a Continent:\nAfrica \nAsia \nEurope \nAmericas \nOceania')

    continent = input()
    while continent.lower() != 'africa' and continent.lower() != 'asia' and continent.lower() != 'europe' and continent.lower() != 'americas' and continent.lower() != 'oceania':
        print(
            '\nI\'m sorry that is not a valid option. Please choose one of the following Continents:\nAfrica \nAsia \nEurope \nAmericas \nOceania')
        continent = input()
    if continent.lower() == 'africa':
        print('Ok! let\'s see if you\'ll hear the drums echoing tonight.\n')
        for country, city in africa.items():
            total += 1
            print('What is the capital of ' + str(country))
            answer = input()
            if answer.lower() == city.lower():
                correct += 1
                print('Well Done! That is correct.')
                print('\n')
            elif answer.lower() != city.lower():
                print('Sorry,that is incorrect. The capital city of ' + str(country) + ' is ' + str(city))
                print('\n')
    elif continent.lower() == 'asia':
        print('Ok let\'s see if you know your stuff.\n')
        for country, city in asia.items():
            total += 1
            print('What is the capital of ' + str(country))
            answer = input()
            if answer.lower() == city.lower():
                correct += 1
                print('Well Done! That is correct.')
                print('\n')
            elif answer.lower() != city.lower():
                print('Sorry,that is incorrect. The capital city of ' + str(country) + ' is ' + str(city))
                print('\n')
    elif continent.lower() == 'europe':
        print('Ok let\'s see if you know your stuff.\n')
        for country, city in europe.items():
            total += 1
            print('What is the capital of ' + str(country))
            answer = input()
            if answer.lower() == city.lower():
                correct += 1
                print('Well Done! That is correct.')
                print('\n')
            elif answer.lower() != city.lower():
                print('Sorry,that is incorrect. The capital city of ' + str(country) + ' is ' + str(city))
                print('\n')

    elif continent.lower() == 'oceania':
        print('Ok let\'s see if you know your stuff.\n')
        for country, city in oceania.items():
            total += 1
            print('What is the capital of ' + str(country))
            answer = input()
            if answer.lower() == city.lower():
                correct += 1
                print('Well Done! That is correct.')
                print('\n')
            elif answer.lower() != city.lower():
                print('Sorry,that is incorrect. The capital city of ' + str(country) + ' is ' + str(city))
                print('\n')
    elif continent.lower() == 'americas':
        print('Ok let\'s see if you know your stuff.\n')
        for country, city in americas.items():
            total += 1
            print('What is the capital of ' + str(country))
            answer = input()
            if answer.lower() == city.lower():
                correct += 1
                print('Well Done! That is correct.')
                print('\n')
            elif answer.lower() != city.lower():
                print('Sorry,that is incorrect. The capital city of ' + str(country) + ' is ' + str(city))
                print('\n')

    print('Result:')
    if correct / total == 1:
        print('You got ' + str(correct) + ' out of cities ' + str(total) +
              ' correct.')
        print('Wow, you really know your stuff. Very Impressed!')
    elif correct / total > 0.7:
        print('You got ' + str(correct) + ' out of cities ' + str(total) +
              ' correct.')
        print('Quite the geographer we have here. I am impressed')
    elif correct / total > 0.5:
        print('You got ' + str(correct) + ' out of cities ' + str(total) +
              ' correct.')
        print('Not bad, not bad at all.')
    elif correct / total > 0.4:
        print('You got ' + str(correct) + ' out of cities ' + str(total) +
              ' correct.')
        print(
            'Admirable attemp young Grasshopper. Though there is yet room for improvement.'
        )
    else:
        print('You got ' + str(correct) + ' out of cities ' + str(total) +
              ' correct.')
        print('Looks like you need a little more practice.')
    print('\n')
    print('Do you want to play again?')
    print('Type \'Yes\' to play again. Or press any other button to Exit.')
    play = str(input())
    if play.upper() == 'YES':
        correct = 0
        total = 0
    if play.upper() == 'NO':
        print('OK, see you later! Bye!')
