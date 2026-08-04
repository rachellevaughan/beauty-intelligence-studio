from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Beauty Intelligence Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==================================================
# FILE PATHS
# ==================================================

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"

LOGO_PATH = ASSET_DIR / "sephora-logo.png"
HERO_PATH = ASSET_DIR / "beauty-hero.jpeg"


# ==================================================
# VISUAL DESIGN
# ==================================================

st.markdown(
    """
    <style>
        .stApp {
            background-color: #FAF9F7;
            color: #111111;
        }

        .block-container {
            max-width: 1450px;
            padding-top: 1.5rem;
            padding-bottom: 4rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header[data-testid="stHeader"] {
            background-color: rgba(250, 249, 247, 0.95);
        }

        h1, h2, h3 {
            color: #111111;
            letter-spacing: -0.02em;
        }

        h1 {
            font-size: 2.8rem !important;
            font-weight: 750 !important;
        }

        h2 {
            font-size: 1.8rem !important;
            font-weight: 700 !important;
        }

        h3 {
            font-size: 1.15rem !important;
            font-weight: 700 !important;
        }

        p, li, label {
            color: #343434;
        }

        .hero-shell {
            background-color: #000000;
            border-radius: 4px;
            padding: 42px 48px;
            min-height: 260px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .eyebrow {
            color: #D8B7C2;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .hero-title {
            color: #FFFFFF;
            font-size: 3.2rem;
            line-height: 1.02;
            font-weight: 760;
            letter-spacing: -0.045em;
            margin-bottom: 14px;
        }

        .hero-subtitle {
            color: #D9D9D9;
            max-width: 760px;
            font-size: 1.08rem;
            line-height: 1.55;
        }

        .disclaimer {
            background-color: #FFFFFF;
            border-left: 4px solid #D8B7C2;
            padding: 12px 16px;
            margin: 14px 0 24px 0;
            font-size: 0.82rem;
            color: #555555;
        }

        .section-label {
            color: #8A6673;
            font-size: 0.76rem;
            font-weight: 750;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 2px;
        }

        div[data-testid="stMetric"] {
            background-color: #FFFFFF;
            border: 1px solid #E8E5E3;
            border-radius: 3px;
            padding: 20px 18px;
            min-height: 125px;
            box-shadow: 0 3px 14px rgba(0, 0, 0, 0.035);
        }

        div[data-testid="stMetricLabel"] {
            color: #666666;
            font-size: 0.78rem;
            letter-spacing: 0.045em;
            text-transform: uppercase;
        }

        div[data-testid="stMetricValue"] {
            color: #111111;
            font-weight: 750;
        }

        .decision-card {
            background-color: #FFFFFF;
            border: 1px solid #E8E5E3;
            border-top: 4px solid #111111;
            padding: 22px;
            min-height: 240px;
            box-shadow: 0 3px 14px rgba(0, 0, 0, 0.035);
        }

        .decision-number {
            color: #A27C89;
            font-weight: 750;
            font-size: 0.78rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }

        .decision-title {
            color: #111111;
            font-size: 1.25rem;
            font-weight: 750;
            margin: 8px 0;
        }

        .decision-detail {
            color: #555555;
            line-height: 1.55;
            font-size: 0.93rem;
        }

        .insight-panel {
            background-color: #F0E4E8;
            border: 1px solid #E0CDD4;
            padding: 22px 24px;
            margin: 18px 0;
        }

        .insight-title {
            color: #111111;
            font-weight: 750;
            margin-bottom: 8px;
        }

        .insight-copy {
            color: #343434;
            line-height: 1.6;
        }

        .formula-panel {
            background-color: #FFFFFF;
            border: 1px solid #E8E5E3;
            padding: 18px 22px;
            margin: 12px 0 22px 0;
            line-height: 1.8;
        }

        div[data-testid="stDataFrame"] {
            background-color: #FFFFFF;
            border: 1px solid #E8E5E3;
        }

        button[data-baseweb="tab"] {
            font-weight: 650;
            color: #555555;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #000000;
        }

        div[data-baseweb="tab-highlight"] {
            background-color: #000000;
        }

        section[data-testid="stSidebar"] {
            background-color: #111111;
        }

        section[data-testid="stSidebar"] * {
            color: #F6F6F6;
        }

        section[data-testid="stSidebar"] hr {
            border-color: #3A3A3A;
        }

        @media (max-width: 800px) {
            .hero-shell {
                padding: 30px 24px;
            }

            .hero-title {
                font-size: 2.3rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# SYNTHETIC CAMPAIGN DATA
# ==================================================

campaign_data = pd.DataFrame(
    {
        "Campaign": [
            "Beauty Insider Event",
            "Targeted Reactivation",
            "Skincare Event",
            "Fragrance Event",
        ],
        "Category": [
            "Multi-category",
            "Multi-category",
            "Skincare",
            "Fragrance",
        ],
        "Promotional Sales": [
            1_850_000,
            760_000,
            1_240_000,
            940_000,
        ],
        "Incrementality Rate": [
            0.49,
            0.79,
            0.63,
            0.44,
        ],
        "Gross Margin Rate": [
            0.60,
            0.64,
            0.66,
            0.57,
        ],
        "Campaign Cost": [
            245_000,
            85_000,
            175_000,
            135_000,
        ],
        "Repeat Purchase Rate": [
            0.54,
            0.69,
            0.58,
            0.47,
        ],
        "New Clients": [
            1_900,
            850,
            1_100,
            720,
        ],
        "Fulfillment Cost Rate": [
            0.06,
            0.04,
            0.05,
            0.07,
        ],
        "Variable Selling Cost Rate": [
            0.03,
            0.025,
            0.03,
            0.035,
        ],
        "Fixed Operating Allocation": [
            95_000,
            50_000,
            70_000,
            65_000,
        ],
    }
)


# ==================================================
# CAMPAIGN AND P&L CALCULATIONS
# ==================================================

campaign_data["Incremental Revenue"] = (
    campaign_data["Promotional Sales"]
    * campaign_data["Incrementality Rate"]
)

campaign_data["Pull-Forward Rate"] = (
    1 - campaign_data["Incrementality Rate"]
)

campaign_data["Incremental Gross Profit"] = (
    campaign_data["Incremental Revenue"]
    * campaign_data["Gross Margin Rate"]
)

campaign_data["COGS"] = (
    campaign_data["Incremental Revenue"]
    * (1 - campaign_data["Gross Margin Rate"])
)

campaign_data["Fulfillment Cost"] = (
    campaign_data["Incremental Revenue"]
    * campaign_data["Fulfillment Cost Rate"]
)

campaign_data["Variable Selling Cost"] = (
    campaign_data["Incremental Revenue"]
    * campaign_data["Variable Selling Cost Rate"]
)

campaign_data["Net Incremental Profit"] = (
    campaign_data["Incremental Gross Profit"]
    - campaign_data["Campaign Cost"]
)

campaign_data["Gross Profit ROI"] = (
    campaign_data["Net Incremental Profit"]
    / campaign_data["Campaign Cost"]
)

campaign_data["Contribution Profit"] = (
    campaign_data["Incremental Gross Profit"]
    - campaign_data["Campaign Cost"]
    - campaign_data["Fulfillment Cost"]
    - campaign_data["Variable Selling Cost"]
)

campaign_data["Operating Profit Impact"] = (
    campaign_data["Contribution Profit"]
    - campaign_data["Fixed Operating Allocation"]
)

campaign_data["Operating Profit ROI"] = (
    campaign_data["Operating Profit Impact"]
    / campaign_data["Campaign Cost"]
)

campaign_data["Operating Margin Impact"] = (
    campaign_data["Operating Profit Impact"]
    / campaign_data["Incremental Revenue"]
)

campaign_data["Acquisition Cost"] = (
    campaign_data["Campaign Cost"]
    / campaign_data["New Clients"]
)


# ==================================================
# SIDEBAR
# ==================================================

if LOGO_PATH.exists():
    st.sidebar.image(
        str(LOGO_PATH),
        use_container_width=True,
    )
else:
    st.sidebar.markdown("## BEAUTY INTELLIGENCE")
    st.sidebar.caption("Commercial Analytics Studio")

st.sidebar.markdown("---")
st.sidebar.markdown("### Decision Filters")

selected_campaigns = st.sidebar.multiselect(
    "Campaigns",
    options=campaign_data["Campaign"].tolist(),
    default=campaign_data["Campaign"].tolist(),
)

filtered_data = campaign_data[
    campaign_data["Campaign"].isin(selected_campaigns)
].copy()

if filtered_data.empty:
    st.warning("Select at least one campaign to continue.")
    st.stop()

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ### Executive Business Question

    **How should promotional investment be allocated to
    maximize incremental revenue, customer loyalty, and sustainable
    operating profit?**
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("Synthetic portfolio demonstration · Canada")


# ==================================================
# HERO SECTION
# ==================================================

hero_text, hero_image = st.columns(
    [1.55, 0.75],
    gap="large",
)

with hero_text:
    st.markdown(
        """
        <div class="hero-shell">
            <div class="eyebrow">Canadian Beauty Analytics</div>
            <div class="hero-title">Beauty Intelligence Studio</div>
            <div class="hero-subtitle">
                Executive decision support connecting promotional
                incrementality, customer behaviour, loyalty outcomes,
                and end-to-end P&L performance.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_image:
    if HERO_PATH.exists():
        st.image(
            str(HERO_PATH),
            use_container_width=True,
        )
    else:
        st.markdown(
            """
            <div style="
                height: 260px;
                background: linear-gradient(135deg, #E9D9DE, #B9919E);
                display: flex;
                align-items: center;
                justify-content: center;
                color: #111111;
                text-align: center;
                padding: 30px;
            ">
                Add assets/beauty-hero.jpeg
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="disclaimer">
        <strong>Disclaimer:</strong> Independent analytics portfolio project
        using synthetic beauty retail data. This application is not affiliated
        with, endorsed by, sponsored by, or commissioned by Sephora,
        Sephora Canada, LVMH, or their affiliated companies.
    </div>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# SUMMARY METRICS
# ==================================================

total_promotional_sales = filtered_data["Promotional Sales"].sum()
total_incremental_revenue = filtered_data["Incremental Revenue"].sum()
total_incremental_gross_profit = filtered_data[
    "Incremental Gross Profit"
].sum()
total_contribution_profit = filtered_data[
    "Contribution Profit"
].sum()
total_operating_profit = filtered_data[
    "Operating Profit Impact"
].sum()

best_operating_campaign = filtered_data.loc[
    filtered_data["Operating Profit Impact"].idxmax()
]

highest_pull_forward_campaign = filtered_data.loc[
    filtered_data["Pull-Forward Rate"].idxmax()
]

highest_repeat_campaign = filtered_data.loc[
    filtered_data["Repeat Purchase Rate"].idxmax()
]

lowest_operating_campaign = filtered_data.loc[
    filtered_data["Operating Profit Impact"].idxmin()
]


# ==================================================
# NAVIGATION
# ==================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Executive Summary",
        "Campaign Analytics",
        "P&L Impact",
        "Scenario Studio",
        "Recommendations",
    ]
)


# ==================================================
# TAB 1: EXECUTIVE SUMMARY
# ==================================================

with tab1:
    st.markdown(
        '<div class="section-label">Enterprise performance</div>',
        unsafe_allow_html=True,
    )

    st.header("Executive Summary")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric(
        "Promotional Sales",
        f"${total_promotional_sales / 1_000_000:.2f}M",
    )

    kpi2.metric(
        "Incremental Revenue",
        f"${total_incremental_revenue / 1_000_000:.2f}M",
    )

    kpi3.metric(
        "Contribution Profit",
        f"${total_contribution_profit / 1_000:.0f}K",
    )

    kpi4.metric(
        "Operating Profit",
        f"${total_operating_profit / 1_000:.0f}K",
    )

    st.markdown(
        f"""
        <div class="insight-panel">
            <div class="insight-title">Executive Insight</div>
            <div class="insight-copy">
                <strong>{best_operating_campaign['Campaign']}</strong>
                delivers the highest estimated operating-profit contribution
                despite not generating the greatest promotional sales.
                This highlights the importance of evaluating performance
                through incrementality, product margin, customer retention,
                and end-to-end P&L impact. Future investment should prioritize
                campaigns that create sustainable, profitable growth rather
                than short-term revenue spikes or purchase pull-forward.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Today’s leadership decisions")

    decision1, decision2, decision3 = st.columns(3)

    with decision1:
        st.markdown(
            f"""
            <div class="decision-card">
                <div class="decision-number">Decision 01</div>
                <div class="decision-title">Scale selectively</div>
                <div class="decision-detail">
                    <strong>{best_operating_campaign['Campaign']}</strong>
                    generates the highest estimated operating-profit
                    contribution at
                    <strong>
                    ${best_operating_campaign['Operating Profit Impact']:,.0f}
                    </strong>.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with decision2:
        st.markdown(
            f"""
            <div class="decision-card">
                <div class="decision-number">Decision 02</div>
                <div class="decision-title">Redesign before scaling</div>
                <div class="decision-detail">
                    <strong>{highest_pull_forward_campaign['Campaign']}</strong>
                    has an estimated pull-forward rate of
                    <strong>
                    {highest_pull_forward_campaign['Pull-Forward Rate']:.0%}
                    </strong>, indicating that reported sales may overstate
                    newly created demand.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with decision3:
        st.markdown(
            f"""
            <div class="decision-card">
                <div class="decision-number">Decision 03</div>
                <div class="decision-title">Protect client value</div>
                <div class="decision-detail">
                    <strong>{highest_repeat_campaign['Campaign']}</strong>
                    generates the strongest repeat-purchase rate at
                    <strong>
                    {highest_repeat_campaign['Repeat Purchase Rate']:.0%}
                    </strong>, supporting further loyalty-focused testing.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==================================================
# TAB 2: CAMPAIGN ANALYTICS
# ==================================================

with tab2:
    st.markdown(
        '<div class="section-label">Promotion effectiveness</div>',
        unsafe_allow_html=True,
    )

    st.header("Campaign Analytics")

    executive_table = filtered_data[
        [
            "Campaign",
            "Incremental Revenue",
            "Contribution Profit",
            "Operating Profit Impact",
            "Operating Margin Impact",
            "Operating Profit ROI",
            "Pull-Forward Rate",
            "Repeat Purchase Rate",
        ]
    ].copy()

    currency_columns = [
        "Incremental Revenue",
        "Contribution Profit",
        "Operating Profit Impact",
    ]

    percentage_columns = [
        "Operating Margin Impact",
        "Operating Profit ROI",
        "Pull-Forward Rate",
        "Repeat Purchase Rate",
    ]

    for column in currency_columns:
        executive_table[column] = executive_table[column].map(
            lambda value: f"${value:,.0f}"
        )

    for column in percentage_columns:
        executive_table[column] = executive_table[column].map(
            lambda value: f"{value:.1%}"
        )

    st.dataframe(
        executive_table,
        use_container_width=True,
        hide_index=True,
    )

    roi_chart = px.bar(
        filtered_data.sort_values(
            "Operating Profit ROI",
            ascending=False,
        ),
        x="Campaign",
        y="Operating Profit ROI",
        text="Operating Profit ROI",
        title="Targeted campaigns produce the strongest profit efficiency",
    )

    roi_chart.update_traces(
        texttemplate="%{text:.0%}",
        textposition="outside",
        marker_color="#111111",
    )

    roi_chart.update_layout(
        paper_bgcolor="#FAF9F7",
        plot_bgcolor="#FAF9F7",
        xaxis_title="",
        yaxis_title="Operating profit ROI",
        yaxis_tickformat=".0%",
        showlegend=False,
        margin=dict(t=70, b=20),
    )

    st.plotly_chart(
        roi_chart,
        use_container_width=True,
    )

    pull_forward_chart = go.Figure()

    pull_forward_chart.add_trace(
        go.Bar(
            name="Estimated incremental demand",
            x=filtered_data["Campaign"],
            y=filtered_data["Incrementality Rate"],
            marker_color="#111111",
            text=filtered_data["Incrementality Rate"],
            texttemplate="%{text:.0%}",
        )
    )

    pull_forward_chart.add_trace(
        go.Bar(
            name="Estimated pull-forward",
            x=filtered_data["Campaign"],
            y=filtered_data["Pull-Forward Rate"],
            marker_color="#D8B7C2",
            text=filtered_data["Pull-Forward Rate"],
            texttemplate="%{text:.0%}",
        )
    )

    pull_forward_chart.update_layout(
        barmode="stack",
        title="Broad promotions generate more shifted demand",
        paper_bgcolor="#FAF9F7",
        plot_bgcolor="#FAF9F7",
        xaxis_title="",
        yaxis_title="Share of promotional sales",
        yaxis_tickformat=".0%",
        legend_title="",
        margin=dict(t=70, b=20),
    )

    st.plotly_chart(
        pull_forward_chart,
        use_container_width=True,
    )

    st.markdown(
        f"""
        <div class="insight-panel">
            <div class="insight-title">Commercial Implication</div>
            <div class="insight-copy">
                <strong>{highest_pull_forward_campaign['Campaign']}</strong>
                records meaningful promotional demand, but approximately
                <strong>
                {highest_pull_forward_campaign['Pull-Forward Rate']:.0%}
                </strong>
                may reflect purchases shifted from a future period rather than
                newly created demand. Performance should therefore be measured
                across the event and a four-to-eight-week post-promotion window.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==================================================
# TAB 3: P&L IMPACT
# ==================================================

with tab3:
    st.markdown(
        '<div class="section-label">Financial interconnectedness</div>',
        unsafe_allow_html=True,
    )

    st.header("P&L Impact")

    total_cogs = filtered_data["COGS"].sum()
    total_campaign_cost = filtered_data["Campaign Cost"].sum()
    total_fulfillment_cost = filtered_data[
        "Fulfillment Cost"
    ].sum()
    total_variable_selling_cost = filtered_data[
        "Variable Selling Cost"
    ].sum()
    total_fixed_operating_cost = filtered_data[
        "Fixed Operating Allocation"
    ].sum()

    pnl1, pnl2, pnl3, pnl4 = st.columns(4)

    pnl1.metric(
        "Incremental Revenue",
        f"${total_incremental_revenue / 1_000_000:.2f}M",
    )

    pnl2.metric(
        "Incremental Gross Profit",
        f"${total_incremental_gross_profit / 1_000:.0f}K",
    )

    pnl3.metric(
        "Contribution Profit",
        f"${total_contribution_profit / 1_000:.0f}K",
    )

    pnl4.metric(
        "Operating Profit",
        f"${total_operating_profit / 1_000:.0f}K",
    )

    pnl_bridge = go.Figure(
        go.Waterfall(
            orientation="v",
            measure=[
                "absolute",
                "relative",
                "relative",
                "relative",
                "relative",
                "relative",
                "total",
            ],
            x=[
                "Incremental Revenue",
                "COGS",
                "Campaign Investment",
                "Fulfillment",
                "Variable Selling",
                "Fixed Operating",
                "Operating Profit",
            ],
            y=[
                total_incremental_revenue,
                -total_cogs,
                -total_campaign_cost,
                -total_fulfillment_cost,
                -total_variable_selling_cost,
                -total_fixed_operating_cost,
                total_operating_profit,
            ],
            increasing={
                "marker": {
                    "color": "#111111",
                }
            },
            decreasing={
                "marker": {
                    "color": "#C89CAB",
                }
            },
            totals={
                "marker": {
                    "color": "#8A6673",
                }
            },
            connector={
                "line": {
                    "color": "#A7A7A7",
                }
            },
        )
    )

    pnl_bridge.update_layout(
        title="Campaign costs materially reduce reported sales value",
        paper_bgcolor="#FAF9F7",
        plot_bgcolor="#FAF9F7",
        yaxis_title="CAD",
        showlegend=False,
        margin=dict(t=70, b=20),
    )

    st.plotly_chart(
        pnl_bridge,
        use_container_width=True,
    )

    st.caption(
        """
        The waterfall begins with incremental revenue and deducts product,
        campaign, fulfillment, selling, and allocated operating costs to
        arrive at estimated operating profit.
        """
    )

    st.markdown(
        """
        <div class="formula-panel">
            <strong>Simplified P&L flow</strong><br><br>
            Incremental Revenue<br>
            − Cost of Goods Sold<br>
            = Incremental Gross Profit<br>
            − Campaign Investment<br>
            − Fulfillment and Variable Selling Costs<br>
            = Contribution Profit<br>
            − Fixed Operating Allocation<br>
            = Operating Profit Impact
        </div>
        """,
        unsafe_allow_html=True,
    )

    operating_profit_chart = px.bar(
        filtered_data.sort_values(
            "Operating Profit Impact",
            ascending=False,
        ),
        x="Campaign",
        y="Operating Profit Impact",
        text="Operating Profit Impact",
        title="Which campaigns create the most operating profit?",
    )

    operating_profit_chart.update_traces(
        texttemplate="$%{text:,.0f}",
        textposition="outside",
        marker_color="#111111",
    )

    operating_profit_chart.update_layout(
        paper_bgcolor="#FAF9F7",
        plot_bgcolor="#FAF9F7",
        xaxis_title="",
        yaxis_title="Operating profit impact",
        yaxis_tickprefix="$",
        showlegend=False,
        margin=dict(t=70, b=20),
    )

    st.plotly_chart(
        operating_profit_chart,
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="insight-panel">
            <div class="insight-title">
                Cross-Functional Business Insight
            </div>
            <div class="insight-copy">
                Cross-Functional Business Insight

                The data demonstrates that promotional sales alone overstate commercial success. Once incrementality, gross margins, fulfillment costs, customer retention, and campaign investment are incorporated, operating-profit contribution becomes the more meaningful measure of performance. Marketing creates demand, Merchandising determines the profitability of that demand through product mix and margins, Retail and Ecommerce influence delivery economics, and Loyalty indicates whether campaigns generate lasting customer value through repeat purchasing. By integrating these drivers into a single financial view, Finance identifies which campaigns create sustainable profit rather than temporary revenue growth, enabling more disciplined investment decisions across the business.

            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==================================================
# TAB 4: SCENARIO STUDIO
# ==================================================

with tab4:
    st.markdown(
        '<div class="section-label">Executive scenario planning</div>',
        unsafe_allow_html=True,
    )

    st.header("Scenario Studio")

    selected_campaign = st.selectbox(
        "Select a campaign to stress-test",
        options=filtered_data["Campaign"].tolist(),
    )

    selected_row = filtered_data[
        filtered_data["Campaign"] == selected_campaign
    ].iloc[0]

    slider1, slider2 = st.columns(2)
    slider3, slider4 = st.columns(2)

    with slider1:
        assumed_incrementality = st.slider(
            "Incrementality rate",
            min_value=0.20,
            max_value=1.00,
            value=float(
                selected_row["Incrementality Rate"]
            ),
            step=0.01,
            format="%.0f%%",
        )

    with slider2:
        assumed_margin = st.slider(
            "Gross margin rate",
            min_value=0.30,
            max_value=0.80,
            value=float(
                selected_row["Gross Margin Rate"]
            ),
            step=0.01,
            format="%.0f%%",
        )

    with slider3:
        assumed_campaign_cost = st.slider(
            "Campaign investment",
            min_value=25_000,
            max_value=350_000,
            value=int(
                selected_row["Campaign Cost"]
            ),
            step=5_000,
            format="$%d",
        )

    with slider4:
        assumed_fulfillment_rate = st.slider(
            "Fulfillment cost rate",
            min_value=0.01,
            max_value=0.12,
            value=float(
                selected_row["Fulfillment Cost Rate"]
            ),
            step=0.005,
            format="%.1f%%",
        )

    simulated_incremental_revenue = (
        selected_row["Promotional Sales"]
        * assumed_incrementality
    )

    simulated_gross_profit = (
        simulated_incremental_revenue
        * assumed_margin
    )

    simulated_fulfillment_cost = (
        simulated_incremental_revenue
        * assumed_fulfillment_rate
    )

    simulated_variable_selling_cost = (
        simulated_incremental_revenue
        * selected_row["Variable Selling Cost Rate"]
    )

    simulated_contribution_profit = (
        simulated_gross_profit
        - assumed_campaign_cost
        - simulated_fulfillment_cost
        - simulated_variable_selling_cost
    )

    simulated_operating_profit = (
        simulated_contribution_profit
        - selected_row["Fixed Operating Allocation"]
    )

    simulated_operating_margin = (
        simulated_operating_profit
        / simulated_incremental_revenue
    )

    simulated_operating_roi = (
        simulated_operating_profit
        / assumed_campaign_cost
    )

    contribution_margin_rate = (
        assumed_margin
        - assumed_fulfillment_rate
        - selected_row["Variable Selling Cost Rate"]
    )

    if contribution_margin_rate > 0:
        required_incremental_revenue = (
            assumed_campaign_cost
            + selected_row["Fixed Operating Allocation"]
        ) / contribution_margin_rate

        break_even_incrementality = (
            required_incremental_revenue
            / selected_row["Promotional Sales"]
        )
    else:
        break_even_incrementality = float("inf")

    sim1, sim2, sim3, sim4 = st.columns(4)

    sim1.metric(
        "Incremental Revenue",
        f"${simulated_incremental_revenue:,.0f}",
    )

    sim2.metric(
        "Gross Profit",
        f"${simulated_gross_profit:,.0f}",
    )

    sim3.metric(
        "Contribution Profit",
        f"${simulated_contribution_profit:,.0f}",
    )

    sim4.metric(
        "Operating Profit",
        f"${simulated_operating_profit:,.0f}",
    )

    output1, output2, output3 = st.columns(3)

    output1.metric(
        "Operating Margin",
        f"{simulated_operating_margin:.1%}",
    )

    output2.metric(
        "Operating Profit ROI",
        f"{simulated_operating_roi:.1%}",
    )

    if break_even_incrementality == float("inf"):
        break_even_text = "Not achievable"
    else:
        break_even_text = f"{break_even_incrementality:.1%}"

    output3.metric(
        "Break-Even Incrementality",
        break_even_text,
    )

    if (
        simulated_operating_profit > 150_000
        and simulated_operating_margin >= 0.15
    ):
        st.success(
            f"""
            **Scale selectively:** {selected_campaign} generates strong
            operating profit and an attractive operating margin under the
            selected assumptions. Expand through controlled testing while
            preserving a holdout group.
            """
        )

    elif simulated_operating_profit > 0:
        st.warning(
            f"""
            **Optimize before scaling:** {selected_campaign} remains
            profitable, but further investment should focus on improving
            incrementality, product mix, campaign efficiency, or fulfillment
            economics.
            """
        )

    else:
        st.error(
            f"""
            **Redesign or discontinue:** {selected_campaign} does not create
            positive operating profit under the selected assumptions.
            """
        )


# ==================================================
# TAB 5: RECOMMENDATIONS
# ==================================================

with tab5:
    st.markdown(
        '<div class="section-label">Strategic priorities</div>',
        unsafe_allow_html=True,
    )

    st.header("Executive Recommendations")

    st.markdown(
        f"""
        <div class="insight-panel">
            <div class="insight-title">Priority Recommendation</div>
            <div class="insight-copy">
                The analysis identifies
                <strong>{best_operating_campaign['Campaign']}</strong>
                as the strongest candidate for future investment. Although it
                does not generate the highest promotional sales, it produces
                the greatest estimated operating-profit contribution of
                <strong>
                ${best_operating_campaign['Operating Profit Impact']:,.0f}
                </strong>,
                demonstrating a more efficient conversion of promotional
                investment into profitable customer demand. A disciplined
                test-and-learn expansion can validate scalability, refine
                audience targeting, and protect financial performance before
                a broader rollout.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    recommendation_table = pd.DataFrame(
        {
            "Priority": [
                "Scale",
                "Optimize",
                "Redesign",
                "Measure",
            ],
            "Decision": [
                best_operating_campaign["Campaign"],
                highest_repeat_campaign["Campaign"],
                lowest_operating_campaign["Campaign"],
                "All future campaigns",
            ],
            "Data Rationale": [
                (
                    "Highest operating-profit contribution at "
                    f"${best_operating_campaign['Operating Profit Impact']:,.0f}"
                ),
                (
                    "Strongest repeat-purchase rate at "
                    f"{highest_repeat_campaign['Repeat Purchase Rate']:.0%}"
                ),
                (
                    "Lowest operating-profit contribution at "
                    f"${lowest_operating_campaign['Operating Profit Impact']:,.0f}"
                ),
                (
                    "Incrementality and pull-forward remain estimated inputs"
                ),
            ],
            "Next Action": [
                "Expand through controlled test cells",
                "Develop personalized loyalty treatments",
                "Review targeting, offer depth, and product mix",
                "Use holdout groups and post-event measurement",
            ],
        }
    )

    st.dataframe(
        recommendation_table,
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("Methodology, assumptions, and limitations"):
        st.markdown(
            """
            ### Simplified P&L

            Incremental Revenue  
            − Cost of Goods Sold  
            = Incremental Gross Profit  
            − Campaign Investment  
            − Fulfillment Cost  
            − Variable Selling Cost  
            = Contribution Profit  
            − Fixed Operating Allocation  
            = Operating Profit Impact

            ### Incrementality

            Incrementality represents the estimated share of promotional
            sales caused by the campaign rather than shifted from another
            period, product, or channel.

            ### Production methodology

            A production analysis should validate incrementality using:

            - randomized holdout groups
            - matched test and control customers
            - difference-in-differences analysis
            - post-promotion demand monitoring
            - category, channel, and regional controls

            ### Fixed-cost assumption

            Fixed operating costs represent illustrative campaign-level
            allocations. A production financial evaluation should distinguish
            avoidable incremental costs from existing overhead.

            ### Limitation

            All commercial data and assumptions are synthetic and do not
            represent actual Sephora or LVMH performance.
            """
        )


# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.caption(
    """
    Independent analytics portfolio project · Python · Pandas · Plotly ·
    Streamlit
    """
)