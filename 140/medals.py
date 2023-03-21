import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data: str = data) -> pd.Series:
    df = pd.read_csv(data)
    df_male = (
        df.loc[df["Gender"] == "Men"]
        .groupby("Athlete")["Medal"]
        .count()
        .sort_values(ascending=False)[:1]
    )
    df_female = (
        df.loc[df["Gender"] == "Women"]
        .groupby("Athlete")["Medal"]
        .count()
        .sort_values(ascending=False)[:1]
    )

    return df_male.append(df_female)

    # Pybites Solution was a lot simpler...
    # df = pd.read_csv(data)
    # males = df[df["Gender"] == "Men"]
    # females = df[df["Gender"] == "Women"]
    # best_male = males["Athlete"].value_counts().head(1)
    # best_female = females["Athlete"].value_counts().head(1)
    # return best_male.append(best_female)
