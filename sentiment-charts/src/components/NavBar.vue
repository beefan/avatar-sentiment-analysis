<template>
<div id="nav">
  <b-navbar toggleable="sm" type="dark" variant="dark">
    <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>

    <b-navbar-brand to="/">Avatar Sentiment Analysis</b-navbar-brand>

    <b-collapse id="nav-text-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/charts">Charts</b-nav-item>
        <b-nav-item to="/about">About</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
<style lang="sass">
#nav 
  a 
    color: #f8f8f8
  a:hover
    opacity: 60%
  .router-link-exact-active 
      color: #76b583
      font-weight: bold
</style>