<script lang="js">
  import FaCamera from "svelte-icons/fa/FaCamera.svelte";
  import FaCheckCircle from "svelte-icons/fa/FaCheckCircle.svelte";
  import { clicked } from "./clicked";

  let name = "";

  let images = [];

  export let previewImg;

  let uploaded = false;
  let fetched = false;

  async function postData() {
    let data = new FormData();
    let input = document.querySelector('input[type="file"]');
    if (input) {
      data.append("file", input.files[0]);
      data.append("name", name);
    }
    const res = await fetch("http://127.0.0.1:5000/submit", {
      method: "POST",
      mode: "cors",
      body: data,
    });
    let disp = await res.json();

    for (let key of Object.keys(disp)) {
      images.push({ url: key, val: disp[key] });
    }

    fetched = true;
  }
</script>

<svelte:head>
  <title>Finder</title>
  <meta name="description" content="About this app" />
</svelte:head>

<div id="problem" />
<div id="future" />

<section id="title">
  <h1>Find My Face</h1>
  <p>
    Enter in <span>Your Name</span> and a <span>Photo</span> of yourself to see if
    there are malicious photos of you on the internet
  </p>
</section>

<section id="submission">
  {#if fetched == false}
    <form id="myform" on:submit={postData}>
      <div use:clicked on:click={() => (uploaded = true)} class="photo">
        <img id="preview" />
      </div>
      <h1 class="documentID" />
      <input id="upload" type="file" accept="image/jpeg" />
      <div class="textinput">
        <label for="textbox">Your Name</label>
        <input
          on:input={(e) => (name = e.currentTarget.value)}
          id="textbox"
          type="text"
        />
      </div>
    </form>
    <button form="myform" type="submit">Submit</button>
  {:else}
    <div class="grid-container">
      <!--do not read without headache meds-->
      {#each images as image, index}
        <div class={image.val === "true\n" ? "true" : "false"}>
          <img src={image.url} />
        </div>
      {/each}
    </div>
    <button
      on:click={() => {
        images = [];
        fetched = false;
      }}>Reset</button
    >
  {/if}
</section>

<style lang="scss">
  #title {
    height: 20vh;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-direction: column;
    text-align: center;
  }

  #submission {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }

  button {
    display: inline-block;
    padding: 0.75rem 1.25rem;
    border-radius: 10px;
    margin-top: 10px;
    color: var(--color-bg-0);
    border: none;
    text-transform: uppercase;
    font-weight: bold;
    font-size: 1rem;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
    z-index: 1;
    &:after {
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: #87ceeb;
      border-radius: 10px;
      z-index: -2;
    }
    &:before {
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0%;
      height: 100%;
      background-color: darken(#87ceeb, 15%);
      transition: all 0.3s;
      border-radius: 10px;
      z-index: -1;
    }
    &:hover {
      color: #fff;
      &:before {
        width: 100%;
      }
    }
  }

  .grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-radius: 15px;
    gap: 10px;
    margin-top: 50px;
  }

  .grid-container > div {
    display: flex;
    padding: 10px;
    justify-content: space-around;
    align-items: center;
    font-size: 25px;
    height: 200px;
    color: #000;
    border-radius: 15px;
    filter: drop-shadow(0px 2px 2px rgba(0, 0, 0, 0.25));

    img {
      border-radius: 5px;
      max-width: 120px;
      max-height: 120px;
    }
  }

  label {
    color: white;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    padding: 5px;
  }

  .textinput {
    display: flex;
    flex-direction: column;
  }

  .true {
    background-color: green;
  }
  .false {
    background-color: red;
  }

  input[type="text"] {
    width: 300px;
    border: none;
    outline: none;
    height: 30px;
    padding: 6px 10px;
    border: 20px, var(--color-bg-1);
    border-radius: 10px;
  }

  .photo {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 300px;
    height: 300px;
    border: 5px dashed white;
    border-radius: 20px;
    img {
      width: 300px;
      height: 300px;
      z-index: 1;
    }
  }

  .camera {
    height: 75px;
    width: 75px;
    color: white;
  }

  h1 {
    color: #ffff;
    font-size: 45px;
    font-weight: bold;
    padding: 0;
    margin: 0;
  }

  p {
    color: white;
  }
  span {
    color: var(--color-bg-1);
  }
</style>
