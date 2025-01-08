# Fondation-Follereau-Dashboard

## Introduction
This is a **Streamlit-based interactive dashboard** for the [Fondation Follereau](https://ffl.lu/en/), an NGO that targets the needs of vulnerable African populations (especially in the **healthcare** sector).
The inspiration for this project was taken from a challenge proposed in 2021 by the organization [Viz for Social Good](https://www.vizforsocialgood.com/), and is my submission for the Health Data Visualization subject of my Master's degree MHEDAS.

The dashboard features insightful visualizations such as treemap, choropleth map, pie chart, and bar chart to help readers understand how the Foundation's 2018 budget was used and what results were accomplished.

The ultimate goal of this Dashboard is to raise awareness on the amazing projects from the Foundation and convey an important message to the general public through the power of data visualization. 


## File structure of the repository

```plaintext
Fondation-Follereau-Dashboard/
│
├── app.py                     # Main application file
├── requirements.txt           # List of dependencies needed to run the app
├── Vizforsocialgood.xlsx      # Dataset used for the dashboard
├── vis3.png                   # Logo for the sidebar
├── cover.jpg                  # Cover image for the homepage
└── README.md                  # Project documentation

```

## Installation and set-up
If you want to run this python app in your local computer, please follow these steps:

1. Clone this repository and open it in your code editor of preference (I personally used Pycharm for developing the Dashboard)
2. Create a virtual environment (Not mandatory, but highly recommended)
3. Install the required dependencies to run the app with the command: _pip install -r requirements.txt_
4. Ensure that the Excel files and the Image files on top of the app.py point to your root directory (It may be something like this for example: _C:/Users/Name/PycharmProjects/PythonProject/Vizforsocialgood.xlsx_)
5. Run the app in the code editor terminal with the command: _streamlit run app.py_
6. Open the app following the provided local host link (Likely http://localhost:8501)


## How the Dashboard works
The dashboard has three main sections that are accessible via the navigation sidebar:

- **Meet us**:  Introduction to the Fondation Follereau and its mission.
- **Our impact**: Interactive visualizations highlighting budget allocations and achievements across Africa. This consists of a treemap and a choropleth maps.
- **Call to Action**: It uses a pie chart and a bar chart to represent the intervention areas of the Foundation and the direct beneficiaries of the budget. It also encourages users to support the work of the Foundation.


## Deployment
The Dashboard app was deployed in a straightforward way thanks to Streamlit Cloud.

Please follow this public URL link to access and interact with the dashboard:

https://fondation-follereau-dashboard-hdvc.streamlit.app/


**Note**: If the app has been inactive for many days, streamlit may have frozen it. In this situation, the user may need to "reactive it" by clicking on the button from the screen and then wait for a few seconds until the app is active again.


![image](https://github.com/user-attachments/assets/f5ca007c-077c-4db5-8ea7-071b18917200)


