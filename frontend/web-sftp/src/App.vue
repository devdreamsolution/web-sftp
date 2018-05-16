<template>
  <div id="app">
    <nav-bar/>
    <sftp/>
  </div>
</template>

<script>
  import NavBar from "./components/NavBar";
  import SFTP from "./components/SFTP";

  export default {
    name: 'app',
    components: {
      NavBar,
      'sftp' : SFTP
    },
    data() {
      return {}
    }
  }
</script>

<style>
  :root {
    --primary-color: #F5F5F5;
    --secondary-color: #FFFFFF;
  }

  body {
    font-size: 14px;
    background-color: var(--primary-color);
  }

  .half-width {
    width: 50%;
  }
</style>
