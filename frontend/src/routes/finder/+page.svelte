<script lang="ts">
  import FaCamera from "svelte-icons/fa/FaCamera.svelte";
  import FaCheckCircle from "svelte-icons/fa/FaCheckCircle.svelte";
  import { clicked } from "./clicked";

  let name = "";

  let uploaded = false;

  async function postData() {
    let data = new FormData();
    let input = document.querySelector('input[type="file"]');
    data.append("file", input.files[0]);
    data.append("name", name);
    const res = await fetch("http://127.0.0.1:5000/submit", {
      method: "POST",
      mode: "cors",
      body: data,
    });
    let disp = await res.json();
    console.log(disp.response);
  }
</script>

<svelte:head>
  <title>Finder</title>
  <meta name="description" content="About this app" />
</svelte:head>

<section id="title">
  <h1>Find My Face</h1>
  <p>
    Enter in <span>Your Name</span> and a <span>Photo</span> of yourself to see if
    there are malicious photos of you on the internet
  </p>
</section>

<section id="submission">
  <form id="myform" on:submit={postData}>
    <div use:clicked on:click={() => (uploaded = true)} class="photo">
      {#if uploaded}
        <div class="camera" style="color:green">
          <FaCheckCircle />
        </div>
      {:else}
        <div class="camera">
          <FaCamera />
        </div>
      {/if}
    </div>
    <h1 class="documentID" />
    <input
      on:change={(e) => (image = e.currentTarget.files)}
      id="upload"
      type="file"
      accept="image/jpeg"
    />
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
</section>

<section>
  <!--do not read without headache meds-->
  <div class="item1">
    <img style="border-radius:15px;" width="300" height="300" />
  </div>
</section>

<style lang="scss">
  #title {
    height: 30vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
  }

  #submission {
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  input[type="file"] {
    opacity: 0;
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
    grid-template-areas: "box1 box2";
    gap: 70px;
    background-color: var(--color-bg-1);
    padding-left: 80px;
    padding-right: 90px;
    padding-bottom: 30px;
    border-radius: 15px;
  }

  .grid-container > div {
    background-color: var(--color-bg-0);
    text-align: left;
    padding-top: 30px;
    padding-right: 30px;
    padding-bottom: 30px;
    padding-left: 30px;
    font-size: 25px;
    color: #ffff;
    border-radius: 15px;
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
