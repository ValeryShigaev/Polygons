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
       :geojson="geojsonPoly">

      </l-geo-json>
    </l-map>
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
    }
  },
  methods: {
    
    
  },

  async created() {
    this.geojsonPoly = await getPoly();
  }
}
</script>

