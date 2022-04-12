<template>
  <v-text-field
    label="Номер телефона"
    type="tel"
    placeholder="+7 (999) 999-99-99"
    required
    outlined
    ref="tel"
    :value="phoneNumber"
    :rules="rules"
    @input="phoneInput"
    @keydown="phoneKeydown"
  ></v-text-field>
</template>

<script>
const clearSymbols = (val) => (val.replace(/\D/g, ''))
const isValid = (value) => (
    clearSymbols(value).length === 11 && /^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$/.test(value) ||
    clearSymbols(value).length === 11 && /^8 \(\d{3}\) \d{3}-\d{2}-\d{2}$/.test(value)
)

export default {
    props: {
        value: {
            required: true
        }
    },

    data: () => ({
        phoneNumber: null,
        rules: [
            value =>  clearSymbols(value).length < 11 || isValid(value) || 'Wrong format',
        ],
    }),

    watch: {
        phoneNumber() {
            this.$emit('input', clearSymbols(this.phoneNumber))
        }
    },

    created() {
        this.phoneNumber = this.formatPhone(this.value)
    },

    methods: {
        formatPhone(tel) {
            if (tel == '' || tel == null) return ''

            var firstSymbols, formattedInputValue;
            if (["7", "8", "9"].indexOf(tel[0]) > -1) {
                if (tel[0] == "9") tel = "7" + tel;
                firstSymbols = (tel[0] == "8") ? "8" : "+7";
                formattedInputValue = firstSymbols + " ";
            } else {
                firstSymbols = '+7 (9';
                formattedInputValue = firstSymbols + tel[0]
            }

            if (tel.length > 1) {
                formattedInputValue += '(' + tel.substring(1, 4);
            }
            if (tel.length >= 5) {
                formattedInputValue += ') ' + tel.substring(4, 7);
            }
            if (tel.length >= 8) {
                formattedInputValue += '-' + tel.substring(7, 9);
            }
            if (tel.length >= 10) {
                formattedInputValue += '-' + tel.substring(9, 11);
            }

            return formattedInputValue
        },
        
        phoneKeydown(e) {
            var inputValue = clearSymbols(this.$refs.tel.$refs.input.value);
            if (e.keyCode === 8 && inputValue.length === 1) {
                this.phoneNumber = "";
            }
        },

        phoneInput() {
            const input = this.$refs.tel.$refs.input,
                inputNumbersValue = clearSymbols(input.value),
                selectionStart = input.selectionStart,
                value = input.value,
                cleared_value = value.replace(/[^0-9()+\- ]/g, '');

            if (value !== cleared_value) {
                this.phoneNumber = cleared_value
                input.selectionStart = selectionStart - 1
                input.selectionEnd = selectionStart - 1
            }

            if (!inputNumbersValue) {
                this.phoneNumber = ""
                if (this.phoneNumber === "+") this.phoneNumber = "+"
                else this.phoneNumber = ""
                return
            } else {
                const formattedInputValue = this.formatPhone(inputNumbersValue)

                if (selectionStart === input.value.length) {
                    this.phoneNumber = formattedInputValue
                    input.selectionStart = formattedInputValue.length
                }

                const ph = `+${inputNumbersValue}`
                if (ph.length > 11) {
                    this.phoneNumber = this.formatPhone(inputNumbersValue)
                } else if (isValid(formattedInputValue)) {
                    this.phoneNumber = this.formatPhone(inputNumbersValue)
                    this.phone = ph
                } else {
                    this.phone = ""
                }
            }
        }
    }
}
</script>
