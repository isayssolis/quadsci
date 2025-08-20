<script>
export default {
  data(){
    return{
      results:[],
      isLoading:false,
      error: null,
    }
  },
  methods:{
    loadData(){
      this.isLoading = true;
      this.error = null;
      fetch('http://127.0.0.1:5000/api/rockets')
          .then((res)=>{
            if(res.ok){
              return res.json();
            }else{
              // catch not 200  code!
              throw  new Error('Fetch failed, please try again.');
            }
          })
          .then(data => {
            this.isLoading = false;
            this.results = data;
            console.log(data)
          })
          .catch(error=>{
            this.isLoading = false;
            this.error = error.message;
            console.log(error.message)
          })
    }
  },
  mounted(){
    this.loadData();
  }
};
</script>

<template>
  <div>
    <div v-if="isLoading"><Spinner /></div>
    <div v-else-if="!isLoading && error" >
      <Alert v-bind:text="error"></Alert>
    </div>
    <h1 v-else >Rockets</h1>
  </div>
</template>

<style scoped>

</style>