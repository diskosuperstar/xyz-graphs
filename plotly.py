import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter3d(
    x=[1, 2, 3],
    y=[4, 5, 6],
    z=[7, 8, 9],
    mode='markers'
)])

fig.show()
