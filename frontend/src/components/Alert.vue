<script>
export default {
  props: [
      'text'
  ]
}
</script>


<template>
  <div class="alert alert-danger" role="alert">
    {{this.text}}
  </div>
</template>