<script>
  let { speaker, sentence } = $props();
</script>

<div class="sentence-box {speaker}">
  <pre>{sentence}</pre>
</div>

<style>
  .sentence-box {
    padding: 8px;
    margin: 8px;
    border-radius: 4px;
    line-height: 1.5;
  }
  .user {
    background-color: var(--gray-700);
    font-weight: bold;
  }
  .loading {
    animation: fadeAnimation 1.5s infinite alternate;
  }

  @keyframes fadeAnimation {
    0% {
      opacity: 0.2;
    }
    100% {
      opacity: 0.8;
    }
  }
</style>
