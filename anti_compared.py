import streamlit as st
import pandas as pd
import altair as alt

# 將您提供的數據轉換為DataFrame
data = {
    "Antibiotic": [
        "Penicillin", "Oxacillin", "Ampicillin", "Unasyn", "Tazocin",
        "1代Cefa", "2代Cefa", "Cefmetazole", "Ceftriaxone", "Ceftazidime",
        "Flomoxef", "Brosym", "Cefepime", "Cefpirome", "Ceftobiprole",
        "Ertapenem", "Imipenem", "Meropenem", "Doripenem",
        "Ciprofloxacin", "Levofloxacin", "Moxifloxacin",
        "Vancomycin", "Teicoplanin", "Daptomycin", "Linezolid", "Tigecycline",
        "Fusidic acid", "Doxycycline", "Colistin", "TMP-SMX", "Gentamicin",
        "Amikacin", "Clindamycin", "Metronidazole", "Azithromycin",
        "Fosfomycin", "Rifampin"
    ],
    "Strep.": [1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 4, 3, 3, 3, 4, 4, 4, 4, 2, 3],
    "MSSA": [3, 1, 3, 2, 2, 1, 2, 2, 2, 4, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 4, 2, 3, 4, 2, 4, 4,
             2, 3],
    "MRSA": [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 2, 4, 2, 3, 4, 3, 4, 4,
             2, 3],
    "Efc": [1, 4, 1, 2, 2, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 1, 1, 2, 2, 2, 3, 3, 4, 4, 3, 4, 4, 4, 4,
            3, 3],
    "Efm": [3, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 1, 2, 3, 3, 4, 4, 3, 4, 4, 4, 4,
            3, 3],
    "GNB": [4, 4, 2, 2, 1, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 4, 4, 4, 4, 2, 4, 4, 2, 3, 2, 2, 4, 4, 4,
            2, 4],
    "En.Bac": [4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 1, 4, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4,
               4, 2, 4],
    "PsA": [4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 2, 1, 2, 1, 4, 2, 2, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 2, 2, 4, 4, 4,
            3, 4],
    "AB": [4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4],
    "Anae": [4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 1, 2, 4, 2, 4, 1, 1, 1, 1, 4, 4, 2, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 2, 1, 4, 4, 4],
    "Atyp.": [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 1, 1, 4, 4, 4, 4, 2, 4, 1, 4, 4, 4, 4, 4, 4, 1, 4, 4]
}

df = pd.DataFrame(data)

# Streamlit 應用程式
st.title('抗生素抗菌範圍比較工具')

# 選擇抗生素
# Add a placeholder to the beginning of the unique antibiotics list
unique_antibiotics = ['請選擇'] + list(df['Antibiotic'].unique())

# Select Antibiotics with a default placeholder
antibiotic_1 = st.selectbox('選擇第一種抗生素:', unique_antibiotics, index=0)
antibiotic_2 = st.selectbox('選擇第二種抗生素:', unique_antibiotics, index=0)

bacteria_order = [
    "Strep.", "MSSA", "MRSA", "Efc", "Efm",
    "GNB", "En.Bac", "PsA", "AB", "Anae", "Atyp."
]

# 獲取並顯示選擇的抗生素信息
if st.button('比較'):
    st.write('比較結果:')
    df1 = df[df['Antibiotic'] == antibiotic_1][bacteria_order].T
    df2 = df[df['Antibiotic'] == antibiotic_2][bacteria_order].T

    comparison = pd.concat([df1, df2], axis=1)
    comparison.columns = [antibiotic_1, antibiotic_2]
    comparison = comparison.reset_index()
    comparison.rename(columns={'index': 'Bacteria'}, inplace=True)

    # Melt the comparison dataframe for Altair chart
    comparison_melted = comparison.melt(id_vars='Bacteria', var_name='Antibiotic', value_name='Effectiveness')

    range_ = ['darkgreen', 'lightgreen', 'yellow', 'red']  # 1: 'darkgreen', 2: 'lightgreen', 3: 'yellow', 4: 'red'

    # 使用Altair繪製圖表
    chart = alt.Chart(comparison_melted).mark_circle(size=300).encode(
        x=alt.X('Bacteria:N', axis=alt.Axis(title='', labelFontSize=20, orient='top'), scale=alt.Scale(domain=bacteria_order)),
        y=alt.Y('Antibiotic:N', axis=alt.Axis(title='', labelFontSize=20)),
        color=alt.Color('Effectiveness:O', scale=alt.Scale(domain=[1, 2, 3, 4], range=range_), legend=None),
        tooltip=['Bacteria', 'Antibiotic', 'Effectiveness']
    ).properties(
        width=400,  # Adjust width to accommodate all bacteria categories
        height=200
    )

    st.altair_chart(chart, use_container_width=True)


bacteria_type = st.selectbox('選擇細菌:', ['請選擇'] + list(df.columns[1:]), index=0)

if st.button('有效抗生素'):
    bacteria_df = df[['Antibiotic', bacteria_type]]
    st.write(f"Efficacy of antibiotics against {bacteria_type}")

  # Melt the comparison dataframe
    bacteria_df_melted = bacteria_df.melt(id_vars='Antibiotic', var_name='Bacteria', value_name='Effectiveness')

    antibiotic_order = df['Antibiotic'].unique().tolist()

    range_ = ['darkgreen', 'lightgreen', 'yellow', 'red']  # 1: 'darkgreen', 2: 'lightgreen', 3: 'yellow', 4: 'red'


    # 使用Altair繪製圖表
    chart = alt.Chart(bacteria_df_melted).mark_circle(size=300).encode(
        x=alt.X('Bacteria:N', axis=alt.Axis(title='', labelFontSize=20, orient='top'), scale=alt.Scale(reverse=True)),
        y=alt.Y('Antibiotic:N', axis=alt.Axis(title='', labelFontSize=20), scale=alt.Scale(domain=antibiotic_order)),
        color=alt.Color('Effectiveness:O', scale=alt.Scale(domain=[1, 2, 3, 4], range=range_), legend=None),
        tooltip=['Antibiotic', 'Bacteria', 'Effectiveness']
    ).properties(
        width=300,
        height=1500,
        padding={'left': 100, 'right': 10, 'top': 10, 'bottom': 10}  # 调整图表边距
        ).configure_view(
        strokeWidth=0  # 移除图表边框
        ).configure_axis(
        labelLimit=0  # 移除标签长度限制
        )

    st.altair_chart(chart)