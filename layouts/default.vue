<template>
    <div id="nav" class="d-flex py-3 justify-space-between w-100 align-center"
        style="max-width: 80rem; margin: 0 auto;">
        <nuxt-link id="nav-name" class="text-h4" to="/">Matthew Gilmore</nuxt-link>
        <div class="d-flex ga-6">
            <nuxt-link v-for="item of menu" :to="item.path">{{ item.title }}</nuxt-link>
        </div>
    </div>
    <div id="body">
        <slot />
    </div>
    <v-footer>Footer!</v-footer>
</template>
<script setup>
const menu = [
    {
        title: "Writing",
        path: "/writing"
    },
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
<style scoped>
#nav-name {
    text-decoration: none;
}

#body {
    width: 100vw;
    max-width: 80rem;
    min-height: calc(100vh - 13.7rem);
    margin: 0 auto;
}
</style>