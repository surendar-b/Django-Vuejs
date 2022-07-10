<template>
  <div>
    <h1>Delete Product</h1>
    <select v-model="id">
    <option value="" disabled>Select Product</option>
    <option v-for="item in products" :value="item" :key="item.id">
      {{ item.product_name }}
    </option>
  </select><br><br>
    <button @click="deletes" class="btn1">Delete Product</button>
  </div>
</template>

<script>
export default {
name : 'DeleteProduct',
data(){
    return{
        id:null,
        products:[],
    }
},
async mounted() {
    let response = await fetch('http://127.0.0.1:8000/getproducts/')
    let product = await response.json()
    this.products = product
    console.warn(product)
},
methods: {
    async deletes(){
        const requestOptions = {
        method: 'DELETE'
        }
       // console.log(this.id.id)
        let url = 'http://127.0.0.1:8000/delete/product/'+this.id.id
        //console.log(url)
        let response = await fetch(url,requestOptions)
        let result = await response.json()
        // console.log(result)
        if(result=="Product deleted succesfully")
        {
            //console.log(result)
            this.$router.push("/treeview");
        }
    }
}
}
</script>

<style>
.btn1 {
  background-color: white;
  color: black;
  border: 2px solid #c70404; /* Green */
  border-radius: 4px;
  padding: 12px 28px;
  width: 175px;
  font-weight: bold;
}
.btn1:hover {
  background-color: #f50909; /* Green */
  color: white;
}
.select-select {
  background-color: rgb(228, 8, 8);
  width: 100px;
  height: 40px;
  font-size: 12px;
}
select {
        width: 470px;
        height: 35px;
        padding: 5px 35px 5px 5px;
        font-size: 18px;
      }
h1{
    color:#f50909;
}
</style>