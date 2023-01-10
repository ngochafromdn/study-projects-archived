'''
This Python function are to track the Internaltion Space Station's current position, posting updates every 10 secoonds.
Name: Le Thi Hong Ha (ID:210205), Nguyen Hoang Ngoc Ha (ID:210206)
Time : 24 hours
'''

def track_iss():
    import json
    import requests
    import time
    end_status_land=0
    end_status_ocean=0
    coord = [] #list of coordinates as pair of latitude and logitude
    #set the loop to run for 5 mins (30 OpenNotify calls)
    for i in range(0,30,1):
      #get the iss data
      iss_data = requests.get('http://api.open-notify.org/iss-now.json')
      #check if the data is in successfully
      if iss_data.status_code in (200,400):
        iss_data_json = iss_data.json()
      else:
        break
      #get the latitude and longitude of the current iss position
      latitude = iss_data_json['iss_position']['latitude']
      longitude = iss_data_json['iss_position']['longitude']
      coord.append([latitude, longitude])

      ocean_link='http://api.geonames.org/oceanJSON?formatted=true&'+'lat='+str(latitude)+'&lng=' + str(longitude)+'&username=habeodepzai'
      geodata_name = requests.get(ocean_link)
      if geodata_name.status_code in (200,400):
        geodata_json=geodata_name.json()
      else:
        break
      #check if status is in the data to apply the land_link or ocntinue with the ocean_link above
      if 'status' in geodata_json.keys():
        land_link='http://api.geonames.org/findNearbyJSON?formatted=true&lat='+str(latitude)+'&lng='+str(longitude)+'&username=habeodepzai'
        geodata_name=requests.get(land_link)
        if geodata_name.status_code in (200,400):
          geodata_json = geodata_name.json()
        else:
          break
        geodata_json=geodata_name.json()
        print('Current ISS position:',str(latitude) +',' ,str(longitude),'(over',geodata_json['geonames'][0]['name']+',',geodata_json['geonames'][0]['countryName']+')')
        end_status_land=1
      else:
        print('Current ISS position:',str(latitude) +',' ,str(longitude),'(over',geodata_json['ocean']['name']+')')
        end_status_ocean=1
      #check if whether the program has run through ocean to land or vice versa to stop the loop
      if (end_status_land+end_status_ocean)==2:
        break
      #set the times pausing to 10 seconds
      time.sleep(10)
    return coord 
    
def ggmap(lst):
    import webbrowser
    #get the latitude and longitude of the current iss position
    url = "https://www.google.com/maps/dir"
    for pair in lst:
        url = url + "/" + pair[0] + "," + pair[1]
    print(url)
    print("Wait to open the link...")
    webbrowser.open(url)
    
#Uncomment to run extra credits function
#link = track_iss()
#ggmap(link)      
      
    