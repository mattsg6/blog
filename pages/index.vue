<template>
    <v-container fluid id="landing">
        <v-row>
            <v-col cols="12 pt-10 pb-5 d-flex justify-center">
                <span class="text-h5">This is my blog. Thanks for coming.</span>
            </v-col>
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
const { data } = await useFetch('/data/posts.json');
const latest = computed(() => data.value[0]);
const posts = computed(() => {
    if (data.value?.length > 1) {
        return data.value.slice(1)
    }
    return []
})
</script>