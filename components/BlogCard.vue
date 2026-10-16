<template>
    <v-card :to="`/post/${id}`" variant="outlined" hover class="w-100 h-100">
        <div v-if="isLatest" class="d-flex align-center pa-3">
            <div class="d-flex flex-column">
                <div id="card-title" class="px-2 pt-2">
                    <span class="text-h6">{{ title }}</span>
                </div>
                <div id="card-title" class="px-2">
                    <span class="text-caption">{{ date }}</span>
                </div>
                <div id="card-text" class="px-2">
                    <span class="text-body-2">{{ description }}</span>
                </div>
            </div>
            <img class="hidden-sm-and-down" style="border-radius: 6px;" :src="img" width="250px"></img>
        </div>
        <div v-else>
            <div class="d-flex flex-column align-center justify-center">
                <div class="d-flex align-center justify-space-between w-100">
                    <div class="d-flex flex-column px-4">
                        <div id="card-title">
                            <span class="text-h6">{{ title }}</span>
                        </div>
                        <div id="card-title">
                            <span class="text-caption">{{ date }}</span>
                        </div>
                    </div>
                    <img class="hidden-sm-and-down pa-2" style="border-radius: 12px;" :src="img" width="150px"></img>
                </div>
                <div id="card-text" class="px-4 py-2">
                    <span class="text-body-2">{{ description }}</span>
                </div>
            </div>
        </div>
    </v-card>
</template>
<script setup>
const props = defineProps({
    id: String,
    title: String,
    date: String,
    description: String,
    img: String,
    isLatest: Boolean
});
</script>
<style scoped>
.v-card {
    text-decoration: none !important;
}
</style>