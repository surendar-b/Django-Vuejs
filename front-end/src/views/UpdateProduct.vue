<template>
  <div>
    <h1>Update Product</h1>
    <select v-model="id" @change="onChange">
    <option value="" disabled>Select Category</option>
    <option v-for="item in products" :value="item" :key="item.id">
      {{ item.product_name }}
    </option>
  </select><br>
  <input type="text" placeholder="categoryId" readonly v-model="categoryid" class="inptext"><br>
  <input type="text" placeholder="New Product Name" v-model="product_name" class="inptext"><br>
  <input type="number" placeholder="New Price" v-model="price" class="inptnum"><br>
    <button @click="update" class="btn3">Update Product</button>
  </div>
</template>

<script>
export default {
name : 'UpdateProduct',
data(){
    return{
        id:null,
        products:[],
        categoryid: null,
        product_name: null,
        price:null,
    }
},
async mounted() {
    let response = await fetch('http://127.0.0.1:8000/getproducts/')
    let product = await response.json()
    this.products = product
    console.warn(product)
},
methods: {
    async update(){
        const requestOptions = {
        method: 'PUT',
        body: JSON.stringify({ "category":this.categoryid,"product_name":this.product_name,"price":this.price })
        };
        let url = 'http://127.0.0.1:8000/update/product/'+this.id.id
        let response = await fetch(url,requestOptions)
        let result = await response.json()
        console.log(result)
        if(result.success==true)
        {
            //console.log(result)
            this.$router.push("/treeview");
        }
    },
    async onChange(){
        let url = 'http://127.0.0.1:8000/get/product/'+this.id.id
        let response = await fetch(url)
        let resp= await response.json()
        this.categoryid= resp.category
        this.product_name = resp.product_name
        this.price=resp.price
    }
}
}
</script>

<style>
.selects-sel {
  border: #f0e119;
  width: 100px;
  height: 40px;
  font-size: 12px;
}
.inptext[type=text] {
  width: 35%;
  padding: 12px 15px;
  margin: 8px 0;
  box-sizing: border-box;
  border: 2px solid rgba(255, 251, 0, 0.733);
  border-radius: 4px;
}
.inptnum[type=number] {
  width: 35%;
  padding: 12px 15px;
  margin: 8px 0;
  box-sizing: border-box;
  border: 2px solid rgba(255, 251, 0, 0.733);
  border-radius: 4px;
}
.btn3 {
  background-color: white;
  color: black;
  border: 2px solid #f1e210; /* Green */
  border-radius: 4px;
  padding: 12px 28px;
  width: 175px;
  font-weight: bold;
}
.btn3:hover {
  background-color: #f0e119; /* Green */
  color: white;
}

select {
        width: 470px;
        height: 35px;
        padding: 5px 35px 5px 5px;
        font-size: 18px;
      }
h1{
    color:#f1df3c;
}
</style>