<template>
    <v-container fluid id="landing" v-if="posts?.length">
        <v-row class="mt-3">
            <v-col cols="12" class="d-flex justify-center">
                <blog-card :title="latest.title" :date="latest.date" :description="latest.description" :img="latest.img"
                    :is-latest="true" :id="latest.id"></blog-card>
            </v-col>
        </v-row>
        <v-row :gap="10">
            <v-col v-for="post of posts" cols="12" md="6" class="">
                <blog-card :title="post.title" :date="post.date" :description="post.description" :img="post.img"
                    :is-latest="false" :id="post.id"></blog-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script setup>
const latest = ref({});
const posts = ref([]);
onMounted(async () => {
    await useFetch('/data/posts.json').then((response) => {
        const data = response.data.value;
        if (data) {
            latest.value = data[0];
            posts.value = data.slice(1);
        }
    })
})
</script>