from django.shortcuts import render
import folium
# Create your views here.
def map(request):
    figure = folium.Figure()
    #caminho ate seu arquivo .json
    url = ("Manager/static")
    #acessando arquivo
    state_geo = f"{url}/br_states.json"
    m = folium.Map(location=[-15.77972, -47.92972], zoom_start=4.1)
    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        fill_color="green",
        fill_opacity=0.7,
        line_opacity=0.2,
    ).add_to(m)
    folium.LayerControl().add_to(m)
    m.add_to(figure)
    figure.render()
    return render(request,'map.html',{"map":figure})

