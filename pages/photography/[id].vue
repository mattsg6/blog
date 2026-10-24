<template>
    <v-container fluid class="px-3 mt-5">
        <v-row>
            <v-col cols="12">
                <div class="d-flex flex-column ga-4">
                    <span class="text-body-1 font-weight-bold">{{ photoData?.title }}</span>
                    <span class="text-body-2">{{ photoData?.description }}</span>
                </div>
            </v-col>
        </v-row>
        <v-row v-if="images?.length > 0">
            <v-col v-for="n of images.length" cols="12" md="6">
                <img class="image-box" @click="openDialog(n - 1)" :src="images[n - 1]" width="100%" />
            </v-col>
        </v-row>
        <v-dialog v-model="dialog" width="auto" height="90vh" @keydown.right="moveRight" @keydown.left="moveLeft">
            <v-card width="75vw" height="90vh">
                <div class="pa-5 d-flex ga-3 align-center justify-center h-100">
                    <v-icon @click="moveLeft" icon="mdi-chevron-left" class="mx-5"></v-icon>
                    <img :src="images[currImageIndex]" style="min-width: 90%;" />
                    <v-icon @click="moveRight" icon="mdi-chevron-right" class="mx-5"></v-icon>
                </div>
                <v-icon @click="dialog = false" icon="mdi-close" size="small"
                    style="position: absolute; top: 5px; right:5px;"></v-icon>
            </v-card>
        </v-dialog>
    </v-container>
</template>
<script setup>
const dialog = ref(false);
const route = useRoute();
const pageId = route.params.id;
const photoData = ref({});
const images = ref([]);
await useFetch(`/images/photography/${pageId}/meta.json`).then(({ data }) => {
    if (!data.value?.title) {
        throw createError({
            status: 404,
            statusText: 'Photo collection not found',
            message: 'This collection probably does not exist. Weird...',
            fatal: true
        });
    }
    photoData.value = data.value;
    images.value = data.value.photos.map(i => `/images/photography/${pageId}/${i}`);
})
const currImageIndex = ref("");
function openDialog(index) {
    if (window.innerWidth <= 959) {
        return;
    }
    currImageIndex.value = index;
    dialog.value = true;
}

function moveLeft() {
    if (currImageIndex.value === 0) {
        currImageIndex.value = images.value.length - 1;
    } else {
        currImageIndex.value -= 1;
    }
}

function moveRight() {
    if (currImageIndex.value === images.value.length - 1) {
        currImageIndex.value = 0;
    } else {
        currImageIndex.value += 1;
    }
}
</script>
<style scoped>
.image-box:hover {
    cursor: zoom-in;
}
</style>