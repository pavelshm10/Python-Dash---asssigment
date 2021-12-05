import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv(r"D:\Dev\Dash Assignment - Files\Pricing Data.csv")
app = dash.Dash()

def create_grouped_df(df_in, group_column_name, target_column, aggregate_type):
    print(target_column)
    return df_in.groupby(target_column).agg({group_column_name: aggregate_type}) \
        .rename(columns={group_column_name: group_column_name}).reset_index()


boxplot_layout = (
    dbc.Container(
        [
            html.Div(
                children=[
                    html.H1("Segmented Portfolio Analysis",
                            style={'font-size': 36}
                            ),
                ],

            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        html.Div(
                                                            dbc.Row(
                                                                [
                                                                    dbc.Col([
                                                                        dcc.Dropdown(
                                                                            id="aggregate-dropdown",
                                                                            options=[
                                                                                {
                                                                                    "label": "Total",
                                                                                    "value": "sum",
                                                                                },
                                                                                {
                                                                                    "label": "Average",
                                                                                    "value": "mean",
                                                                                },
                                                                            ],
                                                                            value="sum",
                                                                        ),
                                                                    ],
                                                                        className='drop-down',
                                                                    ),
                                                                    dbc.Col(
                                                                        [
                                                                            html.Label(
                                                                                "of",
                                                                            )
                                                                        ],
                                                                        className='drop-down',
                                                                    ),
                                                                    dbc.Col([
                                                                        dcc.Dropdown(
                                                                            options=[
                                                                                {
                                                                                    'label': 'Age',
                                                                                    'value': 'Age', },
                                                                                {
                                                                                    'label': 'Tenure',
                                                                                    'value': 'Tenure', },
                                                                                {
                                                                                    'label': 'Annual Miles',
                                                                                    'value': 'Annual Miles', },
                                                                                {
                                                                                    'label': 'Car Age',
                                                                                    'value': 'Car Age', },
                                                                                {
                                                                                    'label': 'Car Group',
                                                                                    'value': 'Car Group', },
                                                                                {
                                                                                    'label': 'Car Value',
                                                                                    'value': 'Car Value', },
                                                                                {
                                                                                    'label': 'Car Weight',
                                                                                    'value': 'Car Weight', },
                                                                                {
                                                                                    'label': 'Fuel Type',
                                                                                    'value': 'Fuel Type', },
                                                                                {
                                                                                    'label': 'Gender',
                                                                                    'value': 'Gender', },
                                                                                {
                                                                                    'label': 'Installments',
                                                                                    'value': 'Installments', },
                                                                                {
                                                                                    'label': 'Marital Status',
                                                                                    'value': 'Marital Status', },
                                                                                {
                                                                                    'label': 'Regional Mlass',
                                                                                    'value': 'Regional Mlass', },
                                                                                {
                                                                                    'label': 'Risk Class',
                                                                                    'value': 'Risk Class', },
                                                                                {
                                                                                    'label': 'Year',
                                                                                    'value': 'Year', },
                                                                                {
                                                                                    'label': 'Variable Cost',
                                                                                    'value': 'Variable Cost', },
                                                                                {
                                                                                    'label': 'Premium',
                                                                                    'value': 'Premium', },
                                                                                {
                                                                                    'label': 'Previous Premium',
                                                                                    'value': 'Previous Premium', },
                                                                                {
                                                                                    'label': 'Margin Parameter',
                                                                                    'value': 'Margin Parameter', },
                                                                                {
                                                                                    'label': 'Renewal Demand',
                                                                                    'value': 'Renewal Demand', },
                                                                                {
                                                                                    'label': 'Core Earnings',
                                                                                    'value': 'Core Earnings', },
                                                                                {
                                                                                    'label': 'Actuarial Cost Parameter',
                                                                                    'value': 'Actuarial Cost Parameter', },
                                                                                {
                                                                                    'label': 'Base Premium',
                                                                                    'value': 'Base Premium', },
                                                                                {
                                                                                    'label': 'Tax',
                                                                                    'value': 'Tax', },
                                                                                {
                                                                                    'label': 'Individual Discount',
                                                                                    'value': 'Individual Discount', },
                                                                            ],
                                                                            id="y-axis-dropdown",
                                                                            value='Age',
                                                                        ),
                                                                    ],
                                                                        className='drop-down',
                                                                    ),
                                                                    dbc.Col(
                                                                        [
                                                                            html.Label(
                                                                                "by",
                                                                            )
                                                                        ],
                                                                        className='drop-down',
                                                                    ),
                                                                    dbc.Col(
                                                                        [
                                                                            dcc.Dropdown(
                                                                                options=[
                                                                                    {
                                                                                        'label': 'Age',
                                                                                        'value': 'Age', },
                                                                                    {
                                                                                        'label': 'Tenure',
                                                                                        'value': 'Tenure', },
                                                                                    {
                                                                                        'label': 'Annual Miles',
                                                                                        'value': 'Annual Miles', },
                                                                                    {
                                                                                        'label': 'Car Age',
                                                                                        'value': 'Car Age', },
                                                                                    {
                                                                                        'label': 'Car Group',
                                                                                        'value': 'Car Group', },
                                                                                    {
                                                                                        'label': 'Car Value',
                                                                                        'value': 'Car Value', },
                                                                                    {
                                                                                        'label': 'Car Weight',
                                                                                        'value': 'Car Weight', },
                                                                                    {
                                                                                        'label': 'Fuel Type',
                                                                                        'value': 'Fuel Type', },
                                                                                    {
                                                                                        'label': 'Gender',
                                                                                        'value': 'Gender', },
                                                                                    {
                                                                                        'label': 'Installments',
                                                                                        'value': 'Installments', },
                                                                                    {
                                                                                        'label': 'Marital Status',
                                                                                        'value': 'Marital Status', },
                                                                                    {
                                                                                        'label': 'Regional Mlass',
                                                                                        'value': 'Regional Mlass', },
                                                                                    {
                                                                                        'label': 'Risk Class',
                                                                                        'value': 'Risk Class', },
                                                                                    {
                                                                                        'label': 'Year',
                                                                                        'value': 'Year', },
                                                                                    {
                                                                                        'label': 'Variable Cost',
                                                                                        'value': 'Variable Cost', },
                                                                                    {
                                                                                        'label': 'Premium',
                                                                                        'value': 'Premium', },
                                                                                    {
                                                                                        'label': 'Previous Premium',
                                                                                        'value': 'Previous Premium', },
                                                                                    {
                                                                                        'label': 'Margin Parameter',
                                                                                        'value': 'Margin Parameter', },
                                                                                    {
                                                                                        'label': 'Renewal Demand',
                                                                                        'value': 'Renewal Demand', },
                                                                                    {
                                                                                        'label': 'Core Earnings',
                                                                                        'value': 'Core Earnings', },
                                                                                    {
                                                                                        'label': 'Actuarial Cost Parameter',
                                                                                        'value': 'Actuarial Cost Parameter', },
                                                                                    {
                                                                                        'label': 'Base Premium',
                                                                                        'value': 'Base Premium', },
                                                                                    {
                                                                                        'label': 'Tax',
                                                                                        'value': 'Tax', },
                                                                                    {
                                                                                        'label': 'Individual Discount',
                                                                                        'value': 'Individual Discount', },
                                                                                ],
                                                                                id="x-axis-dropdown",
                                                                                value='Tenure',
                                                                            )
                                                                        ],
                                                                        className='drop-down',
                                                                    ),
                                                                ],
                                                                className='header'
                                                            )
                                                        )
                                                    )
                                                ]
                                            ),
                                            html.Div(
                                                dcc.Graph(id="graph-figure"),
                                                className='graph'
                                            ),
                                        ]
                                    )
                                ],
                                inverse=True,
                            )
                        ]
                    )
                ])
        ]
    ))

app.layout = boxplot_layout


@app.callback(
    Output("graph-figure", "figure"),
    Input("aggregate-dropdown", "value"),
    Input("x-axis-dropdown", "value"),
    Input("y-axis-dropdown", "value"),
)
def update_graph(aggregate_type, x_axis, y_axis):
    aggregate_data = create_grouped_df(df, y_axis, x_axis, aggregate_type)
    print(df[x_axis].dtype)
    if df[x_axis].dtype == 'int64':
        graph = px.scatter(aggregate_data, x=x_axis, y=y_axis)
    elif df[x_axis].dtype == 'object':
        graph = px.bar(aggregate_data, x=x_axis, y=y_axis)
    elif df[x_axis].dtype == 'float64':
        graph = px.scatter(aggregate_data, x=x_axis, y=y_axis)
    return graph


if __name__ == "__main__":
    app.run_server(debug=True)
