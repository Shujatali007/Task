# Import necessary libraries
from dash import Dash, dcc, html, Input, Output  # Dash framework components
import pandas as pd  # Data manipulation
import plotly.express as px  # Interactive visualization

# Read the dataset
df = pd.read_csv('E:\Case Study - DataOps Algo-trading\west_europe_electricity_data.csv')

# Create the Dash application
app = Dash(__name__)

# Create the layout of the dashboard
app.layout = html.Div(children=[
    html.H1('Commodity Price Dashboard'),  # Title of the dashboard
    html.Div(children='''
        Interactive visualizations of commodity price data.
    '''),  # Description of the dashboard
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value=df['country'].unique()[0]
    ),  # Dropdown menu to select a country
    dcc.Graph(id='demand-graph'),  # Placeholder for demand graph
    dcc.Graph(id='supply-graph'),  # Placeholder for supply graph
    dcc.Graph(id='price-graph')  # Placeholder for price graph
])

# Define the callbacks
@app.callback(
    Output('demand-graph', 'figure'),  # Output for demand graph
    Output('supply-graph', 'figure'),  # Output for supply graph
    Output('price-graph', 'figure'),  # Output for price graph
    [Input('country-dropdown', 'value')]  # Input from the country dropdown
)
def update_graphs(country):
    filtered_df = df[df['country'] == country]  # Filter the DataFrame based on the selected country
    
    # Create line plots for demand, supply, and price using the filtered DataFrame
    demand_fig = px.line(filtered_df, x='date', y='demand', title='Demand')
    supply_fig = px.line(filtered_df, x='date', y='supply', title='Supply')
    price_fig = px.line(filtered_df, x='date', y='price', title='Price')
    
    return demand_fig, supply_fig, price_fig  # Return the line plots as output

# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)
