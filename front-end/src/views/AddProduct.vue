<template>
<div>
    <h1>Add Product</h1>
<select v-model="categoryid">
<option value="" disabled>Select Category</option>
    <option v-for="item in response" :value="item" :key="item.id">
      {{ item.category }}
    </option>
  </select><br>
    <input type="text" placeholder="Enter the ProductName" v-model="product_name"><br>
    <input type="text" placeholder="Enter the price" v-model="price"><br>
    <button @click="addcategory" class="btn">Add Product</button>
  </div>

</template>

<script>
export default {
name: 'AddProduct',
data(){
    return {
        response:[],
        categoryid: null,
        product_name: null,
        price: null,
    }
},
async mounted() {
    let response = await fetch('http://127.0.0.1:8000/getcategorys/')
    let category = await response.json()
    this.response = category
    console.warn(category)
},
methods: {
    async addcategory(){
        const requestOptions = {
        method: 'POST',
        body: JSON.stringify({ "category":this.categoryid.id,"product_name":this.product_name ,"price":this.price})
        };
        let response = await fetch('http://127.0.0.1:8000/addproduct/',requestOptions)
        let result = await response.json()
        console.log(result)
        if(result.success== true)
        {
            console.log(result)
            this.$router.push("/treeview");
        }
    }
}
}
</script>

<style>
input[type=text] {
  width: 35%;
  padding: 12px 15px;
  margin: 8px 0;
  box-sizing: border-box;
  border: 2px solid rgba(64, 228, 14, 0.808);
  border-radius: 4px;
} 
.btn {
  background-color: white;
  color: black;
  border: 2px solid #0dee3d; /* Green */
  border-radius: 4px;
  padding: 12px 28px;
  width: 175px;
  font-weight: bold;
}
.btn:hover {
  background-color: #0dee3d; /* Green */
  color: white;
}
.select-selected {
  background-color: rgb(30, 219, 30);
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
    color:#4CAF50;
}
</style>