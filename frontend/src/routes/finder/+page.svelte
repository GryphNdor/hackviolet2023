<script lang="ts">
  import FaCamera from "svelte-icons/fa/FaCamera.svelte";

  import { clicked } from "./clicked";

  let name = "";
  let input = document.querySelector('input[type="file"]');

  async function postData() {
    let data = new FormData();
    data.append("file", input.files[0]);
    data.append("name", name);
    const res = await fetch("http://127.0.0.1:5000/submit", {
      method: "POST",
      mode: "cors",
      body: data,
    });
    console.log(res.body);
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
    <div use:clicked class="photo">
      <div class="camera">
        <FaCamera />
      </div>
    </div>
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

<style lang="scss">
  #title {
    height: 30vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }

  #submission {
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  input[type="file"] {
    opacity: 0;
  }

  label {
    color: white;
    text-align: center;
    padding: 5px;
  }

  .textinput {
    display: flex;
    flex-direction: column;
  }

  input[type="text"] {
    width: 300px;
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
