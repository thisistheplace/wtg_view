import copy
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def figure(df: pd.DataFrame, count: int):
    if df is None:
        data = {
            "time": [datetime.today()],
            "duration": [0.0],
            "count": [count]
        }
        df = pd.DataFrame.from_dict(data)
    else:
        lastrow = df.iloc[-1]
        newrow = copy.deepcopy(lastrow)
        newrow["time"] = datetime.today()
        newrow["duration"] = (newrow["time"] - lastrow["time"]).total_seconds()
        newrow["count"] = count
        df.loc[df.shape[0]] = newrow

    # fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig = make_subplots()

    fig.add_trace(
        go.Scatter(x=df['time'], y=df['duration'], mode="lines+markers"),
        secondary_y=False,
    )

    # fig.add_trace(
    #     go.Bar(x=df['time'], y=df['duration']),
    #     secondary_y=True,
    # )

    # Set x-axis title
    fig.update_xaxes(title_text="time")

    # Set y-axes titles
    fig.update_yaxes(title_text="duration", secondary_y=False)
    # fig.update_yaxes(title_text="duration", secondary_y=True)

    return df, fig