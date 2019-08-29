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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
