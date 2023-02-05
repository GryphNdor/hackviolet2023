export function clicked(node: any) {
  let upload = document.getElementById("upload")
  const handleClick = (e: any) => {
    if (node.contains(e.target)) {
      node.dispatchEvent(new CustomEvent("outclick"));
      upload?.click()
    }
  }
  document.addEventListener("click", handleClick, true);
  return {
    destroy() {
      document.removeEventListener("click", handleClick, true);
    },
  };

}