<template>
  <div id="quick-connect-bar-container" class="u-full-width">
    <div id="quick-connect-bar" class="content-center">
      <span>Host:</span>
      <input type="text" placeholder="Host">
      <span>Username:</span>
      <input type="text" placeholder="Username">
      <span>Password:</span>
      <input type="password" placeholder="Password">
    </div>
  </div>
</template>

<script>
  export default {
    name: "quick-connect-bar"
  }
</script>

<style>
  #quick-connect-bar-container {
    background: var(--secondary-color);
  }

  #quick-connect-bar {
    display: block;
  }

  #quick-connect-bar span {
    font-weight: bold;
    margin-left: 30px;
  }

  #quick-connect-bar span:first-child {
    margin-left: 0;
  }

  #quick-connect-bar input {
    margin: 15px 0px 15px 0;
  }
</style>
