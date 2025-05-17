import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.io as pio
import os

# Optional: For PDF generation
from fpdf import FPDF

# Load data
df = pd.read_csv("Walmart.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Create output folder
os.makedirs("exports", exist_ok=True)

app = dash.Dash(__name__)
app.title = "Walmart Dashboard + Export"

app.layout = html.Div([
    html.H1("📈 Walmart Sales Dashboard with Export", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Store:"),
        dcc.Dropdown(
            id='store-dropdown',
            options=[{'label': f'Store {i}', 'value': i} for i in sorted(df['Store'].unique())],
            value=1
        ),
        html.Label("Holiday Filter:"),
        dcc.RadioItems(
            id='holiday-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'Holiday Only', 'value': 1},
                {'label': 'Non-Holiday Only', 'value': 0}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '10px'}
        ),
        html.Button("📸 Export Charts", id='export-btn'),
        html.Button("📄 Generate PDF Report", id='pdf-btn'),
        html.Div(id='export-message', style={'margin-top': '10px'})
    ], style={'padding': '10px 20px'}),

    dcc.Graph(id='sales-line'),
    html.Div([
        dcc.Graph(id='temp-fuel'),
        dcc.Graph(id='econ-factors')
    ], style={'display': 'flex'})
])

@app.callback(
    [Output('sales-line', 'figure'),
     Output('temp-fuel', 'figure'),
     Output('econ-factors', 'figure')],
    [Input('store-dropdown', 'value'),
     Input('holiday-filter', 'value')]
)
def update_charts(store, filter_value):
    dff = df[df['Store'] == store]
    if filter_value != 'all':
        dff = dff[dff['Holiday_Flag'] == int(filter_value)]

    fig1 = px.line(dff, x='Date', y='Weekly_Sales', title='Weekly Sales Over Time')
    fig2 = px.line(dff, x='Date', y=['Temperature', 'Fuel_Price'], title='Temperature & Fuel Price')
    fig3 = px.line(dff, x='Date', y=['CPI', 'Unemployment'], title='CPI and Unemployment')
    
    return fig1, fig2, fig3

@app.callback(
    Output('export-message', 'children'),
    Input('export-btn', 'n_clicks'),
    Input('pdf-btn', 'n_clicks'),
    Input('store-dropdown', 'value'),
    Input('holiday-filter', 'value'),
    prevent_initial_call='initial_duplicate'
)
def export_content(n_clicks_export, n_clicks_pdf, store, filter_value):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    dff = df[df['Store'] == store]
    if filter_value != 'all':
        dff = dff[dff['Holiday_Flag'] == int(filter_value)]

    fig1 = px.line(dff, x='Date', y='Weekly_Sales', title='Weekly Sales Over Time')
    fig2 = px.line(dff, x='Date', y=['Temperature', 'Fuel_Price'], title='Temperature & Fuel Price')
    fig3 = px.line(dff, x='Date', y=['CPI', 'Unemployment'], title='CPI and Unemployment')

    # Triggered by chart export
    if ctx.triggered[0]['prop_id'].startswith("export-btn"):
        fig1.write_image("exports/sales_line.png")
        fig2.write_image("exports/temp_fuel.png")
        fig3.write_image("exports/econ_factors.png")
        return "✅ Charts exported to 'exports/' folder."

    # Triggered by PDF generation
    elif ctx.triggered[0]['prop_id'].startswith("pdf-btn"):
        fig1.write_image("exports/temp_sales.png")
        fig2.write_image("exports/temp_tempfuel.png")
        fig3.write_image("exports/temp_econ.png")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Walmart Sales Report (Store {store})", ln=True, align='C')
        pdf.image("exports/temp_sales.png", w=170)
        pdf.ln(5)
        pdf.image("exports/temp_tempfuel.png", w=170)
        pdf.ln(5)
        pdf.image("exports/temp_econ.png", w=170)
        pdf.output("exports/Walmart_Report.pdf")
        return "📄 PDF Report saved in 'exports/' folder."

# Run app
if __name__ == '__main__':
    app.run(debug=True)
