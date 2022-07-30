import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:", layout="wide")

df = pd.read_excel(
    io="penindakan-pelanggaran-lantas-2021-maret.xlsx",
    engine="openpyxl",
)
# Add 'hour' column to dataframe

data = ['bap_tilang', 'stop_operasi', 'bap_polisi', 'stop_operasi_polisi',
        'penderekan', 'ocp_roda_dua', 'ocp_roda_empat', 'angkut_motor']
df['total'] = df[data].sum(axis=1)
# view dataframe on page


# SIDEBAR
st.sidebar.header("Filter :")
wilayah = st.sidebar.multiselect(
    "Select The wilayah Type :",
    options=df["wilayah"].unique(),
    default=df["wilayah"].unique()
)


df_selection = df.query(
    "wilayah == @wilayah "
)

st.markdown("""---""")  # markdown


st.title("Data Penilangan  2021 - Maret ")


st.markdown("""---""")
st.dataframe(df_selection)


total_penindakan = (
    df_selection.groupby(by=["wilayah"]).sum()[
        ["total"]].sort_values(by="wilayah")
)
fig_total = px.bar(
    total_penindakan,
    x="total",
    y=total_penindakan.index,
    orientation="h",
    title="<b>Total penindakan pelanggarans Lalu Lintas</b>",
    color_discrete_sequence=["#00FFFF"] * len(total_penindakan),
    template="plotly_white",
)
fig_total.update_layout(
    plot_bgcolor="rgba(1,1,1,1)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_total, use_container_width=True)
total = int(df_selection["total"].sum())
st.subheader(f"Total Kasus: {total:,} Kasus")
st.markdown("""---""")