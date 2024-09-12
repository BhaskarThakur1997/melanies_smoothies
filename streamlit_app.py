import streamlit as st
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
import requests

# Snowflake connection parameters
connection_parameters = {
    "account": "PNUBUJU.MMB26698",
    "user": "thakurbhaskar",
    "password": "Skrillex1@",
    "role": "SYSADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "SMOOTHIES",
    "schema": "PUBLIC"
}

# Create Snowflake session
session = Session.builder.configs(connection_parameters).create()

# Streamlit app setup
st.title("Example Streamlit App :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

# Fetch data from Snowflake
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME')).to_pandas()

# Streamlit widget for selecting ingredients
ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe['FRUIT_NAME'].tolist()
)

# Handle ingredient selection
if ingredients_list:
    ingredients_string = ', '.join(ingredients_list)
    st.write("Selected ingredients: ", ingredients_string)
    
    # Prepare SQL statement (ensure `name_on_order` is defined somewhere)
    name_on_order = "example_order_name"  # You need to set this variable appropriately
    my_insert_stmt = f"""INSERT INTO smoothies.public.orders (ingredients, name_on_order) 
                         VALUES ('{ingredients_string}', '{name_on_order}')"""
    
    st.write("SQL Insert Statement: ", my_insert_stmt)
    
    # Uncomment if you want to execute the statement
    # session.sql(my_insert_stmt).collect()
    
    # Fetch and display nutrition information for each selected fruit
    for fruit_chosen in ingredients_list:
        st.subheader(fruit_chosen + ' Nutrition Information')
        response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_chosen}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.write("Nutrition information not available.")

# Optional: Example data setup (remove if not needed)
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
ingredients_list = st.multiselect(
    'Choose up to 5 ingredients (example):',
    fruits
)

if ingredients_list:
    ingredients_string = ', '.join(ingredients_list)
    st.write("Selected example ingredients: ", ingredients_string)

    for fruit_chosen in ingredients_list:
        st.subheader(fruit_chosen + ' Nutrition Information')
        fruit_data = requests.get(f"https://fruityvice.com/api/fruit/{fruit_chosen}").json()
        st.json(fruit_data)
