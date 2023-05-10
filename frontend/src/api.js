export async function getPoly(){
    const url = "http://0.0.0.0:5000"
    const response = await fetch(url, {headers: {"access": "application/json", "Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}})
    
    //if(response.status == 200){
        return response.json();
    //}else{
        //return false
    //}
}
export async function getPlaces(){
    const url = "http://0.0.0.0:5000/places"
    const response = await fetch(url, {headers: {"access": "application/json", "Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}})
    
    //if(response.status == 200){
        return response.json();
    //}else{
        //return false
    //}
}
export async function getPolyData(fid){
    const url = `http://0.0.0.0:5000/poly_info/${fid}`
    const response = await fetch(url, {headers: {"access": "application/json", "Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}})
    
    //if(response.status == 200){
        return response.json();
    //}else{
        //return false
    //}
}