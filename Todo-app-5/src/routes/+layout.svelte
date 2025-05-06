<script lang="ts">
	import '../app.css';

	let { children } = $props();

	// type ThemeS = {

	// }
</script>

<!-- set the proper colors after  -->
<div class="container">
	<div class="wrapper px-4 py-2">
		{@render children()}
	</div>
</div>

<style>
	:global(body) {
		background: linear-gradient(hsl(192, 100%, 67%) to hsl(280, 87%, 65%));
		background-attachment: fixed;
		background-position: top;
		font-size: 18px;
	}

	.container {
		height: 100%;
		width: 100%;
		place-content: center;
		position: relative;
		margin: 0 auto;
		.wrapper {
			display: grid;
			margin: 0 auto;
			max-width: 440px;
			min-height: 200px;
			grid-template-rows: 1fr 12px auto 1fr;
			/* grid-template-columns: repeat(3, 1fr); */
			border: 1px solid black;
			background: linear-gradient(#222, #444);
		}
	}
</style>
