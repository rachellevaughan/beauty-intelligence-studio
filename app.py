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

ASSET_DIR = Path(__file__).parent / "assets"
LOGO_PATH = ASSET_DIR / "sephora-logo.png"
HERO_PATH = ASSET_DIR / "beauty-hero.jpeg"


# ==================================================
# LUXURY BEAUTY INTERFACE
# ==================================================

st.markdown(
    """
    <style>
        /* Main application */
        .stApp {
            background: #FAF9F7;
            color: #111111;
        }

        .block-container {
            max-width: 1450px;
            padding-top: 1.5rem;
            padding-bottom: 4rem;
        }

        /* Remove excess Streamlit chrome */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header[data-testid="stHeader"] {
            background: rgba(250, 249, 247, 0.92);
        }

        /* Typography */
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
            margin-top: 1rem !important;
        }

        h3 {
            font-size: 1.15rem !important;
            font-weight: 700 !important;
        }

        p, li, label {
            color: #343434;
        }

        /* Hero */
        .hero-shell {
            background: #000000;
            border-radius: 4px;
            padding: 42px 48px;
            margin-bottom: 24px;
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

        /* Disclaimer */
        .disclaimer {
            background: #FFFFFF;
            border-left: 4px solid #D8B7C2;
            padding: 12px 16px;
            margin: 14px 0 24px 0;
            font-size: 0.82rem;
            color: #555555;
        }

        /* Section labels */
        .section-label {
            color: #8A6673;
            font-size: 0.76rem;
            font-weight: 750;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 2px;
        }

        /* KPI cards */
        div[data-testid="stMetric"] {
            background: #FFFFFF;
            border: 1px solid #E8E5E3;
            border-radius: 3px;
            padding: 20px 18px;
            min-height: 132px;
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

        /* Decision cards */
        .decision-card {
            background: #FFFFFF;
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
            line-height: 1.5;
            font-size: 0.93rem;
        }

        /* Insight panel */
        .insight-panel {
            background: #F0E4E8;
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
            line-height: 1.55;
        }

        /* Tables */
        div[data-testid="stDataFrame"] {
            background: #FFFFFF;
            border: 1px solid #E8E5E3;
        }

        /* Tabs */
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

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #111111;
        }

        section[data-testid="stSidebar"] * {
            color: #F6F6F6;
        }

        section[data-testid="stSidebar"] hr {
            border-color: #3A3A3A;
        }

        /* Buttons */
        .stButton > button {
            background: #000000;
            color: #FFFFFF;
            border: 1px solid #000000;
            border-radius: 2px;
            font-weight: 700;
        }

        .stButton > button:hover {
            background: #2A2A2A;
            color: #FFFFFF;
            border-color: #2A2A2A;
        }

        /* Mobile responsiveness */
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
# CALCULATIONS
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

campaign_data["Promotion ROI"] = (
    campaign_data["Net Incremental Profit"]
    / campaign_data["Campaign Cost"]
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
    st.sidebar.image(str(LOGO_PATH), use_container_width=True)
else:
    st.sidebar.markdown("## SEPHORA")
    st.sidebar.caption("Logo placeholder")

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
    **Leadership question**

    Which commercial investments create profitable, incremental and
    sustainable growth?
    """
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Synthetic portfolio demonstration · Canada"
)


# ==================================================
# HERO HEADER
# ==================================================

hero_text, hero_image = st.columns([1.55, 0.75], gap="large")

