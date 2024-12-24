import streamlit as st
import pandas as pd
import plotly.express as px

#### File and images path
file_path = "C:/Users/IhonaCorrea/PycharmProjects/PythonProject/Vizforsocialgood.xlsx"
logo_path = "C:/Users/IhonaCorrea/PycharmProjects/PythonProject/vis3.png"
image_path = "C:/Users/IhonaCorrea/PycharmProjects/PythonProject/cover.jpg"

# Consistent color palette for all visualizations
custom_color_scale = px.colors.sequential.Viridis

#### Load and preprocess data
df = pd.read_excel(file_path, engine="openpyxl", sheet_name="2018", header=None)
df = df.transpose()
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

df = pd.melt(
    df,
    id_vars=[
        "Country",
        "Local partner",
        "Project title",
        "Axis of intervention",
        "Direct beneficiaries",
        "Indirect beneficiaries",
        "Region",
        "Voted 2018 project budget €",
        "Project share % out of all budget",
        "Voted 2018 country budget €",
        "Country share % out of all budget",
        "Type de financement (tel que présenté dans l'Accord-Cadre 2016-2020)",
        "iso_alpha",
    ],
    value_vars=[
        "2018 results",
        "2018 results2",
        "2018 results3",
        "2018 results4",
        "2018 results5",
    ],
    var_name="results",
    value_name="notes",
)


#### Customize navigation bar
st.sidebar.image(logo_path, width=130)
st.sidebar.markdown("---")

st.sidebar.subheader("Navigation bar")
page = st.sidebar.radio("Go to:", ["Meet us", "Our impact", "Call to Action"])

st.sidebar.markdown("---")
st.sidebar.write("### Connect with the designer:")
st.sidebar.markdown(
    """
    [![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IhonaMaria)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ihona-maria-correa-de-cabo-051431160/)
    """,
    unsafe_allow_html=True,
) # Add clickable GitHub and LinkedIn logos


#### Page 1: Introduction
if page == "Meet us":
    st.title("Welcome to the Fondation Follereau's Dashboard")
    st.markdown(
        """
        ### 🌍 Empowering Lives in Africa  
        
        At Fondation Follereau, we transform challenges into opportunities.
        From **healthcare** to **education**, this foundation strives to meet the needs of vulnerable African populations.
        
        Our goal? To end with:
                
        - 🧒 High child mortality rates
        - 🏥 Limited access to healthcare facilities
        - 🦟 Prevalence of diseases
        - 📚 Insufficient educational opportunities

        Together, we can make a difference.
          
        Explore the dashboard to learn about our **impact** and how you can **contribute**.
        """,
        unsafe_allow_html=True,
    )
    st.image(image_path, width=500)


#### Page 2: Visualizations
elif page == "Our impact":
    st.title("💡 See Our Impact at a Glance")
    st.subheader("Budget Allocation Across Africa")

    # Short description of the plots
    st.markdown(
        """
        This page shows how the Fondation uses its **resources** to create a positive impact in Africa.
        
        - The treemap shows how the budget is divided among the different countries, regions, and project focus areas (like healthcare or education). 
        It gives a clear picture of how we prioritize the resources to make the biggest impact possible.
        
        - The map highlights the budget percentage allocated to each country, showing in proportion how much we are currently investing in each.
        
        - Want to learn more? Use the **dropdown** below to focus on a specific country and discover the amazing **achievements** we have accomplished there 👇
        """,
        unsafe_allow_html=True,
    )

    # Sidebar filter
    selected_country = st.selectbox(
        "Select a Country", ["All"] + df["Country"].unique().tolist()
    )

    # Filter data when user selects a country
    filtered_df = df if selected_country == "All" else df[df["Country"] == selected_country]

    ## Create a treemap
    treemap_fig = px.treemap(
        filtered_df,
        path=["Country", "Axis of intervention", "Region"],
        color="Country share % out of all budget",
        values="Voted 2018 project budget €",
        height=600,
        width=1000,
        color_continuous_scale=custom_color_scale,
        range_color=(0, filtered_df["Country share % out of all budget"].max()),
    ).update_layout(margin=dict(t=25, r=0, l=5, b=20))


    ## Create a choropleth

    # First ensure the column is numeric before the choropleth
    filtered_df["Country share % out of all budget"] = pd.to_numeric(
        filtered_df["Country share % out of all budget"], errors="coerce"
    ).fillna(0)

    choropleth_fig = px.choropleth(
        filtered_df,
        locations="iso_alpha",
        hover_name="Country",
        color="Country share % out of all budget",
        scope="africa",  # Focus on the Africa region
        projection="natural earth",  # Map projection
        color_continuous_scale=custom_color_scale,
        range_color=(0, df["Country share % out of all budget"].max()),  # color range
    ).update_layout(
        margin=dict(t=25, r=0, l=5, b=20)
    )

    # Display treemap
    st.plotly_chart(treemap_fig)

    # Display choropleth
    st.plotly_chart(choropleth_fig)

    ## Combine all notes (results) into a single text box
    if selected_country != "All":
        st.subheader(f"🏆Achievements in {selected_country}")

        # Extract unique notes for the selected country
        country_notes = filtered_df["notes"].dropna().unique()

        # Combine all notes
        combined_notes = "\n\n".join([f"✓ {note}" for note in country_notes])

        # Display text box
        st.text_area(
            f"",
            combined_notes,
            height=200,
        )


