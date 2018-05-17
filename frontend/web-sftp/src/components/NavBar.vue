<template>
  <div id="nav-bar">
    <ul class="u-full-width">
      <li>Settings</li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "nav-bar"
  }
</script>

<style>
  #nav-bar {
    background-color: var(--primary-decoration-color);
  }

  #nav-bar ul {
    display: inline-block;
    margin-bottom: 0;
  }

  #nav-bar li {
    list-style-type: none;
    font-weight: bold;
    font-size: 2em;
    margin-bottom: 0;
    cursor: pointer;
    padding: 10px;
  }

  #nav-bar li:last-child {
    float: right;
  }
</style>
