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
    </l-map>
    <template v-if="showPopup">
      <div class="popup">

      </div>
    </template>
  </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson } from 'vue2-leaflet';
import { getPoly } from './api.js';
import 'leaflet/dist/leaflet.css';

export default {
  name: 'App',
  components: {
    'l-map': LMap,
    'l-tile-layer': LTileLayer,
    'l-geo-json': LGeoJson,
  },
  data() {
    return {
      showPoly: true,
      geojsonPoly: null,
      geojsonPoints: null,
      showPopup: false,
      prevLayerClicked: null
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
    },
    selObjectsStyles(clickedLayer){
      if(this.prevLayerClicked){
        this.prevLayerClicked.setStyle({opacity: 1});
      }
      clickedLayer.setStyle({opacity: 0.3})
      this.prevLayerClicked = clickedLayer
    },
    getPolyInfo(id){
      
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
    prevLayerClicked(){
      if (this.prevLayerClicked){
        this.showPopup = true;
      }
    }
  },
  async created() {
    this.geojsonPoly = await getPoly();
  }
}
</script>

