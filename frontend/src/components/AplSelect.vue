<template>
  <label ref="root" class="apl-select" :class="$props.class">
    <span v-if="label" class="label"
      >{{ label }}
      <span v-if="tooltip" class="tooltip q-px-sm">
        <q-icon><!-- <tooltip-icon /> -->[icon]</q-icon>

        <q-tooltip>{{ tooltip }}</q-tooltip>
      </span>
    </span>

    <q-select
      v-model="model"
      filled
      v-bind="$attrs"
      popup-content-class="apl-select-popup"
    ></q-select>

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
// import TooltipIcon from "components/icons/tooltip.vue";

defineOptions({
  name: "AplSelect",
  inheritAttrs: false,
});

const model = defineModel({
  // allow any kind of v-model for now
  type: [String, Number, Date, Boolean, Object, Array],
});

defineProps({
  datePicker: {
    type: Boolean,
    default: false,
  },

  class: {
    type: String,
    default: "",
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
.apl-select {
  display: flex;
  flex-direction: column;
  font-size: 1rem;

  .label {
    font-size: 0.875rem;
    display: block;
    margin-bottom: 4px;
    font-weight: 700;
  }

  .q-field {
    height: 3rem;

    .q-field__control {
      height: 100%;
      min-height: auto;
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

      .q-field__native {
        padding: 0 16px;
        min-height: auto;
      }
    }
  }

  // icon slot (for the dropdown arrow))
  .q-field__append {
    font-size: 1.5rem;
    height: auto;
    padding: 0 16px 0 0;
  }

  .q-field--highlighted .q-field__control {
    border-color: $primary;
  }
}

// dropdown list (elsewhere in the DOM)
.apl-select-popup {
  box-shadow: none;
  border: 1px solid $primary;

  .q-item {
    background-color: #404040;

    .q-focus-helper {
      opacity: 0.1 !important;
    }

    &.q-item--active {
      color: #ffffff;
      background-color: #606060;
    }
  }
}
</style>
