<template>
  <p>file uploader</p>

  <q-uploader
    style="max-width: 300px"
    url="http://192.168.50.171:4444/upload"
    label="Upload images"
    auto-upload
    multiple
    max-files="4"
    accept=".jpg, image/*"
    @rejected="onRejected"
    @start="() => console.log('uploader: start')"
    @finish="() => console.log('uploader: finish')"
    @uploaded="onUploaded"
  />
  <p>Uploaded {{ uploadedFiles.length }} files:</p>
  <pre>{{ uploadedFiles }}</pre>
</template>

<script setup>
import { ref } from "vue";

defineOptions({
  name: "FileUpload",
});

const uploadedFiles = ref([]);

function onRejected(files) {
  console.log("rejected", files);
}

function onUploaded({ files }) {
  console.log("uploaded", files);
  uploadedFiles.value.push(files.map((file) => file.name));
}
</script>
