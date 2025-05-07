<script lang="ts">
	import '../app.css';

	let { children } = $props();

	// type ThemeS = {

	// }
</script>

<!-- set the proper colors after  -->
<div class="container">
	<div class="wrapper">
		{@render children()}
	</div>
</div>

<style>
	:global(body::before) {
		content:'';
		height: 100vh;
		width: 100%;
		position: fixed;
		z-index: -1;
		top: 0;
		left: 0;
		/* inset: 0; */
		background-image: var(--background-img), linear-gradient(to bottom, var(--background-color));
		background-repeat: no-repeat, no-repeat;
		object-fit: cover;
		background-position: top, top;
		background-size: 100% auto, 100% 100%;
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
			max-width: 480px;
			/* min-height: 200px; */
			grid-template-rows: 1.5fr 1fr 12px auto 1fr;
			/* grid-template-columns: repeat(3, 1fr); */
			/* border: 1px solid black; */
			/* background: linear-gradient(#222, #444); */
		}
	}
</style>
