<template>
    <v-container fluid class="px-3 mt-5">
        <v-row>
            <v-col cols="12">
                <div class="d-flex flex-column ga-1">
                    <span class="text-h5">{{ meta?.title }}</span>
                    <span class="text-body-2">By {{ meta?.author }}</span>
                    <span class="text-caption">{{ meta?.date }}</span>
                </div>
            </v-col>
        </v-row>
        <v-row class="mt-0">
            <v-col cols="12">
                <div class="d-flex flex-column ga-5" v-html="text"></div>
            </v-col>
        </v-row>
    </v-container>
</template>
<script setup>
const route = useRoute();
const pageId = route.params.id;
const meta = ref({});
const text = ref("");
await useFetch(`/posts/${pageId}/meta.json`).then(({ data, status }) => {
    if (!data.value?.title) {
        throw createError({
            status: 404,
            statusText: 'Post not found',
            message: 'This post probably does not exist. Weird...',
            fatal: true
        })
    }
    meta.value = data.value;
})
await useFetch(`/posts/${pageId}/p.txt`).then(({ data, error }) => {
    if (error.value) {
        // throw to error.vue
        return
    }
    const chunks = data.value.split("\n");
    let t = "";
    for (const chunk of chunks) {
        if (chunk.slice(0, 3) === 'img') {
            t += createImageTag(chunk);
        } else if (chunk) {
            t += `<span class="text-body-1">${chunk.replace("{END}", "&#9724;")}</span>`
        }
    }
    text.value = t;
});

function createImageTag(t) {
    const attrs = t.split(";");
    const obj = {};
    for (const attr of attrs) {
        const [key, value] = attr.split("=");
        obj[key] = value;
    }
    return `<div class="d-flex flex-column ga-1 justify-center align-center"><img src="${obj.img}" width=${obj.size}/><span class="text-caption">${obj.caption}</span></div>`
}
</script>