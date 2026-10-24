<template>
    <v-container fluid class="px-3 mt-5">
        <v-row>
            <v-col cols="12" class="pt-0 py-2">
                <span class="text-h5">Photography</span>
            </v-col>
        </v-row>
        <v-row>
            <v-col v-if="photos.length" v-for="photo of photos" cols="12" md="6">
                <v-card :to="`/photography/${photo.id}`" variant="outlined" hover>
                    <div class="d-flex justify-center flex-column pa-3 ga-1">
                        <img :src="photo.img" width="100%" />
                        <span class="text-body-2">{{ photo.title }}</span>
                    </div>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script setup>
const { data } = await useFetch("/data/photography.json");
const photos = computed(() => data.value)
</script>
<style scoped>
.v-card {
    text-decoration: none !important;
}
</style>
