<template>
  <v-card>
    <v-card-title class="headline" :style="'color: white; background:' + color">
      Введите данные пользователя:
    </v-card-title>

    <v-card-text class="mt-4">
      <v-col>
        <v-row>
          <v-text-field
            v-model="login"
            label="Login"
            :rules="rule"
            :error="errors.login"
            :error-messages="errorsMessages.login"
            required
            class="p-2"
            append-icon="mdi-account"
          ></v-text-field>
        </v-row>

        <v-row>
          <v-text-field
            v-model="password"
            label="Password"
            :rules="rule"
            :error="errors.password"
            :error-messages="errorsMessages.password"
            required
            append-icon="mdi-eye"
            @click:append="show()"
            class="p-2"
            :type="pass_type"
          ></v-text-field>
        </v-row>

        <v-row class="my-2 justify-content-center">
          <span v-if="errorsMessages.non_field_errors" style="color: red">{{
            errorsMessages.non_field_errors[0]
          }}</span>
        </v-row>

        <v-row class="my-2" justify="center">
          <v-btn :color="color" dark width="200" @click="log_in()">Войти</v-btn>
        </v-row>

        <v-row justify="center">
          <v-btn text :color="color" @click="$router.push({ name: 'SignUp' })">
            Регистрация
          </v-btn>
        </v-row>
      </v-col>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",

  data: () => ({
    color: "rgba(10, 20, 255, 0.85)",
    pass_type: "password",
    rule: [(val) => (val || "").length > 0 || "This field is required"],
    errors: {
      login: false,
      password: false,
    },
    errorsMessages: {
      login: null,
      password: null,
      non_field_errors: null,
    },

    login: null,
    password: null,
  }),

  methods: {
    show() {
      if (this.pass_type === "password") this.pass_type = "text";
      else if (this.pass_type === "text") this.pass_type = "password";
    },

    log_in() {
      axios({
        method: "POST",
        url: `${this.$store.state.backendUrl}/auth/token/login/`,
        data: {
          login: this.login,
          password: this.password,
        },
      })
        .then((response) => {
          let token = response.data.auth_token;
          this.$store.dispatch("setToken", token);

          Object.keys(this.errors).forEach((e) => {
            this.errors[e] = false;
            this.errorsMessages[e] = null;
          });

          axios({
            method: "GET",
            url: `${this.$store.state.backendUrl}/auth/users/me/`,
            headers: {
              Authorization: `Token ${token}`,
            },
          }).then((r) => {
            this.$store.dispatch("setMe", r.data);
            this.$router.push({ name: "main" });
          });
        })
        .catch((error) => {
          Object.keys(this.errors).forEach((e) => {
            this.errors[e] = false;
            this.errorsMessages[e] = null;
          });

          let errors = error.response.data;
          Object.keys(errors).forEach((e) => {
            this.errors[e] = true;
            this.errorsMessages[e] = errors[e];
          });
        });
    },
  },
};
</script>

<style scoped>
</style>
