<template>
    <nav-bar></nav-bar>
    <div id="body">
        <slot />
    </div>
    <blog-footer></blog-footer>
</template>
<style scoped>
#body {
    width: 100vw;
    max-width: 50rem;
    min-height: calc(100vh - 6rem);
    margin: 0 auto;
}
</style>