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
                <div id="post" class="d-flex flex-column ga-5" v-html="text"></div>
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
    let footnote = 1;
    for (const chunk of chunks) {
        if (chunk.slice(0, 4) === 'img#') {
            t += createTag(chunk, 'img');
        } else if (chunk.slice(0, 9) === 'footnote#') {
            t += createTag(chunk, 'footnote');
        }
        else if (chunk) {
            let tChunk = chunk.replace("{END}", "&#9724;");
            while (tChunk.includes("FOOTNOTE")) {
                tChunk = tChunk.replace("FOOTNOTE", `<sup><a id="footnote-${footnote}" href="#footnote-${footnote}-text" style="text-decoration: none !important;">${footnote}</a></sup>`);
                footnote++;
            }
            t += `<span class="text-body-1">${tChunk}</span>`
        }
    }
    text.value = t;
});

function createTag(t, tagType) {
    const attrs = t.split(";");
    const obj = {};
    for (const attr of attrs) {
        const [key, value] = attr.split("#");
        obj[key] = value;
    }
    if (tagType === 'img') {
        return `<div class="d-flex flex-column ga-1 justify-center align-center"><img src="${obj.img}" width=${obj.size}/><span class="text-caption">${obj.caption}</span></div>`;
    } else if (tagType === 'footnote') {
        return `<span class="text-caption" id="footnote-${obj.num}-text"><a href="#footnote-${obj.num}">${obj.num}.</a> ${obj.footnote}</span>`
    }
}

</script>
<style scoped>
#post :deep(a) {
    text-decoration: underline !important;
}
</style>