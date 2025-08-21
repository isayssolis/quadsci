<script>

</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-white">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">SPACE X TEST</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link ">HOME</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/rockets" class="nav-link ">ROCKETS</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/launches" class="nav-link ">LAUNCHES</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/starlink" class="nav-link ">STARLINK</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
  a.active{ text-decoration: underline}
  .bg-light{background-color: #dcdcdc !important; }
</style>
