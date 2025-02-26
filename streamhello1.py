import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import warnings
import datetime
from datetime import datetime
import io
import os

warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(page_title='PWT GPS Tracker Dashbaard', page_icon='', layout="wide")
# with open("style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
cwd = os.getcwd()
image_path = cwd+"//background2.jpg"

#path_imag = "C://Users//z021534//Downloads//stemlint//stemlint//background2.jpg"
path_imag= image_path
# image = Image.open(path)
# st.image(path_imag)
# Display title
st.title("RNTBCI PWT: GPS Data Tracker")

#PWT logo image

image_url = "https://your-image-url.com/your-image.jpg"

# File uploader widget for main file

import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
val = 0

# Load your image
#image_path = "background-image.jpg"  # Local image path
image_base64 = get_base64_image(path_imag)
# Slider for width control
#width = st.slider("Set File Uploader Width", min_value=100, max_value=800, value=400)
# Use the base64 string in the background image
st.markdown(
    f"""
    <style>
    
    .col-centered {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }}
    .col-bottom {{
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        height: 100%;
    }}
    
    .stApp {{
        background-image: url("data:image/jpeg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100%;
        width: 100%;
    }}
    /* Custom font style and size */
    h1 {{
        font-size: 50px;
        font-family: 'Arial', sans-serif;
        color: black;
    }}
    
    h2 {{
        font-size: 40px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: yellow;
    }}
    
    p {{
        font-size: 20px;
        font-family: 'Courier New', Courier, monospace;
        color: lightblue;
    }}
    
    /* Change Streamlit's button style */
    .stButton > button {{
        font-size: 18px;
        font-family: 'Times New Roman', Times, monospace;
        color: black;
        background-color: lightgreen;
        border-radius: 10px;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)

#serif
#%%

#import streamlit as st

# Path to your image (optional, for background image)
# image_path = "http://localhost:8501/logo3.jpg"  # Replace with your actual path or URL

# # Set the background image using markdown and inline CSS
# st.markdown(
#     f"""
#     <style>
   
    
#     /* Custom font style and size */
#     h1 {{
#         font-size: 50px;
#         font-family: 'Arial', sans-serif;
#         color: black;
#     }}
    
#     h2 {{
#         font-size: 40px;
#         font-family: 'Comic Sans MS', cursive, sans-serif;
#         color: yellow;
#     }}
    
#     p {{
#         font-size: 20px;
#         font-family: 'Courier New', Courier, monospace;
#         color: lightblue;
#     }}
    
#     /* Change Streamlit's button style */
#     .stButton > button {{
#         font-size: 18px;
#         font-family: 'Times New Roman', Times, serif;
#         color: black;
#         background-color: lightgreen;
#         border-radius: 10px;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#col1, col2, col3 = st.columns(3)

# Example content
#st.title("Streamlit App with Custom Font Style and Size")


def style_dataframe(df):
    return df.style \
        .applymap(lambda v: 'background-color: lightblue; color: black; font-size: 16px;' if isinstance(v, (int, float, str)) else '', subset=['Depatment', 'Ju', 'Depart_Meterie','Sum Actual ETP 209', 'Difference ETP 209', 'Expected Sum ETP 209']) \
        .set_table_styles([
            {'selector': 'thead th', 'props': [('background-color', 'green'), ('color', 'white'), ('font-size', '18px')]},
            {'selector': 'tbody td', 'props': [('font-size', '14px')]},
            {'selector': 'tr:nth-child(odd)', 'props': [('background-color', '#f2f2f2')]},
            {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#ffffff')]},
        ]) \
        .hide(axis="index")  # Optional: Hide index if you don’t want to show it.



# with  col1:

#st.write("Here is some paragraph text with custom font size and style.")
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    # with st.container():
    #     st.markdown('<div class="stFileUploader">', unsafe_allow_html=True)
    st.subheader("Please Upload the Global Data")
    fl = st.file_uploader("", type=["xlsx", "csv"])
    #df = pd.read_excel(fl, sheet_name="BDD", header=None)

    # Checking if the second row contains the expected column names
    #second_row = df.iloc[1].tolist()
    
        # st.markdown('</div>', unsafe_allow_html=True)
# Button to show custom button style
# if st.button('Click Me'):
#     st.write('Button was clicked!')
val = 0
test_final_dict = {}
global_df =pd.DataFrame()
if fl is not None:
    check_final_list = []
    check_final_list2 = []
    global_df = pd.read_excel(fl, sheet_name='BDD', header=None)
    second_row = global_df.iloc[1].tolist()
    global_df.columns = second_row
    global_df = global_df.drop([0, 1])
    # Create two columns
    #val = 0
    with col2:
        st.subheader("Please Select to Check the PWT GPS Data")
        #col4, col5 = st.columns(2)
        with st.container():
            st.markdown('<div class="col-centered">', unsafe_allow_html=True)
            # yes_button = st.button("Wants upload Template Data")
            # no_button = st.button("Wants Enter Data manually")
            genre = st.radio("",
                #"Do you have your Department template with filled data?",
                ["Wants upload Template Data", "Wants Enter Data manually"],
                # captions=[
                #     "Laugh out loud.",
                #     "Get the popcorn.",
                #     "Never stop learning.",
                # ],
            )
            st.markdown('</div>', unsafe_allow_html=True)
    with col3:
            
            # st.button("Button at Bottom")
            
        #template_file = None    
    # with col1:
        
    # if st.button('Wants upload Upload Template Data'):
    #     st.write('Button was clicked!')
        # if yes_button:
        #     val = 1
        
        st.subheader("Please Upload the Filled Template Data")
    # if genre == "Template Data Present":
        #template_file = st.file_uploader("", type=["xlsx", "csv"])
        month_checkboxes = {
            "Jan": '01-01-2025', "Feb": '01-02-2025', "Mar": '01-03-2025', "Apr": '01-04-2025',
            "May": '01-05-2025', "Jun": '01-06-2025', "Jul": '01-07-2025', "Aug": '01-08-2025',
            "Sep": '01-09-2025', "Oct": '01-10-2025', "Nov": '01-11-2025', "Dec": '01-12-2025'
        }
        #final_dict = {}
        
        
        if genre == "Wants upload Template Data":
            template_file = st.file_uploader("  ", type=["xlsx", "csv"])
            if template_file is not None:
                # try:
                    #global data
                    # Load the template file (single sheet)
                    template_df = pd.read_excel(template_file)
                    template_columns = template_df['DEPARTMENT'].tolist()
                    all_ju_list = template_df['JU'].tolist()
                    Req_metier_list = template_df['METIER'].tolist()
                    
                    #st.text(template_columns)
                    JU_unique = template_df['JU'].unique().tolist()
                    Month_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
                    ETP_Template_col = 'Expected WL in ETP209'
                    # for this_all_ju in all_ju_list:
                    #     this_ju_df = template_df['']
                    # ####################################
                    # for this_ju in all_ju_list:
                    #     ju_sum_list = []
                    #     count = 1
                    #     new_df = pd.DataFrame()
                    #     template_df_ju = template_df[template_df['JU'] == this_ju]
                    #     ju_filter_df_num = template_df_ju['Expected WL in ETP209'].tolist()
                    #     test_final_dict['Expected Sum ETP 209'] = template_df_ju[0]
                    #     depart_list = template_df_ju['DEPARTMENT'].tolist()
                    #     meterie_list = template_df_ju['METIER'].tolist()
                    #     for this_depart in depart_list:
                    #         test_final_dict["Depatment"]=this_depart
                    #         test_final_dict['Ju'] = this_ju
                    #         for meterie in meterie_list:
                    #             test_final_dict['METIER'] = meterie
                    #     #global_df_meterie = global_df[global_df['DMM']==this_meterie]
                    #     global_meterie_zone_df =global_df[global_df['Zone']=="RTI"]
                    #     global_meterie_zone_ju_df = global_meterie_zone_df[global_meterie_zone_df["Type d'activité ingénierie"]==this_ju]
                    #     mon_val_list =month_checkboxes.values()
                    #     for month_check in mon_val_list:
                    #         if len(global_meterie_zone_ju_df) > 0:
                    #             column_date = pd.to_datetime(month_check, format="%d-%m-%Y")
                    #             if column_date in global_meterie_zone_ju_df.columns:
                    #                 #st.write(column_date)
                    #                 new_df[month_check] = global_meterie_zone_ju_df[column_date].tolist()
                                    
                    #             else:
                    #                 #st.text(Depart)
                    #                 pass
                    #         else:
                    #             count = 0
                    #     if count ==1:
                    #         new_df["sum"+str(this_ju)] = new_df.sum(axis=1)
                    #         new_df["sum"+str(this_ju)] = new_df["sum"+str(this_ju)].div(209)
                    #         sum_val = new_df["sum"+str(this_ju)].sum()
                    #         ju_sum_list.append(sum_val)
                    #     else:
                    #         new_df["sum"+str(this_ju)] = 0
                    #         new_df["sum"+str(this_ju)] = 0
                    #         sum_val = 0
                    #         ju_sum_list.append(sum_val)
                            
                    #     test_final_dict['Sum Actual ETP 209'] = ju_sum_list[0]
                    #     #try_list_test.append(ju_sum_list[0])
                    #     st.write(test_final_dict['Expected Sum ETP 209'])
                    #     st.write(test_final_dict['Sum Actual ETP 209'])
                    #     test_final_dict['Difference ETP 209'] = test_final_dict['Expected Sum ETP 209'] - test_final_dict['Sum Actual ETP 209']
                    #     check_final_list.append(test_final_dict)
                    
                    # ####################################
                    
                    
                    
                    
                    for Depart in template_columns:
                        final_dict = {}
                        
                        ju_sum_list = []
                        try_list_test = []
                        final_dict["Depatment"]=Depart
                        try_list_test.append(Depart)
                        filtered_template_df =template_df[template_df['DEPARTMENT']==Depart]
                        depart_meterie = filtered_template_df['METIER'].tolist()
                        depart_meterie_unique = filtered_template_df['METIER'].unique().tolist()
                        
                        #final_dict['Depart_Meterie'] = depart_meterie
                        #st.write(depart_meterie)
                        
                        depart_ju  = filtered_template_df['JU'].tolist()
                        if all(x == depart_meterie[0] for x in depart_meterie):
                            for this_meterie in depart_meterie_unique:
                                final_dict['Depart_Meterie'] = this_meterie
                                try_list_test.append(this_meterie)
                                global_df_meterie = global_df[global_df['DMM']==this_meterie]
                                global_meterie_zone_df =global_df_meterie[global_df_meterie['Zone']=="RTI"]
                                this_meterie_df = filtered_template_df[filtered_template_df['METIER'] == this_meterie]
                                this_meterie_ju_list = this_meterie_df['JU'].tolist()
                                #st.write(this_meterie_ju_list)
                                #final_dict['Ju'] = this_meterie_ju_list[0]
                                
                            for this_ju in this_meterie_ju_list:
                                count = 1
                                final_dict['Ju'] = this_ju
                                #st.write(this_ju)
                                try_list_test.append(this_ju)
                                new_df = pd.DataFrame()
                                ju_filter_df = this_meterie_df[this_meterie_df['JU']==this_ju]
                                ju_filter_df_num = ju_filter_df['Expected WL in ETP209'].tolist()
                                final_dict['Expected Sum ETP 209'] = ju_filter_df_num[0]
                                try_list_test.append(ju_filter_df_num[0])
                                mon_val_list =month_checkboxes.values()
                                global_meterie_zone_ju_df = global_meterie_zone_df[global_meterie_zone_df["Type d'activité ingénierie"]==this_ju]
                                # global_meterie_zone_df = global_meterie_zone_df.columns()
                                for month_check in mon_val_list:
                                    if len(global_meterie_zone_ju_df) > 0:
                                        column_date = pd.to_datetime(month_check, format="%d-%m-%Y")
                                        if column_date in global_meterie_zone_ju_df.columns:
                                            #st.write(column_date)
                                            new_df[month_check] = global_meterie_zone_ju_df[column_date].tolist()
                                            
                                        else:
                                            #st.text(Depart)
                                            pass
                                    else:
                                        count = 0
                            if count ==1:
                                new_df["sum"+str(this_ju)] = new_df.sum(axis=1)
                                new_df["sum"+str(this_ju)] = new_df["sum"+str(this_ju)].div(209)
                                sum_val = new_df["sum"+str(this_ju)].sum()
                                ju_sum_list.append(sum_val)
                            else:
                                new_df["sum"+str(this_ju)] = 0
                                new_df["sum"+str(this_ju)] = 0
                                sum_val = 0
                                ju_sum_list.append(sum_val)
                            #print("All strings are the same")
                        else:
                            #print("Not all strings are the same")
                            for this_meterie in depart_meterie:
                                final_dict['Depart_Meterie'] = this_meterie
                                try_list_test.append(this_meterie)
                                global_df_meterie = global_df[global_df['DMM']==this_meterie]
                                global_meterie_zone_df =global_df_meterie[global_df_meterie['Zone']=="RTI"]
                                this_meterie_df = filtered_template_df[filtered_template_df['METIER'] == this_meterie]
                                this_meterie_ju_list = this_meterie_df['JU'].tolist()
                                #st.write(this_meterie_ju_list)
                                #final_dict['Ju'] = this_meterie_ju_list[0]
                                
                                for this_ju in this_meterie_ju_list:
                                    count = 1
                                    final_dict['Ju'] = this_ju
                                    try_list_test.append(this_ju)
                                    new_df = pd.DataFrame()
                                    ju_filter_df = this_meterie_df[this_meterie_df['JU']==this_ju]
                                    ju_filter_df_num = ju_filter_df['Expected WL in ETP209'].tolist()
                                    final_dict['Expected Sum ETP 209'] = ju_filter_df_num[0]
                                    try_list_test.append(ju_filter_df_num[0])
                                    mon_val_list =month_checkboxes.values()
                                    global_meterie_zone_ju_df = global_meterie_zone_df[global_meterie_zone_df["Type d'activité ingénierie"]==this_ju]
                                    # global_meterie_zone_df = global_meterie_zone_df.columns()
                                    for month_check in mon_val_list:
                                        if len(global_meterie_zone_ju_df) > 0:
                                            column_date = pd.to_datetime(month_check, format="%d-%m-%Y")
                                            if column_date in global_meterie_zone_ju_df.columns:
                                                #st.write(column_date)
                                                new_df[month_check] = global_meterie_zone_ju_df[column_date].tolist()
                                                
                                            else:
                                                #st.text(Depart)
                                                pass
                                        else:
                                            count = 0
                                if count ==1:
                                    new_df["sum"+str(this_ju)] = new_df.sum(axis=1)
                                    new_df["sum"+str(this_ju)] = new_df["sum"+str(this_ju)].div(209)
                                    sum_val = new_df["sum"+str(this_ju)].sum()
                                    ju_sum_list.append(sum_val)
                                else:
                                    new_df["sum"+str(this_ju)] = 0
                                    new_df["sum"+str(this_ju)] = 0
                                    sum_val = 0
                                    ju_sum_list.append(sum_val)
                                
                        #st.text(this_ju)
                        #final_dict["Depatment"]=Depart
                        
                        
                        final_dict['Sum Actual ETP 209'] = ju_sum_list[0]
                        try_list_test.append(ju_sum_list[0])
                        #st.write(final_dict['Expected Sum ETP 209'])
                        #st.write(final_dict['Sum Actual ETP 209'])
                        final_dict['Difference ETP 209'] = final_dict['Expected Sum ETP 209'] - final_dict['Sum Actual ETP 209']
                        try_list_test.append(final_dict['Difference ETP 209'])
                        check_final_list.append(final_dict)
                        check_final_list2.append(try_list_test)
                        
                        
                        
                        
                       # Depart = new_df.copy()
                        
                                #expected_val = ju_filter_df[0]
    # Apply styling
    try:
        if (check_final_list) > 0:
            test_df =pd.DataFrame(check_final_list)
            styled_df = style_dataframe(test_df)
            st.dataframe(styled_df)
            # test_xx_df =pd.DataFrame(try_list_test)
            # st.dataframe(test_xx_df)
            
            #st.text(styled_df)
    except:
        if len(check_final_list) > 0:
            test_df =pd.DataFrame(check_final_list)
            styled_df = style_dataframe(test_df)
            
            st.dataframe(styled_df)
            # test_xx_df =pd.DataFrame(try_list_test)
            # st.dataframe(test_xx_df)
            pass
        else:
            st.text("Load Template Data... Please wait......")
        
                            
                    
                    
                # else:
                #     filtered_template_df = pd.DataFrame()
                #     st.write("Provided Department template file not having selected department name, please check the Department template")
                # except:
                #     st.write("Error present in template, please update the template file and upload it again")
        #pass
    # else:
    #     Department_List_name = ['CPCT - Cust Perf - DEA - M', "ISIT - PLM DEA - M", "PWT CAE", "PWT CALI & PERF", "PWT DESIGN",  "PWT EMB ALGO", "PWT EMB SWI", "PWT PROJ", "VP OFFICE"]
        #Depart = st.sidebar.selectbox("Pick Department",  options=[None] + Department_List_name)

        # If a department is selected, show file uploader for the template file
        # if genre == "Template Data Present":
        #     pass
        


#%%%
# import pandas as pd
# import streamlit as st

# # Sample data
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'Score': [80, 90, 85, 95]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# Custom styling function
# def style_dataframe(df):
#     return df.style \
#         .applymap(lambda v: 'background-color: lightblue; color: black; font-size: 16px;' if isinstance(v, (int, float)) else '', subset=['Score', 'Age']) \
#         .set_table_styles([
#             {'selector': 'thead th', 'props': [('background-color', 'green'), ('color', 'white'), ('font-size', '18px')]},
#             {'selector': 'tbody td', 'props': [('font-size', '14px')]},
#             {'selector': 'tr:nth-child(odd)', 'props': [('background-color', '#f2f2f2')]},
#             {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#ffffff')]},
#         ]) \
#         .hide(axis="index")  # Optional: Hide index if you don’t want to show it.

# # Apply styling
# styled_df = style_dataframe(df)

# # Display styled dataframe in Streamlit
# st.dataframe(styled_df)
         
    
    
    
