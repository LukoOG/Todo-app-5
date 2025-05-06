
//to implement
export async function load({ fetch }){
    let res = await fetch("http://127.0.0.1:8000/api/list")

    let data = await res.json()
    return{
        todos: data
    }
}