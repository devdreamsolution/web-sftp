<template>
  <div id="sftp-container" class="content-center">
    <div id="sftp-client">
      <p>{{ clientPath }}</p>
      <ul @click="toggleActive">
        <li>Testing row</li>
        <li>Testing row</li>
        <li>Testing row</li>
      </ul>
    </div>
    <div id="sftp-host">
      <p>{{ hostPath }}</p>
      <ul @click="toggleActive">
        <!--<li v-for="item in fileList">{{ item }}</li>-->
        <li>Testing row</li>
        <li>Testing row</li>
        <li>Testing row</li>
      </ul>
    </div>
  </div>
</template>

<script>
  import Api from './helpers/API';

  export default {
    name: "client",
    data() {
      return {
        fileList: [],
        clientPath: '/home/user',
        hostPath: '/files'
      };
    },
    methods: {
      getFile() {
        Api.getHostContent()
          .then(res => {
            this.fileList = res;
          })
          .catch(res => {

          });
      },
      toggleActive(event) {
        let el = event.target;
        el.classList.contains('active') ? el.classList.remove('active') : el.classList.add('active');
      }
    },
    mounted() {
      // this.getFile();
    }
  }
</script>

<style>
  #sftp-container {
    display: flex;
    margin-top: 20px;
  }

  #sftp-container > div {
    flex-grow: 1;
    flex-basis: 0;
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
    overflow-y: scroll;
    overflow-x: hidden;
    max-height: 75vh;
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

  #sftp-container p {
    font-size: 1.4em;
    font-weight: bold;
    margin-bottom: 0;
  }

  #sftp-container li.active {
    background: var(--secondary-decoration-color);
    color: white;
  }
</style>
