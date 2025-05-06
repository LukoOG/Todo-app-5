<script lang="ts">
	let { data } = $props();

	type Todo = {
		id: number;
		text: string;
		updated: boolean;
	};

	import Form from '../components/Form.svelte';

	let todos = $state<Todo[]>(data.todos);
</script>

<!-- grid stops at the value before the end value it seems -->
<div class="form-wrapper">
	<Form />
</div>

<div class="empty-space"></div>

<div class="list-wrapper">
	<ul>
		{#each todos as { id, text, updated }, i (id)}
			<li class={['list-item', { updated }]}>
				<input type="checkbox" bind:checked={todos[i].updated} />
				<span>{text}</span>
			</li>
		{/each}
	</ul>
</div>

<div class="actions">
	<p>no of items left</p>

	<div class="filters">
		<button>All</button>
		<button>Active</button>
		<button>Completed</button>
	</div>

	<button> Clear completed </button>
</div>

<style>
	.filters {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		margin: 0 auto;
		width: 70%;
		flex-basis: content;
	}
</style>
