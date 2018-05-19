#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

    
#@app.errorhandler(400)
#def not_found(error):
#    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

#@app.errorhandler(404)
#def not_found(error):
#    return make_response(jsonify( { 'error': 'Not found' } ), 404)

countries = [
            {
                "countryName": "Andorra",
                "capital": "Andorra la Vella"
            },
            {
                "countryName": "United Arab Emirates",
                "capital": "Abu Dhabi"
            },
            {
                "countryName": "Afghanistan",
                "capital": "Kabul"
            },
            {
                "countryName": "Antigua and Barbuda",
                "capital": "St. John's"
            },
            {
                "countryName": "Anguilla",
                "capital": "The Valley"
            },
            {
                "countryName": "Albania",
                "capital": "Tirana"
            },
            {
                "countryName": "Armenia",
                "capital": "Yerevan"
            },
            {
                "countryName": "Angola",
                "capital": "Luanda"
            },
            {
                "countryName": "Antarctica",
                "capital": ""
            },
            {
                "countryName": "Argentina",
                "capital": "Buenos Aires"
            },
            {
                "countryName": "American Samoa",
                "capital": "Pago Pago"
            },
            {
                "countryName": "Austria",
                "capital": "Vienna"
            },
            {
                "countryName": "Australia",
                "capital": "Canberra"
            },
            {
                "countryName": "Aruba",
                "capital": "Oranjestad"
            },
            {
                "countryName": "Aland",
                "capital": "Mariehamn"
            },
            {
                "countryName": "Azerbaijan",
                "capital": "Baku"
            },
            {
                "countryName": "Bosnia and Herzegovina",
                "capital": "Sarajevo"
            },
            {
                "countryName": "Barbados",
                "capital": "BrcountryNamegetown"
            },
            {
                "countryName": "Bangladesh",
                "capital": "Dhaka"
            },
            {
                "countryName": "Belgium",
                "capital": "Brussels"
            },
            {
                "countryName": "Burkina Faso",
                "capital": "Ouagadougou"
            },
            {
                "countryName": "Bulgaria",
                "capital": "Sofia"
            },
            {
                "countryName": "Bahrain",
                "capital": "Manama"
            },
            {
                "countryName": "Burundi",
                "capital": "Bujumbura"
            },
            {
                "countryName": "Benin",
                "capital": "Porto-Novo"
            },
            {
                "countryName": "Saint Barthelemy",
                "capital": "Gustavia"
            },
            {
                "countryName": "Bermuda",
                "capital": "Hamilton"
            },
            {
                "countryName": "Brunei",
                "capital": "Bandar Seri Begawan"
            },
            {
                "countryName": "Bolivia",
                "capital": "Sucre"
            },
            {
                "countryName": "Bonaire",
                "capital": "Kralendijk"
            },
            {
                "countryName": "Brazil",
                "capital": "Brasilia"
            },
            {
                "countryName": "Bahamas",
                "capital": "Nassau"
            },
            {
                "countryName": "Bhutan",
                "capital": "Thimphu"
            },
            {
                "countryName": "Bouvet Island",
                "capital": ""
            },
            {
                "countryName": "Botswana",
                "capital": "Gaborone"
            },
            {
                "countryName": "Belarus",
                "capital": "Minsk"
            },
            {
                "countryName": "Belize",
                "capital": "Belmopan"
            },
            {
                "countryName": "Canada",
                "capital": "Ottawa"
            },
            {
                "countryName": "Cocos [Keeling] Islands",
                "capital": "West Island"
            },
            {
                "countryName": "Democratic Republic of the Congo",
                "capital": "Kinshasa"
            },
            {
                "countryName": "Central African Republic",
                "capital": "Bangui"
            },
            {
                "countryName": "Republic of the Congo",
                "capital": "Brazzaville"
            },
            {
                "countryName": "Switzerland",
                "capital": "Bern"
            },
            {
                "countryName": "Ivory Coast",
                "capital": "Yamoussoukro"
            },
            {
                "countryName": "Cook Islands",
                "capital": "Avarua"
            },
            {
                "countryName": "Chile",
                "capital": "Santiago"
            },
            {
                "countryName": "Cameroon",
                "capital": "Yaounde"
            },
            {
                "countryName": "China",
                "capital": "Beijing"
            },
            {
                "countryName": "Colombia",
                "capital": "Bogota"
            },
            {
                "countryName": "Costa Rica",
                "capital": "San Jose"
            },
            {
                "countryName": "Cuba",
                "capital": "Havana"
            },
            {
                "countryName": "Cape Verde",
                "capital": "Praia"
            },
            {
                "countryName": "Curacao",
                "capital": "Willemstad"
            },
            {
                "countryName": "Christmas Island",
                "capital": "Flying Fish Cove"
            },
            {
                "countryName": "Cyprus",
                "capital": "Nicosia"
            },
            {
                "countryName": "Czechia",
                "capital": "Prague"
            },
            {
                "countryName": "Germany",
                "capital": "Berlin"
            },
            {
                "countryName": "Djibouti",
                "capital": "Djibouti"
            },
            {
                "countryName": "Denmark",
                "capital": "Copenhagen"
            },
            {
                "countryName": "Dominica",
                "capital": "Roseau"
            },
            {
                "countryName": "Dominican Republic",
                "capital": "Santo Domingo"
            },
            {
                "countryName": "Algeria",
                "capital": "Algiers"
            },
            {
                "countryName": "Ecuador",
                "capital": "Quito"
            },
            {
                "countryName": "Estonia",
                "capital": "Tallinn"
            },
            {
                "countryName": "Egypt",
                "capital": "Cairo"
            },
            {
                "countryName": "Western Sahara",
                "capital": "Laayoune / El Aaiun"
            },
            {
                "countryName": "Eritrea",
                "capital": "Asmara"
            },
            {
                "countryName": "Spain",
                "capital": "MadrcountryName"
            },
            {
                "countryName": "Ethiopia",
                "capital": "Addis Ababa"
            },
            {
                "countryName": "Finland",
                "capital": "Helsinki"
            },
            {
                "countryName": "Fiji",
                "capital": "Suva"
            },
            {
                "countryName": "Falkland Islands",
                "capital": "Stanley"
            },
            {
                "countryName": "Micronesia",
                "capital": "Palikir"
            },
            {
                "countryName": "Faroe Islands",
                "capital": "Torshavn"
            },
            {
                "countryName": "France",
                "capital": "Paris"
            },
            {
                "countryName": "Gabon",
                "capital": "Libreville"
            },
            {
                "countryName": "United Kingdom",
                "capital": "London"
            },
            {
                "countryName": "Grenada",
                "capital": "St. George's"
            },
            {
                "countryName": "Georgia",
                "capital": "Tbilisi"
            },
            {
                "countryName": "French Guiana",
                "capital": "Cayenne"
            },
            {
                "countryName": "Guernsey",
                "capital": "St Peter Port"
            },
            {
                "countryName": "Ghana",
                "capital": "Accra"
            },
            {
                "countryName": "Gibraltar",
                "capital": "Gibraltar"
            },
            {
                "countryName": "Greenland",
                "capital": "Nuuk"
            },
            {
                "countryName": "Gambia",
                "capital": "Bathurst"
            },
            {
                "countryName": "Guinea",
                "capital": "Conakry"
            },
            {
                "countryName": "Guadeloupe",
                "capital": "Basse-Terre"
            },
            {
                "countryName": "Equatorial Guinea",
                "capital": "Malabo"
            },
            {
                "countryName": "Greece",
                "capital": "Athens"
            },
            {
                "countryName": "South Georgia and the South Sandwich Islands",
                "capital": "Grytviken"
            },
            {
                "countryName": "Guatemala",
                "capital": "Guatemala City"
            },
            {
                "countryName": "Guam",
                "capital": "Hagatna"
            },
            {
                "countryName": "Guinea-Bissau",
                "capital": "Bissau"
            },
            {
                "countryName": "Guyana",
                "capital": "Georgetown"
            },
            {
                "countryName": "Hong Kong",
                "capital": "Hong Kong"
            },
            {
                "countryName": "Heard Island and McDonald Islands",
                "capital": ""
            },
            {
                "countryName": "Honduras",
                "capital": "Tegucigalpa"
            },
            {
                "countryName": "Croatia",
                "capital": "Zagreb"
            },
            {
                "countryName": "Haiti",
                "capital": "Port-au-Prince"
            },
            {
                "countryName": "Hungary",
                "capital": "Budapest"
            },
            {
                "countryName": "Indonesia",
                "capital": "Jakarta"
            },
            {
                "countryName": "Ireland",
                "capital": "Dublin"
            },
            {
                "countryName": "Israel",
                "capital": ""
            },
            {
                "countryName": "Isle of Man",
                "capital": "Douglas"
            },
            {
                "countryName": "India",
                "capital": "New Delhi"
            },
            {
                "countryName": "British Indian Ocean Territory",
                "capital": ""
            },
            {
                "countryName": "Iraq",
                "capital": "Baghdad"
            },
            {
                "countryName": "Iran",
                "capital": "Tehran"
            },
            {
                "countryName": "Iceland",
                "capital": "Reykjavik"
            },
            {
                "countryName": "Italy",
                "capital": "Rome"
            },
            {
                "countryName": "Jersey",
                "capital": "Saint Helier"
            },
            {
                "countryName": "Jamaica",
                "capital": "Kingston"
            },
            {
                "countryName": "Jordan",
                "capital": "Amman"
            },
            {
                "countryName": "Japan",
                "capital": "Tokyo"
            },
            {
                "countryName": "Kenya",
                "capital": "Nairobi"
            },
            {
                "countryName": "Kyrgyzstan",
                "capital": "Bishkek"
            },
            {
                "countryName": "Cambodia",
                "capital": "Phnom Penh"
            },
            {
                "countryName": "Kiribati",
                "capital": "Tarawa"
            },
            {
                "countryName": "Comoros",
                "capital": "Moroni"
            },
            {
                "countryName": "Saint Kitts and Nevis",
                "capital": "Basseterre"
            },
            {
                "countryName": "North Korea",
                "capital": "Pyongyang"
            },
            {
                "countryName": "South Korea",
                "capital": "Seoul"
            },
            {
                "countryName": "Kuwait",
                "capital": "Kuwait City"
            },
            {
                "countryName": "Cayman Islands",
                "capital": "George Town"
            },
            {
                "countryName": "Kazakhstan",
                "capital": "Astana"
            },
            {
                "countryName": "Laos",
                "capital": "Vientiane"
            },
            {
                "countryName": "Lebanon",
                "capital": "Beirut"
            },
            {
                "countryName": "Saint Lucia",
                "capital": "Castries"
            },
            {
                "countryName": "Liechtenstein",
                "capital": "Vaduz"
            },
            {
                "countryName": "Sri Lanka",
                "capital": "Colombo"
            },
            {
                "countryName": "Liberia",
                "capital": "Monrovia"
            },
            {
                "countryName": "Lesotho",
                "capital": "Maseru"
            },
            {
                "countryName": "Lithuania",
                "capital": "Vilnius"
            },
            {
                "countryName": "Luxembourg",
                "capital": "Luxembourg"
            },
            {
                "countryName": "Latvia",
                "capital": "Riga"
            },
            {
                "countryName": "Libya",
                "capital": "Tripoli"
            },
            {
                "countryName": "Morocco",
                "capital": "Rabat"
            },
            {
                "countryName": "Monaco",
                "capital": "Monaco"
            },
            {
                "countryName": "Moldova",
                "capital": "Chisinau"
            },
            {
                "countryName": "Montenegro",
                "capital": "Podgorica"
            },
            {
                "countryName": "Saint Martin",
                "capital": "Marigot"
            },
            {
                "countryName": "Madagascar",
                "capital": "Antananarivo"
            },
            {
                "countryName": "Marshall Islands",
                "capital": "Majuro"
            },
            {
                "countryName": "Macedonia",
                "capital": "Skopje"
            },
            {
                "countryName": "Mali",
                "capital": "Bamako"
            },
            {
                "countryName": "Myanmar [Burma]",
                "capital": "Naypyitaw"
            },
            {
                "countryName": "Mongolia",
                "capital": "Ulan Bator"
            },
            {
                "countryName": "Macao",
                "capital": "Macao"
            },
            {
                "countryName": "Northern Mariana Islands",
                "capital": "Saipan"
            },
            {
                "countryName": "Martinique",
                "capital": "Fort-de-France"
            },
            {
                "countryName": "Mauritania",
                "capital": "Nouakchott"
            },
            {
                "countryName": "Montserrat",
                "capital": "Plymouth"
            },
            {
                "countryName": "Malta",
                "capital": "Valletta"
            },
            {
                "countryName": "Mauritius",
                "capital": "Port Louis"
            },
            {
                "countryName": "Maldives",
                "capital": "Male"
            },
            {
                "countryName": "Malawi",
                "capital": "Lilongwe"
            },
            {
                "countryName": "Mexico",
                "capital": "Mexico City"
            },
            {
                "countryName": "Malaysia",
                "capital": "Kuala Lumpur"
            },
            {
                "countryName": "Mozambique",
                "capital": "Maputo"
            },
            {
                "countryName": "Namibia",
                "capital": "Windhoek"
            },
            {
                "countryName": "New Caledonia",
                "capital": "Noumea"
            },
            {
                "countryName": "Niger",
                "capital": "Niamey"
            },
            {
                "countryName": "Norfolk Island",
                "capital": "Kingston"
            },
            {
                "countryName": "Nigeria",
                "capital": "Abuja"
            },
            {
                "countryName": "Nicaragua",
                "capital": "Managua"
            },
            {
                "countryName": "Netherlands",
                "capital": "Amsterdam"
            },
            {
                "countryName": "Norway",
                "capital": "Oslo"
            },
            {
                "countryName": "Nepal",
                "capital": "Kathmandu"
            },
            {
                "countryName": "Nauru",
                "capital": "Yaren"
            },
            {
                "countryName": "Niue",
                "capital": "Alofi"
            },
            {
                "countryName": "New Zealand",
                "capital": "Wellington"
            },
            {
                "countryName": "Oman",
                "capital": "Muscat"
            },
            {
                "countryName": "Panama",
                "capital": "Panama City"
            },
            {
                "countryName": "Peru",
                "capital": "Lima"
            },
            {
                "countryName": "French Polynesia",
                "capital": "Papeete"
            },
            {
                "countryName": "Papua New Guinea",
                "capital": "Port Moresby"
            },
            {
                "countryName": "Philippines",
                "capital": "Manila"
            },
            {
                "countryName": "Pakistan",
                "capital": "Islamabad"
            },
            {
                "countryName": "Poland",
                "capital": "Warsaw"
            },
            {
                "countryName": "Saint Pierre and Miquelon",
                "capital": "Saint-Pierre"
            },
            {
                "countryName": "Pitcairn Islands",
                "capital": "Adamstown"
            },
            {
                "countryName": "Puerto Rico",
                "capital": "San Juan"
            },
            {
                "countryName": "Palestine",
                "capital": ""
            },
            {
                "countryName": "Portugal",
                "capital": "Lisbon"
            },
            {
                "countryName": "Palau",
                "capital": "Melekeok"
            },
            {
                "countryName": "Paraguay",
                "capital": "Asuncion"
            },
            {
                "countryName": "Qatar",
                "capital": "Doha"
            },
            {
                "countryName": "Reunion",
                "capital": "Saint-Denis"
            },
            {
                "countryName": "Romania",
                "capital": "Bucharest"
            },
            {
                "countryName": "Serbia",
                "capital": "Belgrade"
            },
            {
                "countryName": "Russia",
                "capital": "Moscow"
            },
            {
                "countryName": "Rwanda",
                "capital": "Kigali"
            },
            {
                "countryName": "Saudi Arabia",
                "capital": "Riyadh"
            },
            {
                "countryName": "Solomon Islands",
                "capital": "Honiara"
            },
            {
                "countryName": "Seychelles",
                "capital": "Victoria"
            },
            {
                "countryName": "Sudan",
                "capital": "Khartoum"
            },
            {
                "countryName": "Sweden",
                "capital": "Stockholm"
            },
            {
                "countryName": "Singapore",
                "capital": "Singapore"
            },
            {
                "countryName": "Saint Helena",
                "capital": "Jamestown"
            },
            {
                "countryName": "Slovenia",
                "capital": "Ljubljana"
            },
            {
                "countryName": "Svalbard and Jan Mayen",
                "capital": "Longyearbyen"
            },
            {
                "countryName": "Slovakia",
                "capital": "Bratislava"
            },
            {
                "countryName": "Sierra Leone",
                "capital": "Freetown"
            },
            {
                "countryName": "San Marino",
                "capital": "San Marino"
            },
            {
                "countryName": "Senegal",
                "capital": "Dakar"
            },
            {
                "countryName": "Somalia",
                "capital": "Mogadishu"
            },
            {
                "countryName": "Suriname",
                "capital": "Paramaribo"
            },
            {
                "countryName": "South Sudan",
                "capital": "Juba"
            },
            {
                "countryName": "Sao Tome and Principe",
                "capital": "Sao Tome"
            },
            {
                "countryName": "El Salvador",
                "capital": "San Salvador"
            },
            {
                "countryName": "Sint Maarten",
                "capital": "Philipsburg"
            },
            {
                "countryName": "Syria",
                "capital": "Damascus"
            },
            {
                "countryName": "Swaziland",
                "capital": "Mbabane"
            },
            {
                "countryName": "Turks and Caicos Islands",
                "capital": "Cockburn Town"
            },
            {
                "countryName": "Chad",
                "capital": "N'Djamena"
            },
            {
                "countryName": "French Southern Territories",
                "capital": "Port-aux-Francais"
            },
            {
                "countryName": "Togo",
                "capital": "Lome"
            },
            {
                "countryName": "Thailand",
                "capital": "Bangkok"
            },
            {
                "countryName": "Tajikistan",
                "capital": "Dushanbe"
            },
            {
                "countryName": "Tokelau",
                "capital": ""
            },
            {
                "countryName": "East Timor",
                "capital": "Dili"
            },
            {
                "countryName": "Turkmenistan",
                "capital": "Ashgabat"
            },
            {
                "countryName": "Tunisia",
                "capital": "Tunis"
            },
            {
                "countryName": "Tonga",
                "capital": "Nuku'alofa"
            },
            {
                "countryName": "Turkey",
                "capital": "Ankara"
            },
            {
                "countryName": "TrincountryNamead and Tobago",
                "capital": "Port of Spain"
            },
            {
                "countryName": "Tuvalu",
                "capital": "Funafuti"
            },
            {
                "countryName": "Taiwan",
                "capital": "Taipei"
            },
            {
                "countryName": "Tanzania",
                "capital": "Dodoma"
            },
            {
                "countryName": "Ukraine",
                "capital": "Kiev"
            },
            {
                "countryName": "Uganda",
                "capital": "Kampala"
            },
            {
                "countryName": "U.S. Minor Outlying Islands",
                "capital": ""
            },
            {
                "countryName": "United States",
                "capital": "Washington"
            },
            {
                "countryName": "Uruguay",
                "capital": "MontevcountryNameeo"
            },
            {
                "countryName": "Uzbekistan",
                "capital": "Tashkent"
            },
            {
                "countryName": "Vatican City",
                "capital": "Vatican City"
            },
            {
                "countryName": "Saint Vincent and the Grenadines",
                "capital": "Kingstown"
            },
            {
                "countryName": "Venezuela",
                "capital": "Caracas"
            },
            {
                "countryName": "British Virgin Islands",
                "capital": "Road Town"
            },
            {
                "countryName": "U.S. Virgin Islands",
                "capital": "Charlotte Amalie"
            },
            {
                "countryName": "Vietnam",
                "capital": "Hanoi"
            },
            {
                "countryName": "Vanuatu",
                "capital": "Port Vila"
            },
            {
                "countryName": "Wallis and Futuna",
                "capital": "Mata-Utu"
            },
            {
                "countryName": "Samoa",
                "capital": "Apia"
            },
            {
                "countryName": "Kosovo",
                "capital": "Pristina"
            },
            {
                "countryName": "Yemen",
                "capital": "Sanaa"
            },
            {
                "countryName": "Mayotte",
                "capital": "Mamoudzou"
            },
            {
                "countryName": "South Africa",
                "capital": "Pretoria"
            },
            {
                "countryName": "Zambia",
                "capital": "Lusaka"
            },
            {
                "countryName": "Zimbabwe",
                "capital": "Harare"
            }
        ]
 

@app.route('/todo/api/v1.0/countries', methods=['GET'])
#@auth.login_required
def get_countries():
    return jsonify({'countries': countries})


@app.route('/todo/api/v1.0/countryName=<string:Name>', methods=['GET'])
def get_database(Name):
    capital = [database for database in countries if database['countryName'] == Name]
    return jsonify({'Data': capital[0]})
    
if __name__ == '__main__':
    app.run(debug = True)