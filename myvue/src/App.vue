<template>
  <div id="app">
      <section class="container grid-960">
          <div class="columns">
              <div class="column col-2"></div>
              <div class="column col-8 col-md-12">
                  <header class="text-center">
                      <h2>Create note</h2>
                  </header>
                  <create-note></create-note>
                  <header class="text-center">
                      <h2>List of notes</h2>
                  </header>
                  <note-list></note-list>
              </div>
              <div class="column col-2"></div>
          </div>
      </section>
  </div>
</template>

<script>
import CreateNote from './components/CreateNote'
import NoteList from './components/NoteList'
export default {
  name: 'app',
  components: {
    'create-note': CreateNote,
    'note-list': NoteList
  }
}
</script>

<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);
  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
