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
        :lat-lng="vertex"
        :icon="vertexIcon"
        :draggable="true"
        @dragend="vertexDragEnd(index, $event.target)">
      </l-marker>
    </l-map>
    <template v-if="errorMsg">
      <div class="app_log">
        <span class="logErr">{{ errorMsg }}</span>
      </div>
    </template>
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
import { LMap, LTileLayer, LGeoJson, LMarker, } from 'vue2-leaflet';
import { icon } from "leaflet";
import { getPoly, getPolyData, updatePoly } from './api.js';
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
      wscon: null,
      showPoly: true,
      geojsonPoly: null,
      geojsonPoints: null,
      showPopup: false,
      prevLayerClicked: null,
      selectedPolyId: null,
      loading: false,
      places: null,
      pop: null,
      vertexes: null,
      errorMsg: null,
      vertexIcon: icon({
        iconUrl: 'vertex-icon.png',
        iconSize: [10, 10],
      }),
    }
  },
  methods: {
    onEachFeatureFunction(feature, layer) {
      layer.on({
        click: this.objectClickHandler
      });
    },
    objectClickHandler(e){
      //change poly style block
      this.selObjectsStyles(e.target);
      //create vertexes block
      this.createVertexes(e.target)
    },
    createVertexes(polygon){
      let polyVertexes = polygon.feature.geometry.coordinates[0][0].slice(0, -1);
      this.selectedPolyId = polygon.feature.properties.id
      let newVertexes = []
      polyVertexes.forEach(element => {
        newVertexes.push([...element].reverse())
        
      });
      this.vertexes = newVertexes;
    },
    async vertexDragEnd(index, vertex){
      let result = await updatePoly(this.selectedPolyId, index, vertex.getLatLng());
      if(result){
        await this.intersInfo();
      }else{
        this.errorMsg = "Something went wrong! Please try again later..."
      }
    },
    selObjectsStyles(clickedLayer){
      if(this.prevLayerClicked){
        this.prevLayerClicked.setStyle({opacity: 1});
      }
      clickedLayer.setStyle({opacity: 0.3})
      this.prevLayerClicked = clickedLayer
    },
    async getPolygons(){
        let polygons = await getPoly();
        if(polygons){
          this.geojsonPoly = polygons;
        }else{
          this.errorMsg = "Something went wrong! Please try again later..."
        }
    },
    async intersInfo(){
      this.loading = true;
      this.showPopup = true;
      const selInfo = await getPolyData(this.prevLayerClicked.feature.properties.id)
      this.places = selInfo.places
      this.pop = selInfo.pop
      if(selInfo){
        this.loading = false;
      }else{
        this.errorMsg = "Something went wrong! Please try again later..."
        this.loading = false;
      }
    },
    
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
        await this.intersInfo();
      }
    }
  },
  async created() {
    this.wscon = new WebSocket("ws://0.0.0.0:5000/ws")
    this.wscon.onmessage = async (message) => {
      this.geojsonPoly = JSON.parse(message.data);
    }
  },
}
</script>

