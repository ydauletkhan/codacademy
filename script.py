# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
new_damages=[]
for i in damages:
  if "M" in i:
    i= float(i[:-1])*conversion.get("M")
  elif "B" in i:
    i=float(i[:-1])*conversion.get("B")
  new_damages.append(i)
  
#print(new_damages)

# 2 
hurricans={}
for i in range(len(names)):
 hurricans[names[i]]={'Name':names[i],'Month':months[i],'Year':years[i],'Max Sustained Wind':max_sustained_winds[i],'Areas Affected':areas_affected[i],'Damage':new_damages[i],'Deaths':deaths[i]}
#print(hurricans)
# Create a Table

# Create and view the hurricanes dictionary

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def yearss(year):
 hurricans_year=[]
 new_hurricans={}
 for i in range(len(names)):
  if hurricans.get(names[i]).get("Year")==year:
   hurricans_year.append(hurricans.get(names[i]))
 new_hurricans[year]=hurricans_year
 return new_hurricans
#print(yearss(1932))

# 4
# Counting Damaged Areas
def count_af():
 unique_areas=[]
 for i in areas_affected:
  for a in i:
    if not a in unique_areas:
      unique_areas.append(a)
 count=[0 for i in range(len(unique_areas))]
 for i in range(len(unique_areas)):
  for n in areas_affected:
    for b in n:
      if unique_areas[i]==b:
        count[i]=count[i]+1
 affected_areass={key:value for key, value in zip(unique_areas,count)}
 return affected_areass
#print(count_af().items())
def themost_a():
 max=0
 for keys, values in count_af().items():
  if values>max:
    max=values
    name=keys
 return name
#print(themost_a())
def max_death():
 max=0
 for keys, values in hurricans.items():
  if values.get("Deaths")>max:
    max=values.get("Deaths")
    name=keys
 return name
#print(max_death())
  
mortality_scalee = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000,
                   5: 20000}
def mort():
 mortality_scale=[0,100,500,1000,10000,20000]
 new_mort_scale=mortality_scale

 all_values=[list() for i in range(5)]
 for values in hurricans.values():
  for i in range(0,5):
   if (values.get("Deaths") < mortality_scale[i+1]) and (values.get("Deaths") > mortality_scale[i]) :
     all_values[i].append(values)

 keyss=list(range(5))

 mort={key:value for key, value in zip(keyss,all_values)}
 return mort

def damagee():
  maxx=0
  for values in hurricans.values():
   if not values.get("Damage")=="Damages not recorded":
    if values.get("Damage")>maxx:
     maxx=values.get("Damage")
     name=values.get("Name") 
  a=[name,maxx]
  return a
#print(damagee())







  

  




   
# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def damage():
 damage_scalee=[0,100000000,1000000000,10000000000,50000000000,20000000000000]
 

 all_values=[list() for i in range(5)]
 for values in hurricans.values():
  for i in range(0,5):
   if values.get("Damage")=="Damages not recorded":
    all_values[0].append(values)
   else:
     if (values.get("Damage") < damage_scalee[i+1]) and (values.get("Damage") > damage_scalee[i]) :
       all_values[i].append(values)
    
      
 keyss=list(range(5))
 mort={key:value for key, value in zip(keyss,all_values)}
 return mort
print(damage())
 #return mort
  
# categorize hurricanes in new dictionary with damage severity as key
