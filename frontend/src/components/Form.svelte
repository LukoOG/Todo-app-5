<script lang="ts">
	let { handleSubmit, text, id } = $props()
</script>

<form class="flex w-full flex-row items-center justify-start" onsubmit={(e)=>handleSubmit(e, id)}>
	<input type="checkbox" />
	<input type="text" value={text} placeholder="Create a new todo..." />
</form>

<style>
	/* make the input styles global later */

	/* label {
        
    } */
</style>
