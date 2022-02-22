import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importing data
df = pd.read_csv('medical_examination.csv', index_col="id")

# Adding an 'overweight' column
df["overweight"] = df["weight"] / ((df["height"] / 100) ** 2) > 25
# If BMI value is greater than 25 -> overweight
df["overweight"] = df["overweight"].map({True: 1, False: 0})
# 1 = is overweight ; 0 = is NOT overweight

# Normalizing data by making 0 always good and 1 always bad. E.g:
# If the value of 'cholesterol' or 'gluc' is 1 (=Good), changing it to 0.
# If the value is more than 1 (=Bad), changing it to 1.

df["cholesterol"] = df["cholesterol"] > 1
df["cholesterol"] = df["cholesterol"].map({True: 1, False: 0})
df["gluc"] = df["gluc"] > 1
df["gluc"] = df["gluc"].map({True: 1, False: 0})


# Drawing Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df[plot_columns],
                     id_vars="cardio",
                     value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()) \
        .rename(columns={'value': 'total'}).reset_index()

    sns.set_style("white")
    fig = sns.catplot(x="variable", y="total", hue="value", data=df_cat, kind="bar", col="cardio")

    fig.set_xlabels('variable', fontsize=15)
    fig.set_ylabels('total', fontsize=15)
    plt.subplots_adjust(bottom=0.1)

    fig.savefig('catplot.png')
    return fig


# Drawing Heat Map
def draw_heat_map():
    # Cleaning the data.
    df_heat = df.copy()
    df_heat.drop(df_heat[df_heat["ap_lo"] > df_heat["ap_hi"]].index, inplace=True)
    df_heat.drop(df_heat[df_heat["height"] < df_heat["height"].quantile(0.025)].index, inplace=True)
    df_heat.drop(df_heat[df_heat["height"] > df_heat["height"].quantile(0.975)].index, inplace=True)
    df_heat.drop(df_heat[df_heat["weight"] < df_heat["weight"].quantile(0.025)].index, inplace=True)
    df_heat.drop(df_heat[df_heat["weight"] > df_heat["weight"].quantile(0.975)].index, inplace=True)

    corr = df_heat.corr()
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    fig, ax = plt.subplots(figsize=(16, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.1, square=True, ax=ax)

    fig.savefig('heatmap.png')
    return fig
