
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair

df = pd.read_csv("./titanic_cleansed.csv")

st.dataframe(df)

fig, ax = plt.subplots()
ax.scatter(df.parch, df.fare, color="blue")

m, b = np.polyfit(df.pclass, df.fare, deg = 1)
xseq = np.linspace(1, 3, num = 10)

ax.plot(xseq, b + m * xseq, color = 'k', lw = 1.5)

stacked_bar_chart = (
    altair.Chart(df)
    .mark_bar()
    .encode(
        x="parch",
        y="count()",
        color='sibsp',
        tooltip=["parch", "sibsp", "count()"]
    )
    .properties(
        title="Parents/Children (parch) and Siblings/Spouses (sibsp)"
    )
)

st.pyplot(fig)
st.bar_chart(df['sibsp'].value_counts())
st.altair_chart(stacked_bar_chart, use_container_width=True)