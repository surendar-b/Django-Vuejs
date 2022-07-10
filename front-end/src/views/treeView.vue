<template>
<div>
  <button @click="change" class="button2">Add Category</button>
  <button @click="deleteChange" class="button4">Detele Category</button>
  <button @click="UpdateChange" class="button3">Update Category</button>
  </div>
  <br>
  <div>
  <button @click="AddProduct" class="button2">Add Product</button>
  <button @click="DeleteProduct" class="button4">Delete Product</button>
  <button @click="UpdateProduct" class="button3">Update Product</button>
</div>
  <tree-table
          class="table"
          :columns="columns"
          :table-data="tableData" />
</template>

<script>
import TreeTable from 'vue-tree-table-component';
//import Vue from 'vue';
//import { ButtonPlugin } from '@syncfusion/ej2-vue-buttons';
//Vue.use(ButtonPlugin);
export default {
    name: 'DefaultTableTree',
    components: {
        TreeTable
        },
    data: function(){
      return {
        tableData: [],
        columns: [{label: 'Category', id: 'category'}, {label: 'Product Name', id: 'product_name'},{label: 'Price', id:'price'}]
      }
    },
     async mounted() {
        let response = await fetch('http://127.0.0.1:8000/getcategorys/')
        let category = await response.json()
        console.warn(category)
        var i=0
        for(i=0;i<category.length;i++)
        {
            let url='http://127.0.0.1:8000/getproduct/'+category[i].id
            let productResp = await fetch(url)
            let product = await productResp.json()
            if(product.length>0)
            {
                category[i].children=product
            }
            console.warn(category[i])
        }
        this.tableData=category
        console.log(this.tableData)    
    },
    methods: {
    change(){
      this.$router.push('/addcategory')
    },
    deleteChange(){
      this.$router.push('/deletecategory')
    },
    UpdateChange(){
      this.$router.push('/updatecategory')
    },
    AddProduct(){
      this.$router.push('/addproduct')
    },
    DeleteProduct(){
      this.$router.push('/deleteproduct')
    },
    UpdateProduct(){
      this.$router.push('/updateproduct')
    }
    }
  }
</script>

<style>
.table{
    width: 60%;
    margin: auto;
  }
.button2 {
  background-color: white;
  color: black;
  border: 2px solid #4CAF50; /* Green */
  border-radius: 4px;
  padding: 12px 28px;
  width: 150px;
  font-weight: bold;
}
.button3 {
  background-color: white;
  color: black;
  border: 2px solid #f3e410; /* Yellow */
  border-radius: 4px;
  padding: 12px 28px;
  width: 175px;
  font-weight: bold;
}
.button4 {
  background-color: white;
  color: black;
  border: 2px solid #c70404; /* Green */
  border-radius: 4px;
  padding: 12px 28px;
  width: 175px;
  font-weight: bold;
}
.button2:hover {
  background-color: #4CAF50; /* Green */
  color: white;
}
.button3:hover {
  background-color: #e9db16; /* Green */
  color: white;
}
.button4:hover {
  background-color: #f50909; /* Green */
  color: white;
}
</style>