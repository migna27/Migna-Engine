<script lang="ts">
  import { onMount } from 'svelte';

  let online = false;

  onMount(async () => {
    try {
      const response = await fetch('/api/health');
      if (response.ok) {
        online = true;
      }
    } catch (error) {
      console.error('Health check failed:', error);
    }
  });
</script>

{#if online}
  <div class="flex items-center space-x-2">
    <span class="relative flex h-3 w-3">
      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
      <span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
    </span>
    <span>Online</span>
  </div>
{:else}
    <div class="flex items-center space-x-2">
        <span class="relative flex h-3 w-3">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-3 w-3 bg-red-500"></span>
        </span>
        <span>Offline</span>
    </div>
{/if}
