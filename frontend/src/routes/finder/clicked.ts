
export function clicked(node: any) {
  let upload = document.getElementById("upload")
  const handleClick = (e: any) => {
    if (node.contains(e.target)) {
      node.dispatchEvent(new CustomEvent("outclick"));
      upload?.click()

    }
  }

  let preview = document.getElementById('preview');
  (<HTMLImageElement>preview).src = URL.createObjectURL(upload?.files[0]);
  document.getElementById("preview").contentWindow.location.reload(true);



  document.addEventListener("click", handleClick, true);
  return {
    destroy() {
      document.removeEventListener("click", handleClick, true);
    },
  };

}