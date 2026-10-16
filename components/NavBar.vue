<template>
    <div id="nav"
        class="d-flex flex-column flex-sm-row justify-center justify-sm-space-between align-center py-3 px-3 flex-wrap ga-2"
        style="max-width: 50rem; margin: 0 auto;">
        <nuxt-link style="text-decoration: none; text-align: center;" class="text-h3" to="/">Matthew Gilmore<span
                class="text-h5">'s
                blog</span></nuxt-link>
        <div class="d-flex ga-6">
            <nuxt-link class="text-body-1" v-for="item of menu" :to="item.path">{{ item.title
                }}</nuxt-link>
        </div>
    </div>
    <v-divider></v-divider>
</template>
<script setup>
const menu = [
    {
        title: "Photography",
        path: "/photography"
    },
    {
        title: "Contact",
        path: "/contact"
    },
]
</script>