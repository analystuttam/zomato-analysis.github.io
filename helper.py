import plotly.express as px
import folium
import geopy.distance

def most_popular_cuisines(df3,c):
  fig = px.bar(df3, x=c.index, y=c, labels={'x': 'cuisines', 'y': 'count'})
  return fig


def rest_per_area(df):
  per_area = df[['state', 'State_area']]
  state = df['state'].unique()
  l = per_area['state'].value_counts()
  dic = {}
  for i in state:
    n = l[i]
    ar = df[df.state == i]['State_area']
    for z in ar:
      area = z
    a = n / area
    dic[i] = a
  perc = [i for i in dic.values()]
  fig = px.bar(x=list(dic.keys()), y=list(perc),
               labels={'x': 'State', 'y': "Count per Area"})
  fig.update_layout(xaxis={'categoryorder':'total descending'})
  return fig


def most_popular_chain(df):
  chain = df['name'].value_counts().head(20)
  fig = px.bar(x=chain.index, y=chain, labels={'x': 'Restaurant Chain', 'y': 'No. of Outlets'})
  return fig


def state_wise(df,state):
  state_df = df[df.state == state]
  s = state_df['city'].value_counts()
  fig = px.bar(x=s.index, y=s, labels={'x': 'City', 'y': 'No. of Restaurant'})
  return fig


def state_famous_cuisines(state_df):
  cuisines = state_df[0].value_counts().head(10)
  fig = px.pie(state_df, values=cuisines, names=cuisines.index, title='Most Popular Cuisines')
  return fig


def city_famous_cuisines(state_df):
  cuisines = state_df[0].value_counts().head(10)
  fig = px.pie(state_df, values=cuisines, names=cuisines.index, title='Most Popular Cuisines')
  return fig

def locality_famous_cuisines(state_df):
  cuisines = state_df[0].value_counts().head(10)
  fig = px.pie(state_df, values=cuisines, names=cuisines.index, title='Most Popular Cuisines')
  return fig


def res_type(df,restaurant):
  res_df = df[df.name== restaurant]
  cuisines = res_df['type'].value_counts()
  fig = px.pie(res_df, values=cuisines,names=cuisines.index,hole=0.7)
  return fig


def res_rating(df,restaurant):
  res_famous_food = df[df.name == restaurant]
  fig = px.histogram(res_famous_food, x='aggregate_rating', nbins=10)
  return fig


def res_distance(df,res1,res2):
  lat1 = df[df.res_id==res1]['latitude']
  lat2 = df[df.res_id == res2]['latitude']
  long1 = df[df.res_id == res1]['longitude']
  long2 = df[df.res_id == res2]['longitude']
  n1 = df[df.res_id==res1]['name']
  n2 = df[df.res_id == res2]['name']
  for a in n1:
    n1=a
  for b in n2:
    n2=b
  for i in lat1:
    lat1=i
  for x in lat2:
    lat2=x
  for y in long1:
    long1=y
  for w in long2:
    long2=w
  coords_1 = (lat1, long1)
  coords_2 = (lat2, long2)
  d = geopy.distance.geodesic(coords_1, coords_2).km
  d = round(d, 2)
  my_map4 = folium.Map(location=[lat1, long1],
                       zoom_start=5)
  folium.Marker([lat1, long1],
                popup=n1).add_to(my_map4)
  folium.Marker([lat2, long2],
                popup=n2).add_to(my_map4)
  folium.PolyLine(locations=[(lat2, long2), (lat1, long1)],
                  line_opacity=0.5, color='red', popup=d).add_to(my_map4)
  return my_map4

