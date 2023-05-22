import folium
from scrapper4 import news_list
from folium.plugins import HeatMap
import re
from geopy.geocoders import Nominatim
import sys


geolocator = Nominatim(user_agent="my-app")



cities=["Andhra Pradesh","Seoni","Ajmer","Hoogly","Begusarai","Farrukhabad","Mansa","Sonipat","Borivali","Mathura", "Jubilee Hills","Guntur", "Amaravati","Burhanpur", "Visakhapatnam","Cuttak","Kalyanpuri","Ajmer","Patiala", "Sitamarhi","Tirupati", "Arunachal Pradesh", "Itanagar", "Assam", "Dispur", "Guwahati", "Bihar", "Patna", "Gaya", "Purulia","Fatehpur", "Muzaffarpur", "Chandigarh", "Chhattisgarh", "Raipur", "Bhilai", "Goa", "Panaji", "Gujarat", "Gandhinagar", "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Haryana", "Chandigarh","Kanpur", "Faridabad", "Gurugram", "Hisar", "Karnal", "Ambala", "Jammu and Kashmir", "Jammu", "Srinagar", "Jharkhand", "Ranchi", "Jamshedpur", "Bokaro Steel City", "Karnataka", "Bengaluru", "Mangalore", "Hubli", "Belgaum", "Gulbarga", "Shimoga", "Udupi", "Kerala", "Thiruvananthapuram", "Kochi", "Calicut", "Madhya Pradesh", "Bhopal", "Indore", "Jabalpur", "Maharashtra", "Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Thane", "Manipur", "Imphal", "Meghalaya", "Shillong", "Mizoram", "Aizawl", "Nagaland", "Kohima", "Odisha", "Bhubaneswar", "Cuttack", "Punjab", "Chandigarh", "Ludhiana", "Amritsar", "Rajasthan", "Jaipur", "Jodhpur", "Udaipur", "Bikaner", "Ajmer","Dwarka","Mathura","Gurdaspur","Sonipat", "Sikkim", "Gangtok", "Tamil Nadu", "Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Telangana", "Hyderabad", "Warangal", "Tripura", "Agartala", "Uttar Pradesh", "Lucknow", "Kanpur", "Agra", "Noida", "Varanasi", "Prayagraj", "Uttarakhand", "Dehradun", "West Bengal", "Kolkata", "Howrah", "Asansol", "Siliguri"]

if(len(news_list)<550):
    print("no new updates")
    sys.exit()

city_list = []
for string in news_list:
        for city in cities:
            if city in string:
                city_list.append(city)
            elif "Uttar Pradesh's" in string:
                city_list.append('Uttar Pradesh')
            elif "UP's" in string:
                city_list.append('Uttar Pradesh')
            elif "UP" in string:
                city_list.append('Uttar Pradesh')
            elif 'Bangalore' in string:
                city_list.append('Bengaluru')
            elif 'Mangalore' in string:
                city_list.append('Mangaluru')
            elif 'MP' in string:
                city_list.append('Madhya Pradesh')
            elif "MP's" in string:
                city_list.append('Madhya Pradesh')
            elif "Andhra" in string:
                city_list.append('Andhra Pradesh')
            elif "Andhra Pradesh's" in string:
                city_list.append('Andhra Pradesh')
            elif "Delhi" in string:
                city_list.append('New Delhi')
                
            
                
city_list.remove("Surat")

print(len(news_list))


    # Create a dictionary to store the frequency of each city
city_freq = {}
for city in city_list:
        if city not in city_freq:
            city_freq[city] = 1
        else:
            city_freq[city] += 1
print(city_freq)
    # Create a list of tuples with latitude, longitude and frequency of each city
city_coords_freq = []
for city in city_freq:
        coords = geolocator.geocode(city)[1]
        freq = city_freq[city]
        city_coords_freq.append((coords[0], coords[1], freq))

    # Create a folium map centered at India
india_coords = [20.5937, 78.9629]
m = folium.Map(location=india_coords, zoom_start=5)


    # Create a heatmap layer using the list of tuples
HeatMap(city_coords_freq, radius=15, blur=10).add_to(m)

    # Display the map



m.save('templates/final.html') 
print("Heat Map Generated. Refresh to see the results.")
    #HeatMap(data).add_to(mapObj)




