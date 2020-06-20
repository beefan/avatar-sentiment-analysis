<template lang="pug">
  div#jumbo
    b-jumbotron(bg-variant="dark")
      template(v-slot:header) Avatar Sentiment Analysis
      img(src="@/assets/avatar-header.jpeg")
      template(v-slot:lead) python web scraping and natural language processing turned beautiful graphical representation of emotional arcs of Avatar: The Last Airbender and its characters
      hr.my-4
      b-button.btn(variant="success" href="/charts") View the Charts!
      b-button.btn(variant="info" href="/about") About the Project
</template>
<script>
export default {
  name: "Home"
};
</script>
<style lang="sass">
#jumbo
  color: #f8f8f8
  margin: 10%
  img
    border-radius: 3px
    max-width: 100%
.btn
  margin: 5%
</style>