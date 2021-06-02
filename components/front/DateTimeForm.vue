<template>
  <div style="display: flex">
    <v-col cols="8" class="py-0">
      <v-menu
        v-model="menu"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="date"
            :label="label"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker v-model="date" @input="menu = false" no-title>
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="
              date = '';
              menu = false;
            "
          >
            Clear
          </v-btn>
          <v-btn text color="primary" @click="menu = false"> Cancel </v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>

    <v-col class="py-0" align-self="center">
      <input class="ml-3 time" type="time" v-model="time" />
    </v-col>
  </div>
</template>

<script>
export default {
  name: "DateTimeField",

  props: {
    value: {
      required: true,
    },
    label: {
      required: false,
      default: "",
    },
  },

  data: () => ({
    menu: false,
    date: null,
    time: null,
  }),

  methods: {
    setDateTime(val) {
      if (val) {
        this.date = val.toISOString().substr(0, 10);

        let h = val.getHours();
        if (h < 10) h = "0" + h;

        let m = val.getMinutes();
        if (m < 10) m = "0" + m;

        this.time = h + ":" + m;
      }
    },
  },

  computed: {
    datetime() {
      let d = null;
      if (this.date) d = new Date(this.date);
      if (this.date && this.time) {
        let y, m, d = this.date.split("-");
        d = new Date(y, m-1, d, ...this.time.split(":"));
      }
      return d;
    },
  },

  created() {
    this.setDateTime(this.value);
  },

  watch: {
    datetime(val) {
      this.$emit("input", val);
    },
  },
};
</script>

<style scoped>
.time {
  font-size: 18px;
  cursor: pointer;
}

.time::-webkit-calendar-picker-indicator {
  color: white;
  cursor: pointer;
  display: none;
}
</style>