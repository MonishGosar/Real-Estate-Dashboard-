import streamlit as st
from streamlit_elements import elements, dashboard, mui, nivo
from database_operations import get_tenant_sector_data, get_qoq_leasing_data

# Set page config

# Sidebar
with st.sidebar:
    st.title("REjournal")
    st.write("Dashboard controls can be added here.")

# Main content
st.title("Real Estate Leasing Analytics")

# Create a frame to display elements
with elements("dashboard"):
    # Define layout
    layout = [
        dashboard.Item("tenant_sector_chart", 0, 0, 6, 4),
        dashboard.Item("qoq_trend_chart", 6, 0, 6, 4),
    ]
    
    # Create dashboard grid
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        # Tenant Sector Share Chart
        with mui.Card(key="tenant_sector_chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(
                title="Tenant Sector Share in Leasing",
                className="draggable",
                sx={
                    "textAlign": "center",
                    "backgroundColor": "#f0f0f0",
                    "& .MuiCardHeader-title": {
                        "fontSize": "1.25rem",
                        "fontWeight": "bold",
                    },
                }
            )
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                tenant_sector_data = get_tenant_sector_data()
                if tenant_sector_data:
                    nivo.Pie(
                        data=tenant_sector_data,
                        margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        activeOuterRadiusOffset=8,
                        borderWidth=1,
                        borderColor={"from": "color", "modifiers": [["darker", 0.2]]},
                        arcLinkLabelsSkipAngle=10,
                        arcLinkLabelsTextColor="#333333",
                        arcLinkLabelsThickness=2,
                        arcLinkLabelsColor={"from": "color"},
                        arcLabelsSkipAngle=10,
                        arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                        legends=[
                            {
                                "anchor": "right",
                                "direction": "column",
                                "justify": False,
                                "translateX": 0,
                                "translateY": 0,
                                "itemsSpacing": 0,
                                "itemWidth": 100,
                                "itemHeight": 18,
                                "itemTextColor": "#999",
                                "itemDirection": "left-to-right",
                                "itemOpacity": 1,
                                "symbolSize": 18,
                                "symbolShape": "circle",
                            }
                        ]
                    )
                else:
                    mui.Typography("No data available for the tenant sector chart.")

        # Q-o-Q Trend Chart
        with mui.Card(key="qoq_trend_chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(
                title="Q-o-Q Trend in Leasing",
                className="draggable",
                sx={
                    "textAlign": "center",
                    "backgroundColor": "#f0f0f0",
                    "& .MuiCardHeader-title": {
                        "fontSize": "1.25rem",
                        "fontWeight": "bold",
                    },
                }
            )
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                qoq_data = get_qoq_leasing_data()
                if qoq_data:
                    nivo.Bar(
                        data=qoq_data,
                        keys=["Area_Leased_in_mln_sft"],
                        indexBy="Quarter",
                        margin={"top": 50, "right": 130, "bottom": 50, "left": 60},
                        padding=0.3,
                        valueScale={"type": "linear", "min": 0, "max": 3},
                        indexScale={"type": "band", "round": True},
                        colors={"scheme": "blues"},
                        defs=[
                            {
                                "id": "gradientA",
                                "type": "linearGradient",
                                "colors": [
                                    { "offset": 0, "color": "#4caf50" },
                                    { "offset": 100, "color": "#2196f3" }
                                ],
                            }
                        ],
                        fill=[{ "match": "*", "id": "gradientA" }],
                        axisBottom={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": -45,
                            "legend": "Quarter",
                            "legendPosition": "middle",
                            "legendOffset": 32
                        },
                        axisLeft={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": "Area Leased (M sq ft)",
                            "legendPosition": "middle",
                            "legendOffset": -40,
                            "tickValues": [0, 1, 2, 3]
                        },
                        labelSkipWidth=12,
                        labelSkipHeight=12,
                        labelTextColor="#000000",
                        labels=lambda d: f'{d.value:.2f}M',
                        isInteractive=True,
                        motionConfig="gentle",
                        legends=[
                            {
                                "dataFrom": "keys",
                                "anchor": "bottom-right",
                                "direction": "column",
                                "justify": False,
                                "translateX": 120,
                                "translateY": 0,
                                "itemsSpacing": 2,
                                "itemWidth": 100,
                                "itemHeight": 20,
                                "itemDirection": "left-to-right",
                                "itemOpacity": 0.85,
                                "symbolSize": 20,
                                "effects": [{"on": "hover", "style": {"itemOpacity": 1}}]
                            }
                        ]
                    )
                else:
                    mui.Typography("No data available for the Q-o-Q trend chart.")

