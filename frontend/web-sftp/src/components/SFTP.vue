<template>
  <div id="sftp-container">
    <div id="sftp-client" class="six columns">
      <ul>
        <li>how i met your mother</li>
        <li>how i met your mother</li>
        <li>how i met your mother</li>
      </ul>
    </div>
    <div id="sftp-host" class="six columns">
      <ul>
        <li v-for="item in fileList">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
  import Api from './helpers/API';

  export default {
    name: "file-view",
    data() {
      return {
        fileList: []
      };
    },
    methods: {
      getFile() {
        Api.getHostContent()
          .then(res => {
            console.log(res);
          })
          .catch(res => {

          });
      }
    },
    mounted() {
      this.getFile();
    }
  }
</script>

<style>
  #sftp-container {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
  }

  #sftp-client {
    margin-right: 20px;
  }

  #sftp-host {
    margin-left: 20px;
  }

  #sftp-container ul {
    list-style-type: none;
    padding: 0;
  }

  #sftp-container li {
    padding: 10px;
    font-weight: bold;
    font-size: 1.2em;
    cursor: pointer;
    margin-bottom: 2px;
    box-shadow: 0 2px 3px rgba(0, 0, 0, .26);
    background-color: var(--secondary-color);
  }

  #sftp-container li:hover {
    background: var(--primary-color);
  }
</style>
