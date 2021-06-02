<template>
    <v-text-field
    label="Номер телефона"
    type='tel'
    placeholder='+7 (999) 999-99-99'
    required
    outlined
    ref="tel"
    :value='phoneNumber'
    :rules="rules"
    @input='TelInput'
    @keydown="TelKeydown"
    @paste='onPhonePaste'
    ></v-text-field>
</template>

<script>
export default {
    name: 'Phone',

    props: {
        value: {
            required: true
        }
    },

    data: () => ({
        phoneNumber: null,
        rules: [
            value => (value.replace(/\D/g, '') || '').length <= 11 || 'Max 11 characters',
        ],
    }),

    watch: {
        phoneNumber() {
            this.$emit('input', this.phoneNumber.replace(/\D/g, ''))
        }
    },

    created() {
        this.phoneNumber = this.format(this.value)
    },

    methods: {
        format(tel) {
            if (tel == '' || tel == null) return ''

            tel = tel.replace(/\D/g, '')
            if (["7", "8", "9"].indexOf(tel[0]) > -1) {
                if (tel[0] == "9") tel = "7" + tel;
                var firstSymbols = (tel[0] == "8") ? "8" : "+7";
                var formattedInputValue = firstSymbols + " ";
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
            } else {
                formattedInputValue = '+' + tel.substring(0, 16);
            }

            return formattedInputValue
        },

        getInputNumbersValue(input) {
            return input.value.replace(/\D/g, '');
        },
        
        TelKeydown(e) {
            var inputValue = this.$refs.tel.$refs.input.value.replace(/\D/g, '');
            if (e.keyCode == 8 && inputValue.length == 1) {
                e.target.value = "";
            }
        },

        onPhonePaste (e) {
            var input = this.$refs.tel.$refs.input,
                inputNumbersValue = this.getInputNumbersValue(input);
            var pasted = e.clipboardData || window.clipboardData;
            if (pasted) {
                var pastedText = pasted.getData('Text');
                if (/\D/g.test(pastedText)) {
                    input.value  = inputNumbersValue;
                    this.phoneNumber = input.value;
                }
            }
        },

        TelInput() {
            var input = this.$refs.tel.$refs.input,
                inputNumbersValue = this.getInputNumbersValue(input),
                selectionStart = input.selectionStart;
                
            if (inputNumbersValue.length == 1 || inputNumbersValue.length == 0) {
                input.value = ''
                this.phoneNumber = input.value;
                return;
            }

            if (input.value.length != selectionStart) return;

            let formattedInputValue = this.format(inputNumbersValue)

            input.value = formattedInputValue;
            this.phoneNumber = input.value;
        },
    }
}
</script>

<style scoped>
</style>
