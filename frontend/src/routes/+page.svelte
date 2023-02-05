<script lang="ts">
	import { onMount } from "svelte";

	let results: any = [];

	onMount(async () => {
		const res = await fetch("https://randomuser.me/api/?results=500");
		const data = await res.json();
		results = data.results;
	});

	import logo from "$lib/images/logo.svg";

	import tomas from "$lib/images/tomas.jpg";
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section id="main">
	<div class="text">
		<h1 class="title"><span class="text-shadow">face.report</span></h1>
		<h2>Search the web for unwanted photographs</h2>
		<button>
			<a href="/finder"> Find Your Face </a>
		</button>
	</div>
	<div class="avatar">
		<img src={logo} alt="logo" width="300" height="300" />
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
	<div>
		<h1>The Problem</h1>
		<p>
			In today's technological landscape, it is not unlikely of to find unwanted
			pictures of oneself online. With the prevelance of social media as well
			the improvements of deepfake technology, malicious parties can fake images
			of anybody. This technology is often abused to humiliate and intimidate
			women. As the technology becomes more accurate and accessible, the issue
			only grows, requiring a soluton.
		</p>
	</div>
	<img src={tomas} alt="tom" width="300" height="300" />
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
	<h2>
		<center
			>Using image scraping and facial recognition, find yourself on the web,
			and look for malicious images
		</center>
	</h2>
	<button><a href="/finder">Find Your Face</a></button>
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
			animation-duration: 10s;
			animation-direction: alternate;
			animation-fill-mode: forwards;
			animation-iteration-count: infinite;
			animation-timing-function: linear;
		}

		.fast {
			height: 150px;
			width: 150px;
			animation-name: scrollSideways;
			animation-delay: 0;
			animation-duration: 10s;
			animation-fill-mode: forwards;
			animation-direction: alternate-reverse;
			animation-iteration-count: infinite;
			animation-timing-function: linear;
		}
	}
	@keyframes scrollSideways {
		from {
			transform: translateX(0);
		}
		to {
			transform: translateX(100vw);
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

	@keyframes float {
		0% {
			transform: translatey(15px);
		}
		50% {
			transform: translatey(-15px);
		}
		100% {
			transform: translatey(15px);
		}
	}

	.avatar {
		transform: translatey(0px);
		animation: float 6s ease-in-out infinite;
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
