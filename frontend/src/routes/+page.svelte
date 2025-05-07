<script lang="ts">
	let { data } = $props();

	type Todo = {
		id: number;
		text: string;
		updated: boolean;
	};

	type Theme = "dark" | "light"
	let theme: Theme = $state("dark")

	import Form from '../components/Form.svelte';

	let todos = $state<Todo[]>(data.todos);
	$inspect(todos, theme);

	let filteredTodos = $derived(todos)
</script>

{#snippet toggle(theme: Theme)}
	{#if theme=='dark'}
	<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26"><path fill="#FFF" fill-rule="evenodd" d="M13 21a1 1 0 011 1v3a1 1 0 11-2 0v-3a1 1 0 011-1zm-5.657-2.343a1 1 0 010 1.414l-2.121 2.121a1 1 0 01-1.414-1.414l2.12-2.121a1 1 0 011.415 0zm12.728 0l2.121 2.121a1 1 0 01-1.414 1.414l-2.121-2.12a1 1 0 011.414-1.415zM13 8a5 5 0 110 10 5 5 0 010-10zm12 4a1 1 0 110 2h-3a1 1 0 110-2h3zM4 12a1 1 0 110 2H1a1 1 0 110-2h3zm18.192-8.192a1 1 0 010 1.414l-2.12 2.121a1 1 0 01-1.415-1.414l2.121-2.121a1 1 0 011.414 0zm-16.97 0l2.121 2.12A1 1 0 015.93 7.344L3.808 5.222a1 1 0 011.414-1.414zM13 0a1 1 0 011 1v3a1 1 0 11-2 0V1a1 1 0 011-1z"/></svg>
	{:else}
	<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26"><path fill="#FFF" fill-rule="evenodd" d="M13 0c.81 0 1.603.074 2.373.216C10.593 1.199 7 5.43 7 10.5 7 16.299 11.701 21 17.5 21c2.996 0 5.7-1.255 7.613-3.268C23.22 22.572 18.51 26 13 26 5.82 26 0 20.18 0 13S5.82 0 13 0z"/></svg>
	{/if}
{/snippet}

<!-- grid stops at the value before the end value it seems -->
 <header class="header-wrapper">
	<h2>
		TODO
	</h2>

	<button onclick={() => theme = theme === "dark" ? "light" : "dark"}>
		{@render toggle(theme)}
	</button>
 </header>

<div class="form-wrapper">
	<Form />
</div>

<div class="empty-space"></div>

	<ul  class="list-wrapper w-full">
		{#each todos as { id, text, updated }, i (id)}
			<li class={['todo-item', { updated }]}>
				<input type="checkbox" bind:checked={todos[i].updated} />
				<span class="ml-[1em] w-[90%] cursor-pointer">{text}</span>
			</li>
		{/each}
	</ul>


<div class="actions">
	<p>{filteredTodos.length} items left</p>

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

	.header-wrapper{
		background: transparent;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		font-size: 32px;
		/* align-items: flex-start; iinvestigate why it only works on the svg*/
		
	}

	.form-wrapper, .actions{
		padding: 0.5em 1em;
	}

	.header-wrapper,
	.form-wrapper,
	.list-wrapper,
	.actions {
		&:not(.header-wrapper){
			background-color: var(--surface-1);
		}
		/* padding: 0.5em 1em; */
		color: var(--text-primary);
		font-weight: var(--light);
		button{
			&:hover{
				color: var(--bright-blue);
				cursor: pointer;
			}
		}
	}


</style>
