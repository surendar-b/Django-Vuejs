<template>
<h1>Add Category</h1>
  <div>
    <input type="text" placeholder="Enter the CategoryName" v-model="category"><br>
    <button @click="addcategory" class="button">Add Category</button>
  </div>

</template>

<script>
export default {
name: 'AddCategory',
data(){
    return {
        category: null,
    }
},
methods: {
    async addcategory(){
        const requestOptions = {
        method: 'POST',
        body: JSON.stringify({ "category":this.category })
        };
        let response = await fetch('http://127.0.0.1:8000/addcategory/',requestOptions)
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
.button {
  background-color: white;
  color: black;
  border: 2px solid #4CAF50; /* Green */
  border-radius: 4px;
  padding: 10px 24px;
  width: 175px;
  font-size: 18px;
  font-weight: bold;
}
.button:hover {
  background-color: #4CAF50; /* Green */
  color: white;
}

input[type=text] {
  width: 35%;
  padding: 12px 15px;
  margin: 8px 0;
  box-sizing: border-box;
  border: 2px solid rgba(115, 255, 0, 0.808);
  border-radius: 4px;
} 
h1{
    color:#4CAF50;
}
</style>