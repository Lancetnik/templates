<template>
  <v-card>
    <v-card-title class="headline" :style="'color: white; background:' + color">
      Введите данные пользователя:
    </v-card-title>

    <v-card-text class="mt-4">
      <v-col>
        <v-row>
          <v-text-field
            v-model="email"
            label="Email"
            :rules="rule"
            :error="errors.email"
            :error-messages="errorsMessages.email"
            required
            type="email"
            class="p-2"
            append-icon="mdi-email"
          ></v-text-field>
        </v-row>

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
            @click:append="show1()"
            class="p-2"
            :type="pass_type1"
          ></v-text-field>
        </v-row>

        <v-row>
          <v-text-field
            v-model="confirmPassword"
            label="Confirm password"
            :rules="rule"
            :error="errors.confirmPassword"
            :error-messages="errorsMessages.confirmPassword"
            required
            append-icon="mdi-eye"
            @click:append="show2()"
            class="p-2"
            :type="pass_type2"
          ></v-text-field>
        </v-row>

        <v-row class="my-2" justify="center">
          <v-btn :color="color" dark width="200" @click="signUp()"
            >Регистрация</v-btn
          >
        </v-row>

        <v-row justify="center">
          <v-btn text :color="color" @click="$router.push({ name: 'SignIn' })">
            Войти
          </v-btn>
        </v-row>
      </v-col>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",

  data: function () {
    return {
      color: "rgba(10, 20, 255, 0.85)",
      pass_type1: "password",
      pass_type2: "password",
      rule: [(val) => (val || "").length > 0 || "This field is required"],
      errors: {
        email: false,
        login: false,
        password: false,
        confirmPassword: false,
      },
      errorsMessages: {
        email: null,
        login: null,
        password: null,
        confirmPassword: null,
      },

      login: null,
      email: null,
      phone: null,
      password: null,
      confirmPassword: null,
    };
  },

  methods: {
    show1() {
      if (this.pass_type1 === "password") this.pass_type1 = "text";
      else if (this.pass_type1 === "text") this.pass_type1 = "password";
    },

    show2() {
      if (this.pass_type2 === "password") this.pass_type2 = "text";
      else if (this.pass_type2 === "text") this.pass_type2 = "password";
    },

    signUp() {
      if (this.password === this.confirmPassword) {
        axios({
          url: `${this.$store.state.backendUrl}/auth/users/`,
          method: "POST",
          data: {
            login: this.login,
            password: this.password,
            email: this.email,
          },
        })
          .then((response) => {
            Object.keys(this.errors).forEach((e) => {
              this.errors[e] = false;
              this.errorsMessages[e] = null;
            });
            this.$router.push({ name: "SignIn" });
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
      } else {
		  this.errors.confirmPassword = true
		  this.errorsMessages.confirmPassword = 'Wrong password'
	  }
    },
  },
};
</script>


<style scoped>
</style>