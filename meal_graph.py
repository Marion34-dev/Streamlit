import databutton as db
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Welcome to the Vegetarian Meal Graph!")

data = {'Dish Name': ['Veggie Burger', 'Mushroom Risotto', 'Veggie Lasagne','Veggie Sushi'],
        'Popularity':  [17, 45, 30, 8],
        'Tastiness':   [9, 9, 7, 8]
       }

# Create a DataFrame (two dimensional tabular data structure) using the sample data
food = pd.DataFrame(data)

# Display the DataFrame
st.write(food)

# Create a matplotlib figure (top level container) and axis (subplot with data)
fig, ax = plt.subplots()

# Allow the user to select between 'Popularity' and 'Tastiness' for the Y-axis
y_selection = st.selectbox(label = "Pick Y", options=['Popularity', 'Tastiness'])

# Create a bar plot (graph repesentation) using seaborn with the selected Y-axis and display it on the matplotlib axis
sns.barplot(x='Dish Name', y=y_selection, data=food, ax=ax)

# Display the matplotlib figure
st.pyplot(fig)
