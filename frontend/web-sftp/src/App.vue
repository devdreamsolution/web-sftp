<template>
  <div id="app">
    <nav-bar/>
    <quick-connect-bar/>
    <client/>
  </div>
</template>

<script>
  import QuickConnectBar from "./components/QuickConnectBar";
  import NavBar from "./components/NavBar";
  import Client from "./components/Client";

  export default {
    name: 'app',
    components: {
      QuickConnectBar,
      Client,
      NavBar
    },
    data() {
      return {}
    }
  }
</script>

<style>
  :root {
    --primary-decoration-color: #00C853;
    --secondary-decoration-color: #00BFA5;

    /*Light colors*/
    --primary-color: #F5F5F5;
    --secondary-color: #FFFFFF;

    /*Dark colors*/
    /*--primary-color: #212121;*/
    /*--secondary-color: #616161;*/
  }

  body {
    font-size: 14px;
    background-color: var(--primary-color);
    margin: 0;
  }

  ::-webkit-scrollbar {
    width: 4px;
    height: 4px;
  }

  ::-webkit-scrollbar-thumb {
    background-color: var(--primary-decoration-color);
  }

  .content-center,
  .center {
    margin-right: auto;
    margin-left: auto;
  }

  .content-center {
    width: 90%;
  }
</style>
