import streamlit as st
import pandas as pd
import altair as alt

# 將您提供的數據轉換為DataFrame
data = {
    "Antibiotic": [
        "Penicillin", "Oxacillin", "Ampicillin", "Unasyn", "Tazocin",
        "1st", "2nd", "Cefmetazole", "Ceftriaxone", "Ceftazidime",
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
antibiotic_1 = st.selectbox('選擇第一種抗生素:', df['Antibiotic'].unique())
antibiotic_2 = st.selectbox('選擇第二種抗生素:', df['Antibiotic'].unique())

# 獲取並顯示選擇的抗生素信息
if st.button('比較'):
    st.write('比較結果:')
    df1 = df[df['Antibiotic'] == antibiotic_1].drop('Antibiotic', axis=1).T
    df2 = df[df['Antibiotic'] == antibiotic_2].drop('Antibiotic', axis=1).T
    comparison = pd.concat([df1, df2], axis=1)
    comparison.columns = [antibiotic_1, antibiotic_2]
    # Transpose the comparison dataframe
    comparison = comparison.T


    comparison.reset_index(inplace=True)
    comparison.rename(columns={'index': 'Bacteria'}, inplace=True)

    # Melt the comparison dataframe
    comparison_melted = comparison.melt(id_vars='Bacteria', var_name='Antibiotic', value_name='Effectiveness')

    range_ = ['darkgreen', 'lightgreen', 'yellow', 'red']  # 1: 'darkgreen', 2: 'lightgreen', 3: 'yellow', 4: 'red'

    # 使用Altair繪製圖表
    chart = alt.Chart(comparison_melted).mark_circle(size=300).encode(
        x=alt.X('Antibiotic:N', axis=alt.Axis(title='', labelFontSize=20, orient='top'), scale=alt.Scale(reverse=True)),
        y=alt.Y('Bacteria:N', axis=alt.Axis(title='', labelFontSize=20), scale=alt.Scale(reverse=True)),
        color=alt.Color('Effectiveness:O', scale=alt.Scale(domain=[1, 2, 3, 4], range=range_), legend=None),
        tooltip=['Antibiotic', 'Bacteria', 'Effectiveness']
    ).properties(
        width=400,
        height=200  # Adjust height if needed to display all bacteria categories
    )

    st.altair_chart(chart, use_container_width=True)

