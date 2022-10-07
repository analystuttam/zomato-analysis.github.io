import streamlit as st
import pandas as pd
import preprocess
import helper
from streamlit_folium import st_folium
from PIL import Image

icon = Image.open('./favicon.png')
st.set_page_config(page_title= 'Zomato Analysis',page_icon=icon)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1515549832467-8783363e19b6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=327&q=80");
background-size: cover;
}
</style>

'''
st.markdown(page_bg_img,unsafe_allow_html=True)

st.sidebar.write('Bsc Data Analytics(Sec A)')
st.sidebar.write('Group 12')
df = pd.read_csv('final.csv')
gp12 = pd.read_csv('gp 12.csv')
raw = preprocess.show(df)
st.sidebar.image('zomato.jpg')
user_menu = st.sidebar.radio(
    'Select an option',
    ('Pan India Analysis', 'State-wise Analysis', 'Restaurant-Wise Analysis', 'Food-wise Analysis', 'People Analysis',
     'Restaurants on Map')
)

# User Menu

if user_menu == 'Pan India Analysis':
    st.header('Pan India Analysis')
    st.sidebar.header('Pan India Analysis')
    res_chain = df['name'].nunique()
    no_of_res = df['res_id'].nunique()
    no_of_city = df['city'].nunique()
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader("Restaurant Chain")
        st.title(res_chain)
    with col2:
        st.subheader("No of Restaurant")
        st.title(no_of_res)
    with col3:
        st.subheader("City")
        st.title(no_of_city)
    st.dataframe(raw)
    st.subheader('Number of restaurants per sq. km. of area')
    fig = helper.rest_per_area(df)
    st.plotly_chart(fig)
    l = df['cuisines']
    list(l)
    l2 = []
    s = ''
    for i in l:
        try:
            w = i.split(',')
            for y in w:
                y = y.lstrip()
                y = y.rstrip()
                l2.append(y)

        except:
            pass
    df3 = pd.DataFrame(l2)
    size = len(set(l2))
    value = st.slider(
        'Select a range of values',
        0, size, (0, 25))
    start=value[0]
    end=value[1]
    c = df3[0].value_counts()[start:end]
    st.subheader('Most Popular Cuisines')

    fig = helper.most_popular_cuisines(df3,c)
    st.plotly_chart(fig)
    st.subheader('Most Popular Chain')
    fig = helper.most_popular_chain(df)
    st.plotly_chart(fig)


elif user_menu == 'State-wise Analysis':
    st.header('State Wise Analysis')
    sta = df['state'].value_counts()
    sta = [j for j in sta.index]
    sta.sort()
    state = st.sidebar.selectbox('Select State',sta)
    state_df = df[df.state == state]
    ci = state_df['city'].value_counts()
    ci = [j for j in ci.index]
    ci.sort()
    city = st.sidebar.selectbox('Select City', ci)
    loc = state_df['locality'].value_counts()
    loc = [j for j in loc.index]
    loc.sort()
    locality = st.sidebar.selectbox('Select locality', loc)
    st.subheader('City Wise No. of Restaurant in '+state)
    fig = helper.state_wise(df, state)
    st.plotly_chart(fig)
    st.subheader("Famous Cuisines in "+state)
    l = df[df.state == state]['cuisines']
    list(l)
    l2 = []
    s = ''
    for i in l:
        try:
            w = i.split(',')
            for y in w:
                l2.append(y)
        except:
            pass
    l3 = []
    for i in l2:
        s = ''
        sp = i[0]
        if sp.isspace():
            i = i[1:]
        for y in i:
            s += y
        l3.append(s)
    c_l = state_df[state_df.city == city]['cuisines']
    list(c_l)
    c_l2 = []
    s = ''
    for i in c_l:
        try:
            w = i.split(',')
            for y in w:
                c_l2.append(y)
        except:
            pass
    c_l3 = []
    for i in c_l2:
        s = ''
        sp = i[0]
        if sp.isspace():
            i = i[1:]
        for y in i:
            s += y
        c_l3.append(s)
    l_l = state_df[state_df.locality == locality]['cuisines']
    list(l_l)
    l_l2 = []
    s = ''
    for i in l_l:
        try:
            w = i.split(',')
            for y in w:
                l_l2.append(y)
        except:
            pass
    l_l3 = []
    for i in l_l2:
        s = ''
        sp = i[0]
        if sp.isspace():
            i = i[1:]
        for y in i:
            s += y
        l_l3.append(s)
    df3 = pd.DataFrame(l3)
    c_df3 = pd.DataFrame(c_l3)
    l_df3 = pd.DataFrame(l_l3)
    fig = helper.state_famous_cuisines(df3)
    st.plotly_chart(fig)
    st.subheader("Famous Cuisines in " + city)
    fig = helper.city_famous_cuisines(c_df3)
    st.plotly_chart(fig)
    st.subheader("Famous Cuisines in " + locality)
    fig = helper.locality_famous_cuisines(l_df3)
    st.plotly_chart(fig)
    chain_sta = df[df.state == state]
    st.subheader('Famous Chain in ' + state)
    fig = helper.most_popular_chain(chain_sta)
    st.plotly_chart(fig)
    chain_city = df[df.city==city]
    st.subheader('Famous Chain in '+city)
    fig = helper.most_popular_chain(chain_city)
    st.plotly_chart(fig)
    alco = 0
    nalco=0
    for i in chain_city['highlights']:
        if 'Serves Alcohol' in i:
            alco+=1
        elif 'No Alcohol Available' in i:
            nalco+=1
    df_alco = df[df.locality == locality]
    l_alco = 0
    l_nalco = 0
    for i in df_alco['highlights']:
        if 'Serves Alcohol' in i:
            l_alco += 1
        elif 'No Alcohol Available' in i:
            l_nalco += 1
    smoke=0
    nsmoke=0
    for i in chain_city['highlights']:
        if 'Smoking Area' in i:
            smoke+=1
        else:
            nsmoke+=1
    l_smoke = 0
    l_nsmoke = 0
    df_smoke = df[df.locality == locality]
    for i in df_smoke['highlights']:
        if 'Smoking Area' in i:
            l_smoke+=1
        else:
            l_nsmoke+=1
    c_dan = 0
    c_ndan = 0
    for i in chain_city['highlights']:
        if 'Dance Floor' in i:
            c_dan += 1
        else:
            c_ndan += 1
    dan= 0
    ndan=0
    for i in df_smoke['highlights']:
        if 'Dance Floor' in i:
            dan += 1
        else:
            ndan += 1
    par = 0
    npar = 0
    for i in chain_city['highlights']:
        if 'Free Parking' in i:
            par += 1
        else:
            npar += 1
    l_par = 0
    l_npar = 0
    for i in df_smoke['highlights']:
        if 'Free Parking' in i:
            l_par += 1
        else:
            l_npar += 1
    st.subheader('Alcohol vs No Alcohol in '+city)
    fig = helper.alcohol(alco,nalco)
    st.plotly_chart(fig)
    st.subheader('Alcohol vs No Alcohol in ' + locality)
    fig = helper.alcohol(l_alco, l_nalco)
    st.plotly_chart(fig)
    st.subheader('Smoking vs No Smoking Area in '+city)
    fig = helper.smoke(smoke, nsmoke)
    st.plotly_chart(fig)
    st.subheader('Smoking vs No Smoking Area in ' + locality)
    fig = helper.smoke(l_smoke, l_nsmoke)
    st.plotly_chart(fig)
    # timings = chain_city['timings'].value_counts().head(15)
    # fig = helper.timings_charts(timings)
    # st.subheader("Restaurant Timings in "+city)
    # st.plotly_chart(fig)
    # l_timings = df_smoke['timings'].value_counts().head(15)
    # fig = helper.timings_charts(l_timings)
    # st.subheader("Restaurant Timings in " + locality)
    # st.plotly_chart(fig)
    st.subheader('Dance Floor in ' + city)
    fig = helper.dance(c_dan,c_ndan)
    st.plotly_chart(fig)
    fig = helper.dance(dan,ndan)
    st.subheader('Dance Floor in ' + locality)
    st.plotly_chart(fig)
    st.subheader('Free Parking in ' + city)
    fig = helper.parking(par, npar)
    st.plotly_chart(fig)
    fig = helper.parking(l_par, l_npar)
    st.subheader('Free Parking in ' + locality)
    st.plotly_chart(fig)



elif user_menu == 'Restaurant-Wise Analysis':
    st.title('Restaurant-Wise Analysis')
    res = df['name'].value_counts()
    res = [j for j in res.index]
    res.sort()
    res_name = st.sidebar.selectbox("Select Restaurant", res)
    fig = helper.res_type(df,res_name)
    st.subheader(res_name+" Establishment Type")
    st.plotly_chart(fig)
    st.subheader(res_name+' Rating')
    fig = helper.res_rating(df, res_name)
    st.plotly_chart(fig)
    st.write(df[df.name==res_name]['highlights'])
    state_list = df['state'].sort_values().unique()
    state = st.selectbox("Select State",state_list)
    city_list = df[df.state==state]['city'].sort_values().unique()
    city = st.selectbox('Select City',city_list)
    locality_list = df[df.city==city]['locality'].sort_values().unique()
    locality = st.selectbox('Select Locality',locality_list)
    locality_df = df[df.locality==locality]
    restaurant_name1 = locality_df['name'].sort_values().unique()
    restaurant_name2 = df[df.locality==locality]['name'].unique()
    rest_1 = st.selectbox('Restaurant ID :', restaurant_name1,key=1)
    rest_2 = st.selectbox('Restaurant ID :', restaurant_name2,key=2)
    rest1 = locality_df[locality_df.name == rest_1]['res_id']
    rest1 = rest1.reset_index(drop=True)
    rest1 = rest1[0]
    rest2 = locality_df[locality_df.name == rest_2]['res_id']
    rest2 = rest2.reset_index(drop=True)
    rest2 = rest2[0]
    st.subheader('Rating Comparision')
    fig = helper.res_rating_com(df, rest1, rest2)
    st.plotly_chart(fig)
    st.subheader('Average cost for two Comparision')
    fig = helper.res_cost_com(df,rest1,rest2)
    st.plotly_chart(fig)

    n1 = list(df[df.res_id == rest1]['name'])[0]
    n2 = list(df[df.res_id == rest2]['name'])[0]
    fig = helper.res_price_range(df, rest1)
    st.title(n1+" Price Range Distribution")
    st.plotly_chart(fig)
    fig = helper.res_price_range(df, rest2)
    st.title(n2 + " Price Range Distribution")
    st.plotly_chart(fig)
    fig = helper.lun_dinn(df,rest1)

    st.title("Lunch vs Dinner in "+n1)
    st.plotly_chart(fig)
    fig = helper.lun_dinn(df, rest2)

    st.title("Lunch vs Dinner in " + n2)
    st.plotly_chart(fig)
    restaurant_id1_ = df['res_id'].sort_values().unique()
    restaurant_id2_ = df['res_id'].sort_values().unique()
    st.subheader('Distance Between Restaurant')
    rest1_ = st.selectbox('Restaurant ID :', restaurant_id1_, key=3)
    rest2_ = st.selectbox('Restaurant ID :', restaurant_id2_, key=4)
    chart = helper.res_distance(df, rest1_, rest2_)
    st.write('Click on Icon on map to see Restaurant Name and Distance')
    st_folium(chart, width=800)
    st.subheader('Rating Comparision')
    fig = helper.res_rating_com(df, rest1_, rest2_)
    st.plotly_chart(fig)
    st.subheader('Average cost for two Comparision')
    fig = helper.res_cost_com(df, rest1_, rest2_)
    st.plotly_chart(fig)

    n1_ = list(df[df.res_id == rest1_]['name'])[0]
    n2_ = list(df[df.res_id == rest2_]['name'])[0]
    fig = helper.res_price_range(df, rest1_)
    st.title(n1_ + " Price Range Distribution")
    st.plotly_chart(fig)
    fig = helper.res_price_range(df, rest2_)
    st.title(n2_ + " Price Range Distribution")
    st.plotly_chart(fig)
    fig = helper.lun_dinn(df, rest1_)

    st.title("Lunch vs Dinner in " + n1_)
    st.plotly_chart(fig)
    fig = helper.lun_dinn(df, rest2_)

    st.title("Lunch vs Dinner in " + n2_)
    st.plotly_chart(fig)



elif user_menu == 'Food-wise Analysis':
    st.title('Food-wise Analysis')
    state = list(df['state'].unique())
    l = df['cuisines']
    list(l)
    l2 = []
    s = ''
    for i in l:
        try:
            w = i.split(',')
            for y in w:
                l2.append(y)
        except:
            pass
    l3=[]
    for i in l2:
        s = ''
        sp = i[0]
        if sp.isspace():
            i = i[1:]
        for y in i:
            s += y
        l3.append(s)
    l3 = set(l3)
    l3 = list(l3)
    cuisines = st.selectbox('Select Cuisines',l3)
    f = {}
    for i in state:
        n = 0
        c = 0
        for y in df['state']:
            try:
                if i == y:
                    if cuisines in df['cuisines'][n]:
                        c += 1
            except:
                pass
            f[i] = c
            n += 1
    state_x = list(f.keys())
    res_y = list(f.values())
    fig = helper.cuisines_wise_state(state_x, res_y)
    st.subheader("Cuisines : ("+cuisines+") Restaurant in Different States")
    st.plotly_chart(fig)
    state_cus = df['state'].sort_values().unique()
    state_food = st.selectbox('Select State',state_cus)
    state = list(df[df.state == state_food]['city'])
    state_df = set(state)
    state_df = list(state_df)
    l = df['cuisines']
    list(l)
    l2 = []
    s = ''
    for i in l:
        try:
            w = i.split(',')
            for y in w:
                l2.append(y)
        except:
            pass
    l3 = []
    for i in l2:
        s = ''
        sp = i[0]
        if sp.isspace():
            i = i[1:]
            for y in i:
                s += y
                l3.append(s)
    l3 = set(l3)
    l3 = list(l3)
    f = {}
    for i in state_df:
        n = 0
        c = 0
        for y in df['city']:
            try:
                if i == y:
                    if cuisines in df['cuisines'][n]:
                        c += 1
            except:
                pass
            f[i] = c
            n += 1
    state_x = list(f.keys())
    res_y = list(f.values())
    fig = helper.cuisines_wise_city(state_x,res_y)
    st.plotly_chart(fig)
    l_st = df['state'].sort_values().unique()
    l_state = st.selectbox("State",l_st)
    df1 = df[df.state == l_state]
    city_list = df1['city'].sort_values().unique()
    city = st.selectbox('Select City',city_list)
    state = list(df[df.city == city]['locality'])
    state = set(state)
    state = list(state)
    l = df['cuisines']
    l = list(l)
    l2 = []
    s = ''
    for i in l:
        try:
            w = i.split(',')
            for y in w:
                l2.append(y)
        except:
            pass
    l3 = []
    for i in l2:
        s = ''
        sp = i[0]
        if sp.isspace():
            i = i[1:]
            for y in i:
                s += y
                l3.append(s)
    l3 = set(l3)
    l3 = list(l3)
    f = {}
    for i in state:
        n = 0
        c = 0
        for y in df['locality']:
            try:
                if i == y:
                    if cuisines in df[df.city == city]['cuisines'][n]:
                        c += 1
            except:
                pass
            f[i] = c
            n += 1
    l_df = pd.DataFrame(f,index=[0]).T.reset_index()
    fig = helper.cuisines_wise_locality(l_df)
    st.plotly_chart(fig)


elif user_menu == 'Restaurants on Map':
    state_list=df['state'].sort_values().unique()
    state = st.selectbox('Select State',state_list)
    city_list = df[df.state==state]['city'].unique()
    city = st.selectbox('Select City',city_list)
    df4 = df[(df.state==state)&(df.city==city)]
    loc_list = df4['locality'].unique()
    locality = st.selectbox('Select Locality', loc_list)
    df4 = df4[df4.locality == locality]
    df5 = df4.reset_index(drop = True)
    loc_count = df[df.city == city]['locality'].value_counts()
    fig = helper.locality_count(loc_count)
    st.plotly_chart(fig)
    lat = [i for i in df5['latitude']]
    long = [j for j in df5['longitude']]
    map2 = helper.mul_rest(df5, lat, long)
    st.subheader('Restaurant in '+locality+' on basis of price range')
    st_folium(map2,width=800, height=550)
    st.subheader('Restaurant in '+locality+' on basis of Rating')
    map2 = helper.mul_rest_rating(df5, lat, long)
    st_folium(map2, width=800, height=550)
    l = []
    for i in df5['highlights']:
        i = i[1:-1]
        s = i.split(',')
        for y in s:
            high = ''
            for z in y:
                if z.isalpha() or z.isspace():
                    high += z
            high = high.lstrip()
            l.append(high)
    l1 = set(l)
    l1 = list(l1)
    l1.sort()
    l1 = l1[1:]
    h = st.selectbox('Select Highlight ',l1)
    fig = helper.highlights(df5, lat, long, h)
    st_folium(fig, width=800, height=550)
    st.subheader("Average Distance Between Reataurants")
    chart, d = helper.res_avg_distance(gp12)
    st.write('Click on Icon on map to see Restaurant Name and Distance')
    st_folium(chart, width=800)
    st.write("Average Distance : " + str(round(d, 2)) + ' Km')


elif user_menu == 'People Analysis':
    state_lst = df['state'].sort_values().unique()
    state = st.selectbox('Select State',state_lst)
    city_lst = df[df.state==state]
    city_lst = city_lst['city'].sort_values().unique()
    city = st.selectbox('Select City',city_lst)
    df2 = df[df.city == city]
    locality = df2['locality'].sort_values().unique()
    local = st.selectbox('Select Locality ',locality)
    df3= df[df.locality==local]
    veg, nveg = 0, 0
    for i in df2['highlights']:
        if 'Pure Veg' in i:
            veg += 1
        else:
            nveg += 1
    lveg,lnveg=0,0
    for i in df3['highlights']:
        if 'Pure Veg' in i:
            lveg += 1
        else:
            lnveg += 1
    fig = helper.veg_nveg(veg,nveg,lveg,lnveg)
    st.subheader('Veg vs Non-Veg in '+city)
    st.plotly_chart(fig)
    fig1 = helper.lveg(lveg,lnveg)
    st.subheader('Veg vs Non-Veg in ' + local)
    st.plotly_chart(fig1)
