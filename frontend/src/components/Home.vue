<script>
import CircularPlot from "@/components/CircularPlot.vue";
export default {
  components: {CircularPlot},
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
      fetch('https://flask-test1-dun.vercel.app/api/dashboard')
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
  <div class="container">
    <div class="row">
      <div v-if="isLoading"><Spinner /></div>
      <div v-else-if="!isLoading && error" >
        <Alert v-bind:text="error"></Alert>
      </div>
      <div v-else >
        <h1>Ships</h1>
        <CircularPlot v-bind:data="results.ships"></CircularPlot>
      </div>
    </div>
  </div>
</template>
