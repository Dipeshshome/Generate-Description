import streamlit as st
import pickle
import pandas as pd


from textcortex import TextCortex

# Create the hemingwai object and enter your API Key
hemingwai = TextCortex(api_key='gAAAAABkYhcY23IYYMuLuj2UhjoMrgj1_LiQCaRsYj1bvI2ka0WG94fMimNHhfIEDJXIHcRD5vPEYNfMkKjVcDsSS3zQOBqW6TdPN84evgRWTiqtDWtx5sw2XznliDT0Ewq3Ul_WYUOy')

product_name = st.text_input('Product Name')

product_category=st.text_input('Category Name' )

product_brand=st.text_input('Brand Name')

product_features=st.text_input('Feature Name')


# Generate Product Descriptions using Hemingwai

if st.button('Generate'):
    product_description = hemingwai.generate_product_descriptions(
                    product_name= product_name, product_category=product_category,
                    brand=product_brand, product_features=product_features,
                    source_language='en', token_count=500, temperature=0.7, n_gen=5)
    for i in range(0,5):
        if len(str(product_description[i]).split())>=50:
            st.write('Description:', product_description[i])
    
   # st.text_area('Description:', product_description)
   
