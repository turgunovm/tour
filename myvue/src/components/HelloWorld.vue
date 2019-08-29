<template>
  <div class="hello">
    <button @click="getProduct">Check</button>
    <ul v-if="product">
      <li v-for="post in product">
        {{post.title}}
      </li>
    </ul>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'HelloWorld',
  data () {
    return {
      product: []
    }
  }, 
  methods: {
    getProduct(){
        $.ajax({
          url: 'http://127.0.0.1:8000/api/articles/',
          type: 'GET',
          success:(response)=>{
            console.log(response.data)
            this.product = response.data
          }
      })
    }
    
  }
}
</script>

<style scoped>

</style>
