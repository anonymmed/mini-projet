<template>
  <!-- Material form login -->
  <div class="container">
    <div class="col-lg-10 col-lg-offset-5">
    <p class="h4 text-center mb-4">Sign in</p>
    <div class="grey-text">
      <mdb-input label="Your username" icon="envelope" v-model="username" type="text"/>
      <mdb-input label="Your password" icon="lock" v-model="password" type="password"/>
    </div>
    <div class="text-center">
      <mdb-btn v-on:click="login">Login</mdb-btn>
    </div>
      </div>
    </div>
  <!-- Material form login -->
</template>
<script>
  import { mdbInput, mdbBtn } from 'mdbvue';
  import axios from 'axios';

  export default {
    name: 'Login',
    data:()=> ({
      username : '',
      password: ''
    }),
    components: {
      mdbInput,
      mdbBtn
    },
    methods: {
      login: function () {
        axios.post('http://localhost:8080/api-token-auth/',
                {
                  "username": this.username,
                  "password": this.password,
                }).then((res) => {
                  if (res.data.token) {
                    localStorage.setItem('token', res.data.token);
                    localStorage.setItem('id', res.data.id);
                              this.$router.push('Dashboard');

                  }
        }).catch((err) => {
          if (err) {
            throw err;
          }
        });
      }
    }
  }
</script>

<style scoped>

</style>