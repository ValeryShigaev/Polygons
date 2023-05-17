<template>
  <div class="container">
    <l-map style="height: 700px;" 
      :zoom=6 
      :center=[29.981272,29.105190]
      ref="map">
      <l-tile-layer 
       :visible=true            
       :url="'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'">
      </l-tile-layer>
      <l-geo-json
       :show="showPoly"
       :geojson="geojsonPoly"
       :options="options"
       ref="polyLayer">
      </l-geo-json>
      <l-marker 
        v-for="vertex, index in vertexes"
        :key="index"
        :lat-lng="vertex">
      </l-marker>
    </l-map>
    <template v-if="showPopup">
      <div class="popup">
        <div class="popup_container">
          <h5>Places:</h5>
          <ul class="places_list">
            <li class="place"
             v-for="place in places"
             :key="place"
            >{{ place }}</li>
          </ul>
          <span class="pop">Population: {{ pop }}</span>
          <template
            v-if="loading"
            >
              <div class="loading_container">
                  <span class="preloader__item preloader__item1"></span>
                  <span class="preloader__item preloader__item2"></span>
                  <span class="preloader__item preloader__item3"></span>
                  <span class="preloader__item preloader__item4"></span>
              </div>
          </template>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson, LMarker } from 'vue2-leaflet';
import { getPoly, getPolyData } from './api.js';
import 'leaflet/dist/leaflet.css';

export default {
  name: 'App',
  components: {
    'l-map': LMap,
    'l-tile-layer': LTileLayer,
    'l-geo-json': LGeoJson,
    'l-marker': LMarker,
  },
  data() {
    return {
      showPoly: true,
      geojsonPoly: null,
      geojsonPoints: null,
      showPopup: false,
      prevLayerClicked: null,
      loading: false,
      places: null,
      pop: null,
      vertexes: null,
    }
  },
  methods: {
    onEachFeatureFunction(feature, layer) {

      layer.bindTooltip(
        "<div>" +
          feature.properties.id +
          "</div>",
        { permanent: false, sticky: true }
      );
      layer.on({
        click: this.objectClickHandler
      });
      //layer.on("mouseover", function(e){
        //layer.setIcon(icons.iconSelected);
      //});
      //layer.on("mouseout", function(e){
        //layer.setIcon(icons.iconStable);
      //});
    },
    objectClickHandler(e){
      this.selObjectsStyles(e.target);
      console.log(e.target.feature.properties.id);
      const polyVertexes = Array.from(e.target.feature.geometry.coordinates[0][0]);
      polyVertexes.forEach(element => {
        element.reverse()
      });
      this.vertexes = polyVertexes
      console.log(JSON.stringify(this.vertexes));
    },
    selObjectsStyles(clickedLayer){
      if(this.prevLayerClicked){
        this.prevLayerClicked.setStyle({opacity: 1});
      }
      clickedLayer.setStyle({opacity: 0.3})
      this.prevLayerClicked = clickedLayer
    },
    getPolyInfo(){
      
    }
    
  },
  computed:{
    options (){
      return {
        onEachFeature: this.onEachFeatureFunction,
      };
    },
  },
  watch:{
    async prevLayerClicked(){
      if (this.prevLayerClicked){
        this.loading = true;
        this.showPopup = true;
        const selInfo = await getPolyData(this.prevLayerClicked.feature.properties.id)
        this.places = selInfo.places
        this.pop = selInfo.pop
        if(selInfo){
          this.loading = false;
        }
      }
      
      
    }
  },
  async created() {
    this.geojsonPoly = await getPoly();
  }
}
</script>

