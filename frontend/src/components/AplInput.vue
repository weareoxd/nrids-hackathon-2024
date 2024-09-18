<template>
  <label ref="root" class="apl-input" :class="$props.class">
    <span v-if="label" class="label"
      >{{ label }}
      <span v-if="tooltip" class="tooltip q-px-sm">
        <q-icon><!-- <tooltip-icon /> -->[Icon]</q-icon>

        <q-tooltip>{{ tooltip }}</q-tooltip>
      </span>
    </span>

    <q-input
      v-bind="$attrs"
      v-model="model"
      filled
      :label="undefined"
      :prefix="$props.prefix"
    >
      <template v-if="datePicker" #append>
        <div
          class="bg-primary flex flex-center q-pa-xs cursor-pointer date-picker-icon"
        >
          <q-icon color="black" size="16px"
            ><!-- <calendar-icon /> -->[Icon]</q-icon
          >
        </div>
      </template>
    </q-input>

    <q-popup-proxy
      v-if="datePicker"
      :target="$refs.root"
      transition-show="scale"
      transition-hide="scale"
    >
      <q-date v-model="model" minimal no-unset mask="YYYY-MM-DD">
        <div class="row items-center justify-end">
          <q-btn v-close-popup label="Close" color="primary" flat />
        </div>
      </q-date>
    </q-popup-proxy>
  </label>
</template>

<script setup>
// import TooltipIcon from 'components/icons/tooltip.vue';
// import CalendarIcon from 'components/icons/calendar.vue';

defineOptions({
  name: "AplInput",
  inheritAttrs: false,
});

const model = defineModel({
  // allow any kind of v-model for now
  type: [String, Number, Date, Boolean, Object, Array],
});

defineProps({
  // "prefix" is a reserved word,
  // so it can't be passed through from the parent without throwing warnings
  // define here as a prop to avoid the warning.
  prefix: {
    type: String,
    required: false,
    default: "",
  },

  class: {
    type: String,
    default: "",
  },

  datePicker: {
    type: Boolean,
    default: false,
  },

  // display the label above the input, not in the default floating position
  label: {
    type: String,
    default: "",
  },

  tooltip: {
    type: String,
    default: "",
  },
});
</script>

<style lang="scss">
.apl-input {
  display: flex;
  flex-direction: column;

  .label {
    font-size: 0.875rem;
    display: block;
    margin-bottom: 4px;
    font-weight: 700;
  }

  .q-field {
    .q-field__control {
      height: 3rem;
      background-color: #b0b0b0;
      padding: 0;
      border: 1px solid #707070;
      border-radius: 4px;
      transition: border-color $generic-hover-transition,
        background-color $generic-hover-transition;

      // disable border animation
      &:after,
      &:before {
        display: none;
      }
    }

    // text area: dynamic height
    &.q-textarea {
      .q-field__control {
        height: auto;

        textarea {
          // Quasar adds 2px vertical padding
          padding-top: 14px;
          padding-bottom: 14px;

          // add 2px spacing on the right for the scrollbar/resize handle
          margin-right: 2px;
        }
      }
    }
  }

  .q-field__prefix,
  .q-field__suffix,
  input,
  textarea {
    padding: 0 16px;
    margin: 0;
    font-size: 1rem;
    line-height: normal;

    &::placeholder {
      color: #b0b0b0;
      font-style: italic;
    }
  }

  .q-field__prefix {
    padding-right: 0;
  }
  .q-field__suffix {
    padding-left: 0;
  }

  // icon slot (for eg. date picker)
  .q-field__append {
    font-size: 1.5rem;
    height: auto;
    padding: 0 16px 0 0;
  }

  .q-field--highlighted .q-field__control {
    border-color: $primary;
  }

  &:has(input:placeholder-shown) {
    .q-field__prefix,
    .q-field__suffix {
      color: #b0b0b0;
    }
  }

  .date-picker-icon {
    border-radius: 2px;
  }
}
</style>
