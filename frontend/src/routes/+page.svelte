<script lang="ts">
	let { data } = $props();

	type Todo = {
		id: number;
		text: string;
		completed: boolean;
	};
	type todoState = "active" | "all" | "completed"

	type Theme = "dark" | "light"
	let theme: Theme = $state("dark")

	import Form from '../components/Form.svelte';
	// will hook up backend soon
	// let todos = $state<Todo[]>(data.todos);
	let todos =$state<Todo[]>([
		{ id: 188, text: 'get into Caltech', completed: true },
		{ id: 189, text: 'go eat some pizza', completed: true },
		{ id: 193, text: 'migrate to svelte-5', completed: false }
	])
	let todostate = $state<todoState>("all")
	
	let filteredTodos = $derived.by(() => {
		switch (todostate){
			case "all":
				return todos
			case 'active':
				return todos.filter((todo)=>todo.completed === false)
			case 'completed':
				return todos.filter((todo)=>todo.completed === true)
		}

	})

	let editing = $state({})
	const handleSubmit = (e: Event, id:number) => {
		e.preventDefault()
		let inputEl = e.target.elements[1] as HTMLInputElement
		if(!id){
			addTodo(inputEl.value)
			inputEl.value = ""
		} else if(id){
			editTodo(id, inputEl.value)
			inputEl.value = ""
			editing = {}
		}

	}

	const addTodo = (value: string) => {
		if(!value) return;
		let newTodo: Todo = {
			id: Math.random(), //will change on the backend
			text: value,
			completed: false,
		}
		todos.push(newTodo)
		todostate="all"
	}

	const removeTodo = (id: number) => {
		todos = todos.filter((todo)=>todo.id !== id)
	}

	const editTodo = (id: number, text: string) => {
		todos = todos.map((todo)=>{
			if (todo.id == id){
				todo.text = text
			}
			return todo
		})
	}

	const clearCompleted = () => {
		todos = todos.filter((todo)=>todo.completed == false)
	}

	const toggleTheme = () => {
		theme = theme == "dark" ? "light" : "dark"
		document.body.setAttribute('data-theme', theme)
	}
	$inspect(filteredTodos)
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

	<button onclick={toggleTheme}>
		{@render toggle(theme)}
	</button>
 </header>

<div class="form-wrapper">
	<Form { handleSubmit } {...editing} />
</div>

<div class="empty-space"></div>

	<ul  class="list-wrapper w-full">
		{#each filteredTodos as { id, text, completed }, i (id)}
			<li class={['todo-item', { completed }]}>
				<input type="checkbox" bind:checked={filteredTodos[i].completed} />
				<!-- ignore velte(a11y_click_events_have_key_events) -->
				<!-- ignore svelte(a11y_no_static_element_interactions) -->
				<span onclick={()=>editing={id, text}} class="ml-[1em] w-[90%] cursor-pointer">{text}</span>
				<!-- <input class="ml-[1em] w-[90%] cursor-pointer" value={text}  readonly> -->
				<button onclick={()=>removeTodo(id)}>
					<!--ignore svelte(a11y_consider_explicit_label) -->
					<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"><path fill="#494C6B" fill-rule="evenodd" d="M16.97 0l.708.707L9.546 8.84l8.132 8.132-.707.707-8.132-8.132-8.132 8.132L0 16.97l8.132-8.132L0 .707.707 0 8.84 8.132 16.971 0z"/></svg>
				</button>
			</li>
		{/each}
	</ul>


<div class="actions">
	{#snippet completed()}
		{@const length = filteredTodos.filter((todo)=>todo.completed==false).length}
		{@const completed = filteredTodos.filter((todo)=>todo.completed==true).length}
		{@const state = todostate}
		{#if state !== 'completed'}
			<p>{length} { length == 1 ? "item" : "items" } left</p>
		{:else if state == 'completed'}
			<p class=''>{completed} { completed == 1 ? "item" : "items" } completed</p>
		{/if}
	{/snippet}

	{@render completed()}

	

	<div class="filters">
		{#each ["all", "active", "completed"] as state }
		{@const capitalWord = state.charAt(0).toUpperCase() + state.slice(1) }
		{@const current =  state == todostate ? "page" : undefined}
			<button aria-current={current} onclick={()=>todostate =  state as todoState }>{ capitalWord }</button>
		{/each}
	</div>

	<button onclick={clearCompleted}> Clear completed </button>
</div>

<style>
	.filters {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		margin: 0 auto;
		width: 70%;
		flex-basis:auto;
	}

	.header-wrapper{
		background: transparent;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		font-size: 32px;
		/* align-items: flex-start; investigate why it only works on the svg*/
		align-items: center;
		color: var(--very-light-gray);
		font-weight: 600px;
		
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
			color: var(--text-secondary);
		}

		&:not(.list-wrapper){
			font-weight: 600;
		}
		/* padding: 0.5em 1em; */
		button{
			color: var(--button-primary);
			&:hover{
				color: var(--button-hover);
				cursor: pointer;
			}
			&[aria-current="page"]{
				color: var(--bright-blue);

			}
		}
	}


</style>
