export async function getPoly(){
    const url = "http://0.0.0.0:5000"
    const response = await fetch(url, {headers: {"access": "application/json", "Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}})
    
    //if(response.status == 200){
        return response.json();
    //}else{
        //return false
    //}
}