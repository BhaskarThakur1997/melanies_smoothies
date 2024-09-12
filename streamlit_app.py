# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


# Write directly to the app
st.title("My Parents New Healthy Dinner")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)


session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect( 
'Choose up to 5 ingredients:' 
,my_dataframe)

if ingredients_list:
    ingredients_string = ''
    
    for fruit_chosen in ingredients_list: 
        ingredients_string += fruit_chosen + ''

   # st.write(ingredients_string)
    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients) 
            values ('""" + ingredients_string + """')"""
    
    #st.write(my_insert_stmt)

    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

    cnx = st.connection("snowflake")
    session = cnx.session()  # Remove extra spaces


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon") 
#st.text(fruityvice_response.json())
fv_df st.dataframe(data=fruityvice_response.json(), use_container_width=True)
                    
