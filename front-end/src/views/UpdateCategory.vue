<template>
  <div>
    <h1>Update Category</h1>
    <select v-model="id">
    <option value="" disabled>Select Category</option>
    <option v-for="item in category" :value="item" :key="item.id">
      {{ item.category }}
    </option>
  </select><br>
  <input type="text" placeholder="New Category Name" v-model="categoryName" class="inpt"><br>
    <button @click="update" class="btn2">Update Category</button>
  </div>
</template>

<script>
export default {
name : 'DeleteCategory',
data(){
    return{
        id:null,
        category:[],
        categoryName: null,
    }
},
async mounted() {
    let response = await fetch('http://127.0.0.1:8000/getcategorys/')
    let category = await response.json()
    this.category = category
    console.warn(category)
},
methods: {
    async update(){
        const requestOptions = {
        method: 'PUT',
        body: JSON.stringify({ "category":this.categoryName })
        };
        let url = 'http://127.0.0.1:8000/update/category/'+this.id.id
        let response = await fetch(url,requestOptions)
        let result = await response.json()
        // console.log(result)
        if(result.success==true)
        {
            //console.log(result)
            this.$router.push("/treeview");
        }
    }
}
}
</script>

<style>
.select-selects {
  border: #f0e119;
  width: 100px;
  height: 40px;
  font-size: 12px;
}
.inpt[type=text] {
  width: 35%;
  padding: 12px 15px;
  margin: 8px 0;
  box-sizing: border-box;
  border: 2px solid rgba(255, 251, 0, 0.733);
  border-radius: 4px;
}
.btn2 {
  background-color: white;
  color: black;
  border: 2px solid #f1e210; /* Green */
  border-radius: 4px;
  padding: 12px 28px;
  width: 175px;
  font-weight: bold;
}
.btn2:hover {
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
  color:#e7d918;
}
</style>