with hero_text:
    st.markdown(
        """
        <div class="hero-shell">
            <div class="eyebrow">Canadian Beauty Analytics</div>
            <div class="hero-title">Beauty Intelligence Studio</div>
            <div class="hero-subtitle">
                Executive decision support connecting promotions, client
                behaviour, loyalty outcomes and P&L performance.
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
                background: linear-gradient(
                    135deg,
                    #E9D9DE,
                    #B9919E
                );
                display:flex;
                align-items:center;
                justify-content:center;
                color:#111111;
                text-align:center;
                padding:30px;
            ">
                Add assets/beauty-hero.jpg
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="disclaimer">
        Independent portfolio demonstration using synthetic beauty-retail
        data. This project is not affiliated with, endorsed by or
        commissioned by Sephora.
    </div>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# SUMMARY METRICS AND FINDINGS
# ==================================================

total_promotional_sales = filtered_data["Promotional Sales"].sum()
total_incremental_revenue = filtered_data["Incremental Revenue"].sum()
total_contribution_profit = filtered_data["Contribution Profit"].sum()
total_operating_profit = filtered_data["Operating Profit Impact"].sum()

best_operating_campaign = filtered_data.loc[
    filtered_data["Operating Profit Impact"].idxmax()
]

highest_pull_forward_campaign = filtered_data.loc[
    filtered_data["Pull-Forward Rate"].idxmax()
]

highest_repeat_campaign = filtered_data.loc[
    filtered_data["Repeat Purchase Rate"].idxmax()
]


# ==================================================
# NAVIGATION TABS
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
# TAB 1 — EXECUTIVE SUMMARY
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
        "Total event demand",
    )

    kpi2.metric(
        "Incremental Revenue",
        f"${total_incremental_revenue / 1_000_000:.2f}M",
        "Adjusted for pull-forward",
    )

    kpi3.metric(
        "Contribution Profit",
        f"${total_contribution_profit / 1_000:.0f}K",
        "After variable investment",
    )

    kpi4.metric(
        "Operating Profit",
        f"${total_operating_profit / 1_000:.0f}K",
        "After allocated costs",
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
                    <strong>{best_operating_campaign["Campaign"]}</strong>
                    creates the highest estimated operating-profit impact at
                    <strong>${best_operating_campaign["Operating Profit Impact"]:,.0f}</strong>.
                    Expand through controlled testing.
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
                    <strong>{highest_pull_forward_campaign["Campaign"]}</strong>
                    has an estimated pull-forward rate of
                    <strong>{highest_pull_forward_campaign["Pull-Forward Rate"]:.0%}</strong>.
                    Test narrower targeting or non-price benefits.
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
                    <strong>{highest_repeat_campaign["Campaign"]}</strong>
                    produces the strongest repeat-purchase rate at
                    <strong>{highest_repeat_campaign["Repeat Purchase Rate"]:.0%}</strong>.
                    Explore personalized loyalty treatments.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="insight-panel">
            <div class="insight-title">Executive insight</div>
            <div class="insight-copy">
                Promotional sales alone overstate commercial impact.
                {best_operating_campaign["Campaign"]} generates the strongest
                operating-profit contribution despite not having the largest
                reported sales base. Future investment should prioritize
                incrementality, product margin, repeat behaviour and final
                P&L contribution.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==================================================
# TAB 2 — CAMPAIGN ANALYTICS
# ==================================================

with tab2:
    st.markdown(
        '<div class="section-label">Promotion effectiveness</div>',
        unsafe_allow_html=True,
    )
    st.header("Campaign Analytics")

    campaign_display = filtered_data[
        [
            "Campaign",
            "Promotional Sales",
            "Incremental Revenue",
            "Promotion ROI",
            "Pull-Forward Rate",
            "Repeat Purchase Rate",
            "Acquisition Cost",
        ]
    ].copy()

    currency_columns = [
        "Promotional Sales",
        "Incremental Revenue",
        "Acquisition Cost",
    ]

    percentage_columns = [
        "Promotion ROI",
        "Pull-Forward Rate",
        "Repeat Purchase Rate",
    ]

    for column in currency_columns:
        campaign_display[column] = campaign_display[column].map(
            lambda value: f"${value:,.0f}"
        )

    for column in percentage_columns:
        campaign_display[column] = campaign_display[column].map(
            lambda value: f"{value:.1%}"
        )

    st.dataframe(
        campaign_display,
        use_container_width=True,
        hide_index=True,
    )

    roi_chart = px.bar(
        filtered_data.sort_values("Operating Profit ROI", ascending=False),
        x="Campaign",
        y="Operating Profit ROI",
        text="Operating Profit ROI",
        title="Which promotions create the most profitable growth?",
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

    st.plotly_chart(roi_chart, use_container_width=True)

    pull_forward_chart = go.Figure()

    pull_forward_chart.add_trace(
        go.Bar(
            name="Incremental demand",
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
        title=(
            "Did the promotion create demand or shift future purchases?"
        ),
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
            <div class="insight-title">Commercial implication</div>
            <div class="insight-copy">
                {highest_pull_forward_campaign["Campaign"]} records substantial
                sales, but approximately
                {highest_pull_forward_campaign["Pull-Forward Rate"]:.0%}
                may reflect purchases shifted from a future period. Evaluate
                performance over a four-to-eight-week post-event window.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==================================================
# TAB 3 — P&L IMPACT
# ==================================================

with tab3:
    st.markdown(
        '<div class="section-label">Financial interconnectedness</div>',
        unsafe_allow_html=True,
    )
    st.header("P&L Impact")

    total_cogs = filtered_data["COGS"].sum()
    total_campaign_cost = filtered_data["Campaign Cost"].sum()
    total_fulfillment_cost = filtered_data["Fulfillment Cost"].sum()
    total_variable_cost = filtered_data["Variable Selling Cost"].sum()
    total_fixed_cost = filtered_data["Fixed Operating Allocation"].sum()

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
                "Incremental revenue",
                "COGS",
                "Campaign investment",
                "Fulfillment",
                "Variable selling",
                "Fixed operating",
                "Operating profit",
            ],
            y=[
                total_incremental_revenue,
                -total_cogs,
                -total_campaign_cost,
                -total_fulfillment_cost,
                -total_variable_cost,
                -total_fixed_cost,
                total_operating_profit,
            ],
            increasing={"marker": {"color": "#111111"}},
            decreasing={"marker": {"color": "#C89CAB"}},
            totals={"marker": {"color": "#8A6673"}},
            connector={"line": {"color": "#A7A7A7"}},
        )
    )

    pnl_bridge.update_layout(
        title="How promotional revenue flows through the P&L",
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

    pnl_display = filtered_data[
        [
            "Campaign",
            "Incremental Revenue",
            "Incremental Gross Profit",
            "Campaign Cost",
            "Contribution Profit",
            "Operating Profit Impact",
            "Operating Margin Impact",
        ]
    ].copy()

    pnl_currency_columns = [
        "Incremental Revenue",
        "Incremental Gross Profit",
        "Campaign Cost",
        "Contribution Profit",
        "Operating Profit Impact",
    ]

    for column in pnl_currency_columns:
        pnl_display[column] = pnl_display[column].map(
            lambda value: f"${value:,.0f}"
        )

    pnl_display["Operating Margin Impact"] = (
        pnl_display["Operating Margin Impact"]
        .map(lambda value: f"{value:.1%}")
    )

    st.dataframe(
        pnl_display,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown(
        """
        <div class="insight-panel">
            <div class="insight-title">Cross-functional interpretation</div>
            <div class="insight-copy">
                Marketing shapes campaign investment and response.
                Merchandising shapes product mix and gross margin.
                Retail and Ecommerce influence fulfillment and selling costs.
                Loyalty shapes repeat behaviour and long-term client value.
                Finance evaluates whether the combined impact produces
                operating-profit growth.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==================================================
# TAB 4 — SCENARIO STUDIO
# ==================================================

with tab4:
    st.markdown(
        '<div class="section-label">Executive scenario planning</div>',
        unsafe_allow_html=True,
    )
    st.header("Scenario Studio")

    selected_campaign = st.selectbox(
        "Select a campaign to stress-test",
        filtered_data["Campaign"].tolist(),
    )

    selected_row = filtered_data[
        filtered_data["Campaign"] == selected_campaign
    ].iloc[0]

    slider1, slider2, slider3 = st.columns(3)

    with slider1:
        assumed_incrementality = st.slider(
            "Incrementality rate",
            min_value=0.20,
            max_value=1.00,
            value=float(selected_row["Incrementality Rate"]),
            step=0.01,
            format="%.0f%%",
        )

    with slider2:
        assumed_margin = st.slider(
            "Gross margin rate",
            min_value=0.30,
            max_value=0.80,
            value=float(selected_row["Gross Margin Rate"]),
            step=0.01,
            format="%.0f%%",
        )

    with slider3:
        assumed_campaign_cost = st.slider(
            "Campaign investment",
            min_value=25_000,
            max_value=350_000,
            value=int(selected_row["Campaign Cost"]),
            step=5_000,
            format="$%d",
        )

    simulated_revenue = (
        selected_row["Promotional Sales"]
        * assumed_incrementality
    )

    simulated_gross_profit = (
        simulated_revenue
        * assumed_margin
    )

    simulated_fulfillment = (
        simulated_revenue
        * selected_row["Fulfillment Cost Rate"]
    )

    simulated_variable_cost = (
        simulated_revenue
        * selected_row["Variable Selling Cost Rate"]
    )

    simulated_contribution = (
        simulated_gross_profit
        - assumed_campaign_cost
        - simulated_fulfillment
        - simulated_variable_cost
    )

    simulated_operating_profit = (
        simulated_contribution
        - selected_row["Fixed Operating Allocation"]
    )

    simulated_operating_margin = (
        simulated_operating_profit
        / simulated_revenue
    )

    simulated_roi = (
        simulated_operating_profit
        / assumed_campaign_cost
    )

    sim1, sim2, sim3, sim4 = st.columns(4)

    sim1.metric(
        "Incremental Revenue",
        f"${simulated_revenue:,.0f}",
    )

    sim2.metric(
        "Gross Profit",
        f"${simulated_gross_profit:,.0f}",
    )

    sim3.metric(
        "Contribution Profit",
        f"${simulated_contribution:,.0f}",
    )

    sim4.metric(
        "Operating Profit",
        f"${simulated_operating_profit:,.0f}",
        f"{simulated_operating_margin:.1%} margin",
    )

    if (
        simulated_operating_profit > 150_000
        and simulated_operating_margin >= 0.15
    ):
        st.success(
            f"""
            Scale {selected_campaign} selectively. The campaign generates
            strong operating profit and an attractive margin under the
            selected assumptions.
            """
        )

    elif simulated_operating_profit > 0:
        st.warning(
            f"""
            Optimize {selected_campaign} before scaling. Improve client
            targeting, product mix or campaign efficiency to expand margin.
            """
        )

    else:
        st.error(
            f"""
            Redesign or discontinue {selected_campaign}. It does not produce
            positive operating profit under the selected assumptions.
            """
        )

    st.caption(
        f"Estimated operating-profit ROI: {simulated_roi:.1%}"
    )


# ==================================================
# TAB 5 — RECOMMENDATIONS
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
            <div class="insight-title">Priority recommendation</div>
            <div class="insight-copy">
                Scale <strong>{best_operating_campaign["Campaign"]}</strong>
                through a measured test-and-learn plan. It delivers the
                strongest estimated operating-profit contribution at
                <strong>${best_operating_campaign["Operating Profit Impact"]:,.0f}</strong>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    recommendation_table = pd.DataFrame(
        {
            "Priority": [
                "Scale",
                "Redesign",
                "Retain",
                "Measure",
            ],
            "Decision": [
                best_operating_campaign["Campaign"],
                highest_pull_forward_campaign["Campaign"],
                highest_repeat_campaign["Campaign"],
                "All future campaigns",
            ],
            "Rationale": [
                "Highest operating-profit contribution",
                "Highest estimated pull-forward risk",
                "Strongest repeat-purchase rate",
                "Validate incrementality with a control group",
            ],
            "Next Action": [
                "Expand through controlled testing",
                "Test targeted and non-price treatments",
                "Develop personalized loyalty offers",
                "Monitor demand for four to eight weeks",
            ],
        }
    )

    st.dataframe(
        recommendation_table,
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("Methodology and limitations"):
        st.markdown(
            """
            **Simplified P&L**

            Incremental Revenue  
            − Cost of Goods Sold  
            = Incremental Gross Profit  
            − Campaign Investment  
            − Fulfillment Cost  
            − Variable Selling Cost  
            = Contribution Profit  
            − Fixed Operating Allocation  
            = Operating Profit Impact

            **Production methodology**

            Incrementality should be validated using randomized holdout
            groups, matched controls, difference-in-differences analysis and
            post-promotion demand measurement.

            **Limitation**

            All commercial data and assumptions are synthetic and do not
            represent actual Sephora results.
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