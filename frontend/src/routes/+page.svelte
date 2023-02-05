<script lang="ts">
	import { onMount } from "svelte";

	let results: any = [];

	onMount(async () => {
		const res = await fetch("https://randomuser.me/api/?results=500");
		const data = await res.json();
		results = data.results;
	});
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section id="main">
	<div class="text">
		<h1 class="title"><span class="text-shadow">face.report</span></h1>
		<h2>Search the web for unwanted photographs</h2>
		<button>Find Your Face</button>
	</div>
	<div>
		<iframe
			title="thing"
			src="https://giphy.com/embed/mcsPU3SkKrYDdW3aAU"
			width="300"
			height="300"
			frameBorder="0"
		/>
	</div>
</section>

<div class="stripe">
	<div style="background-color:#5B7E8D;">&nbsp</div>
	<div style="background-color:#587484;">&nbsp</div>
	<div style="background-color:#546A7B;">&nbsp</div>
</div>

<section id="quote">
	<h1>
		“No man is good enough to govern any woman without her <span
			style="color: #87CEEB"><span class="text-shadow">consent</span></span
		>”
	</h1>
	<h2><center>Susan B. Anthony</center></h2>
</section>

<section id="problem">
	<h1>The Problem</h1>
	<p>
		In today's technological landscape, it is not unlikely of to find unwanted
		pictures of oneself online. With the prevelance of social media as well the
		advacements of deepfake technology, malicious parties can fake images of
		anybody. This creates an especially hostile environment for women, who often
		find themselves as the target of this new digital harrasment. this is a test
	</p>
</section>

<section id="protect">
	<div class="scroll-container">
		<h1>Protect Your</h1>
		<div class="scroll-list">
			<ul>
				<li class="scroll-item"><span class="text-shadow">Identity</span></li>
				<li class="scroll-item"><span class="text-shadow">Life</span></li>
				<li class="scroll-item"><span class="text-shadow">Pictures</span></li>
			</ul>
		</div>
	</div>
	<h2>
		<center>
			Safeguard Your <span style="color: #87CEEB">Identity</span> &nbsp &nbsp
			&nbsp Find <span style="color: #87CEEB">Non-Consensual</span> Pictures
			&nbsp &nbsp &nbsp <span style="color: #87CEEB">Report</span> Pictures
		</center>
	</h2>
	<div class="complete-gallery">
		<div class="gallery">
			{#each results as item, index (item.id)}
				<img class="slow" src={item.picture.large} alt={item.id.toString()} />
			{/each}
		</div>
		<div class="gallery">
			{#each results as item, index (item.id)}
				<img class="fast" src={item.picture.large} alt={item.id.toString()} />
			{/each}
		</div>
	</div>
</section>

<section id="future">
	<h1><center>The future of privacy is in your hands</center></h1>
	<h2><center>Keep the web free of invasive pictures</center></h2>
	<button>Find Your Face</button>
</section>

<style lang="scss">
	#main {
		height: 90vh;
		width: 100%;
		width: 100%;
		display: flex;
		justify-content: space-around;
		align-items: center;
	}
	#main .title {
		font-size: 70px;
		margin: 0;
		padding: 0;
	}
	#main h2 {
		width: 70%;
	}

	#quote {
		display: flex;
		align-items: center;
		flex-direction: column;
		justify-content: center;
		height: 40vh;
	}

	#quote h1 {
		text-align: center;
		width: 80%;
	}

	#problem {
		height: 50vh;
		display: flex;
		justify-content: center;
		align-items: flex-start;
		flex-direction: column;
	}

	#problem p {
		color: white;
		width: 70%;
		font-weight: 400;
		font-size: 1.2rem;
	}

	#protect {
		height: 60vh;
		display: flex;
		align-items: center;
		flex-direction: column;
		overflow: hidden;
	}

	.complete-gallery {
		margin-top: 50px;
	}

	.gallery {
		display: flex;
		filter: grayscale(100%);

		.slow {
			height: 100px;
			width: 100px;
			animation-name: scrollSideways;
			animation-duration: 15s;
			animation-iteration-count: infinite;
			animation-timing-function: linear;
		}
		.medium {
			height: 100px;
			width: 100px;
			animation-name: scrollSideways;
			animation-duration: 20s;
			animation-iteration-count: infinite;
			animation-timing-function: linear;
		}

		.fast {
			height: 150px;
			width: 150px;
			animation-name: scrollOtherSideways;
			animation-duration: 8s;
			animation-iteration-count: infinite;
			animation-timing-function: linear;
		}
	}
	@keyframes scrollSideways {
		0% {
			transform: translateX(0);
		}
		100% {
			transform: translateX(100vw);
		}
	}

	@keyframes scrollOtherSideways {
		0% {
			transform: translateX(0);
		}
		100% {
			transform: translateX(-100vw);
		}
	}

	#protect h1 {
		font-size: 45px;
	}
	.scroll-container {
		display: flex;
		align-items: center;
		font-size: 2rem;
		font-weight: 600;
		font-size: 45px;
	}

	.scroll-list {
		height: 3rem;
		overflow: hidden;
	}

	.scroll-list ul {
		margin: 0 0.625rem;
		padding: 0;
		animation: scrollUp 4s infinite;
	}

	.scroll-list ul li {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		height: 3rem;
		list-style: none;
		color: var(--color-bg-1);
	}

	$item-count: 3;
	@keyframes scrollUp {
		@for $i from 1 through (2) {
			#{($i * 25) - 10%},
			#{$i * 25%} {
				transform: translateY(calc(-100% / 3) * $i);
			}
		}
	}

	.text-shadow {
		text-shadow: #517789 5px 5px;
	}

	.stripe {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		grid-template-rows: 8px 8px 8px;
	}

	#future {
		height: 35vh;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	h1 {
		color: #ffff;
		justify-content: left;
		font-size: 45px;
		text-align: left;
		font-weight: bold;
		padding: 0;
		margin: 0;
	}

	h2 {
		color: #ffff;
		justify-content: left;
		font-size: 20px;
		text-align: left;
	}

	button {
		display: flex;
		outline: none;
		border: none;
		font-size: 20px;
		color: var(--color-bg-0);
		font-weight: bold;
		border-radius: 10px;
		padding: 20px;
		align-items: center;
		justify-content: center;
		background-color: var(--color-bg-1);
	}

	button:hover {
		filter: brightness(80%);
	}
</style>
