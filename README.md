

|  <image src="https://i.ibb.co/nm5bk8M/poly-image.jpg"></image> | <h2>Polygons</h2> This simple application allows you to display information about settlements and population in a certain area. The area is represented by a polygon that can be edited. |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
<h2> Installation </h2>
<ul>
    <li>Clone this repo and go to root/backend</li>
    <li>Rename the file "env-example" to ".env" and return to root</li>
    <li>Make sure ports 5432, 5000 and 8000 are not busy</li>
    <li>Then use the command <code>docker-compose up --build -d</code></li>
    <li>We'll have to wait a few minutes, then open the address in the browser: <code>localhost:8000</code></li>
</ul>

## Dependencies
### Database
<ul>
    <li>Postgres with PostGIS extensions</li>
</ul>

### Backend
<ul>
    <li>FastAPI</li>
</ul>

### Frontend
<ul>
    <li>Vue</li>
    <li>Leaflet</li>
</ul>
