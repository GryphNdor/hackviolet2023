<script lang="ts">
  import FaCamera from "svelte-icons/fa/FaCamera.svelte";
  import FaCheckCircle from "svelte-icons/fa/FaCheckCircle.svelte";
  import { clicked } from "./clicked";

  let name = "";

  let images: string[] = ["a", "b", "b", "a", "b", "b"];

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
  {#if images.length == 0}
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
  {:else}
    <div class="grid-container">
      <!--do not read without headache meds-->
      {#each images as image, index}
        <div class="item1">
          <div>
            <h4>images.title</h4>
            <h5>Found?</h5>
          </div>
          <img
            src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F1f%2F62%2F96%2F1f629677804018c02f9e4369aace6012.jpg&f=1&nofb=1&ipt=41925177dc0d4fe12b118e825ec7f8a5cd39958241aa98205a7805f27609c3f5&ipo=images"
          />
        </div>
      {/each}
    </div>
    <button on:click={() => (images = [])}>Reset</button>
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
    grid-template-columns: repeat(3, 1fr);
    border-radius: 15px;
    gap: 10px;
    margin-top: 50px;
  }

  .grid-container > div {
    background-color: lightgray;
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