def res_avg_distance(df):
  c = 0
  latitude = list(df['latitude'])
  longitude = list(df['longitude'])
  for i in range(11):
    my_map4 = folium.Map(location=[latitude[c], longitude[c]],
                         zoom_start=14)
    folium.Marker([18.52479, 73.84149], popup="Group 12",icon=folium.Icon(color='red')).add_to(my_map4)

    folium.Marker([18.51768517, 73.8416668], popup='Cafe Goodluck').add_to(my_map4)
    folium.Marker([18.51420776, 73.83845586], popup='Le Plaisir').add_to(my_map4)
    folium.Marker([18.51401732, 73.84095702], popup='Darshan').add_to(my_map4)
    folium.Marker([18.53482102, 73.83816484], popup='Little Italy').add_to(my_map4)
    folium.Marker([18.53800334, 73.83577399], popup='Oriental Connexions').add_to(my_map4)
    folium.Marker([18.52256387, 73.84444457], popup="Shahji's Parantha House - The Coronet Hotel").add_to(my_map4)
    folium.Marker([18.51871459, 73.83625679], popup='Hippie@Heart').add_to(my_map4)
    folium.Marker([18.53479273, 73.83823056], popup='Spiceklub').add_to(my_map4)
    folium.Marker([18.51768517, 73.84940263], popup='The Leaf Kitchen').add_to(my_map4)
    folium.Marker([18.512355, 73.837219], popup='Karlo Art Kitchen & Cafe').add_to(my_map4)

    folium.PolyLine(locations=[(18.52479, 73.84149), (18.51768517, 73.8416668)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.51768517, 73.8416668)).km, 2)).add_to(
      my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.51420776, 73.83845586)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.51420776, 73.83845586)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.51401732, 73.84095702)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.51401732, 73.84095702)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.53482102, 73.83816484)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.53482102, 73.83816484)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.53800334, 73.83577399)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.53800334, 73.83577399)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.52256387, 73.84444457)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.52256387, 73.84444457)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.51871459, 73.83625679)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.51871459, 73.83625679)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.53479273, 73.83823056)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.53479273, 73.83823056)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.51768517, 73.84940263)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.51768517, 73.84940263)).km,
                                2)).add_to(my_map4)
    folium.PolyLine(locations=[(18.52479, 73.84149), (18.512355, 73.837219)], line_opacity=0.5,
                    popup=round(geopy.distance.geodesic((18.52479, 73.84149), (18.512355, 73.837219)).km, 2)).add_to(
      my_map4)
  d1 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.51768517, 73.8416668)).km, 2)
  d2 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.51420776, 73.83845586)).km, 2)
  d3 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.51401732, 73.84095702)).km, 2)
  d4 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.53482102, 73.83816484)).km, 2)
  d5 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.53800334, 73.83577399)).km, 2)
  d6 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.52256387, 73.84444457)).km, 2)
  d7 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.51871459, 73.83625679)).km, 2)
  d8 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.53479273, 73.83823056)).km, 2)
  d9 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.51768517, 73.84940263)).km, 2)
  d10 = round(geopy.distance.geodesic((18.52479, 73.84149), (18.512355, 73.837219)).km, 2)
  d = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10) / 10
  return my_map4,d



def res_rating_com(df,id1,id2):
  res1 = df[df.res_id == id1]['name']
  res2 = df[df.res_id == id2]['name']
  rat1 = df[df.res_id == id1]['aggregate_rating']
  rat2 = df[df.res_id == id2]['aggregate_rating']
  fig = px.bar(x=[list(res1)[0],list(res2)[0]],y=[list(rat1)[0],list(rat2)[0]],labels={'x':"Restaurant Name",'y':'Rating'},color_discrete_sequence=['#ec7c34'])
  return fig

def res_cost_com(df,id1,id2):
  res1 = df[df.res_id == id1]['name']
  res2 = df[df.res_id == id2]['name']
  rat1 = df[df.res_id == id1]['average_cost_for_two']
  rat2 = df[df.res_id == id2]['average_cost_for_two']
  fig = px.bar(x=[list(res1)[0],list(res2)[0]],y=[list(rat1)[0],list(rat2)[0]],labels={'x':"Restaurant Name",'y':'Average Cost For Two'},color_discrete_sequence=['#ec7c34'])
  return fig

def res_price_range(df,id):
  res_name = df[df.res_id == id]['name']
  res_name = list(res_name)[0]
  state_df = df[df.name == res_name]
  price_count = state_df['price_range'].value_counts()
  fig = px.pie(state_df, values=price_count, names=price_count.index,hole=0.6)
  return fig

def lun_dinn(df,id):
  lunch = 0
  dinner = 0
  res_name = df[df.res_id == id]['name']
  res_name = list(res_name)[0]
  res = df[df.name == res_name]
  for i in res['highlights']:
    i = i[2:-2]
    if 'Lunch' in i:
      lunch += 1
    else:
      dinner += 1
  l = ['Lunch', 'Dinner']
  v = [lunch, dinner]
  fig = px.pie(values=v, names=l, hole=0.7)
  return fig

