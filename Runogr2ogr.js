var ogr2ogr = require('ogr2ogr')

ogr2ogr('HE_HighwayBoundary_v3_3_1.shp').exec(function(er, data) {
  if (er) console.error(er)
  console.log(data)
})

ogr2ogr -f GeoJSON -t_srs crs:84 "HE_HighwayBoundary_v3_3_1.geojson" "HE_HighwayBoundary_v3_3_1.shp"
