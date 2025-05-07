<script lang="ts">
</script>

{#snippet checkmark()}
	<svg xmlns="http://www.w3.org/2000/svg" width="11" height="9"
		><path fill="none" stroke="#FFF" stroke-width="2" d="M1 4.304L3.696 7l6-6" /></svg
	>
{/snippet}

<form class="flex w-full flex-row items-center justify-start">
	<input type="checkbox" />
	<!-- {@render checkmark()}<input> -->
	<input type="text" placeholder="Create a new todo..." />
</form>

<style>
	/* make the input styles global later */

	/* label {
        
    } */
</style>