def cuisines_wise_state(x,y):
  fig = px.bar(x=x , y=y, labels={'x': 'State', 'y': 'No. of Restaurant'})
  fig.update_layout(xaxis={'categoryorder': 'total descending'})
  return fig

def cuisines_wise_city(x,y):
  fig = px.bar(x=x, y=y, labels={'x': 'City', 'y': 'No. of Restaurant'})
  fig.update_layout(xaxis={'categoryorder': 'total descending'})
  return fig

def cuisines_wise_locality(df):
  df.columns = ['Locality','No. of Restaurant']
  fig = px.bar(data_frame=df,x='Locality', y='No. of Restaurant' , labels={'x': 'Locality', 'y': 'No. of Restaurant'})
  fig.update_layout(xaxis={'categoryorder': 'total descending'})
  return fig

def mul_rest(df4,lat,long):
  n=0
  my_map3 = folium.Map( location= [lat[n],long[n]],zoom_start='13')
  for i in lat:
    p = df4['name'][n]
    rat = str(df4['price_range'][n])
    avg_cost = str(df4['average_cost_for_two'][n])
    p=p+'(Price Range = '+rat+')'+'('+avg_cost+')'
    p=p+''
    if df4['price_range'][n]==1:
      color = 'green'
    elif df4['price_range'][n]==2:
      color='blue'
    elif df4['price_range'][n]==3:
      color='pink'
    else:
      color='red'
    folium.Marker([lat[n], long[n]],
                  popup=p,icon=folium.Icon(color=color)).add_to(my_map3)
    n += 1
  return my_map3


def highlights(df4, lat, long, h):
  n = 0
  my_map3 = folium.Map(location=[lat[n], long[n]], zoom_start='13')
  for i in lat:
    try:
      p = df4['name'][n]
      if h in df4['highlights'][n]:
        if df4['price_range'][n] == 1:
          color = 'green'
        elif df4['price_range'][n] == 2:
          color = 'blue'
        elif df4['price_range'][n] == 3:
          color = 'pink'
        else:
          color = 'red'
        folium.Marker([lat[n], long[n]],
                      popup=p, icon=folium.Icon(color=color)).add_to(my_map3)

    except:
      pass

    n += 1
  return my_map3



def mul_rest_rating(df4,lat,long):
  n=0
  my_map3 = folium.Map( location= [lat[n],long[n]],zoom_start='13')
  for i in lat:
    p = df4['name'][n]
    rat = str(df4['aggregate_rating'][n])
    p=p+'(rating = '+rat+')'
    p=p+''
    if df4['aggregate_rating'][n]<=2:
      color = 'red'
    elif df4['aggregate_rating'][n]>2 and df4['aggregate_rating'][n]<=3:
      color='blue'
    elif df4['aggregate_rating'][n]>3 and df4['aggregate_rating'][n]<=4:
      color='pink'
    else:
      color='green'
    folium.Marker([lat[n], long[n]],
                  popup=p,icon=folium.Icon(color=color)).add_to(my_map3)
    n += 1
  return my_map3

def locality_count(df):
  fig = px.bar(x=df.index,y=df,labels={'x':'Locality','y':'No. of Restaurant'})
  return fig

def veg_nveg(veg,nveg,lveg,lnveg):
  fig = px.pie(names=['Veg','Non-Veg'],values=[veg,nveg], color_discrete_map={'Veg':'g', 'Non-Veg':'r'})
  return fig

def lveg(lveg,lnveg):
  fig1 = px.pie(values=[lveg, lnveg], names=['Veg', 'Non-Veg'])
  return fig1

def alcohol(alco,nalco):
  fig1 = px.pie(values=[alco, nalco], names=['Alcohol', 'No-Alcohol'],hole=0.7)
  return fig1

def smoke(alco,nalco):
  fig1 = px.pie(values=[alco, nalco], names=['Smoking Area', 'No-Smoking Area'],hole=0.7)
  return fig1

def timings_charts(df):
  fig = px.bar(x=df.index, y=df, labels={'x': 'Timings', 'y': 'Count'})
  return fig

def dance(alco,nalco):
  fig1 = px.pie(values=[alco, nalco], names=['Dance Floor Available', 'Dance Floor Not Available'],hole=0.7)
  return fig1

def parking(alco,nalco):
  fig1 = px.pie(values=[alco, nalco], names=['Free Parking Available', 'Free Parking Not Available'],hole=0.7)
  return fig1