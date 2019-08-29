<template>
  <div class="hello">
    <button @click="getProduct">Check</button>
     <h1>lorem3 </h1>
    <ul v-if="product">
      <li v-for="post in product">
          {{post.title}}
      </li>
    </ul>
  </div>
</template>

<script>
import $ from 'jquery'
import axios from 'axios';
export default {
  name: 'HelloWorld',
  data(){
    return {
      product: ''
    }
  },
  methods: {
    getProduct: function(){
      axios
      .get('http://127.0.0.1:8000/api/articles/')
      .then(response => (this.product = response));
    }
   
  } 
  // methods: {
  //   getProduct(){
  //       $.ajax({
  //         url: 'http://127.0.0.1:8000/api/articles/',
  //         type: 'GET',
  //         console.log(response.data)
  //         success:(response)=>{
  //           console.log(response.data)
  //           this.product = response.data

  //         }
  //     })
  //   }
    
  // },
    
}
</script>

<style scoped>

</style>