#### Page 3: Call to Action
elif page == "Call to Action":
    st.title("✨ Be the Change Africa Needs")
    st.subheader("See in what areas your donation can help")

    ## Create a pie chart for the budget proportion
    budget_by_axis = df.groupby("Axis of intervention")["Voted 2018 project budget €"].sum().reset_index()   # Aggregate budget by axis of intervention

    total_budget = budget_by_axis["Voted 2018 project budget €"].sum()
    budget_by_axis["Proportion (%)"] = (budget_by_axis["Voted 2018 project budget €"] / total_budget) * 100  # Calculate the proportion of the budget for each axis

    pie_fig = px.pie(
        budget_by_axis,
        names="Axis of intervention",
        values="Voted 2018 project budget €",
        #title="Proportion of Budget Allocation by Axis of Intervention (2018)",
        color_discrete_sequence=custom_color_scale,
        labels={"Voted 2018 project budget €": "Budget (€)"},
        hole=0.4,  # Donut chart
    )

    # Display the pie chart with a description
    st.markdown(
        """
        Every donation has a **purpose**.
        This chart shows how the contributions are typically divided among different areas of intervention.
        """,
        unsafe_allow_html=True,
    )
    #pie_fig.update_layout(title="Proportion of Budget Allocation by Axis of Intervention")
    st.plotly_chart(pie_fig)

    ## Create the bar chart
    # Filter out rows where the budget is zero
    beneficiary_budget = (
        df.groupby("Direct beneficiaries")["Voted 2018 project budget €"]
        .sum()
        .reset_index()
        .query("`Voted 2018 project budget €` > 0")  # Keep only rows with a budget > 0
        .sort_values(by="Voted 2018 project budget €", ascending=True)
    )

    # Create a horizontal bar chart with a uniform color
    bar_chart = px.bar(
        beneficiary_budget,
        x="Voted 2018 project budget €",
        y="Direct beneficiaries",
        orientation="h",  # Horizontal bar chart
        #title="Total Budget Allocation by Beneficiary Group",
        labels={
            "Voted 2018 project budget €": "Total Budget (€)",
            "Direct beneficiaries": "Beneficiary Group",
        },
    )

    bar_chart.update_traces(marker_color="rgb(68,1,84)")  # Apply a uniform color to all bars

    bar_chart.update_layout(
        xaxis=dict(title="Total Budget (€)"),
        yaxis=dict(title="Beneficiary Group"),
        margin=dict(t=50, r=25, l=25, b=50),
        height=600,
    )

    # Display the bar chart with a short description
    st.subheader("Meet the Lives You’ll Change")
    st.markdown(
        """
        Behind every number is a **story**.
        This chart highlights the groups that are directly benefited from our initiatives and how much of the budget goes towards helping them.
        """,
        unsafe_allow_html=True,
    )
    st.plotly_chart(bar_chart, use_container_width=True)

    ## Add donation links
    st.subheader("Make a lasting impact today:")
    st.write(
        """
        Every action counts. By donating, volunteering, or sharing, you are supporting us to make these projects a reality.

        - [💖Donate Now](https://ffl.lu/en/)
        - [📚Learn More About Viz For Social Good](https://www.vizforsocialgood.com/)
        """
    )




