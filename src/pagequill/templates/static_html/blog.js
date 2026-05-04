async function loadPosts() {
  const response = await fetch("posts.json");
  const posts = await response.json();
  const root = document.querySelector("#posts");

  root.innerHTML = posts
    .map((post) => `<article><h2><a href="${post.url}">${post.title}</a></h2></article>`)
    .join("");
}

loadPosts();

