function changeTheme() {
  const body = document.querySelector("body");
  body.style.backgroundColor =
    body.style.backgroundColor === "black" ? "#efefef" : "black";
  body.style.color = body.style.color === "white" ? "black" : "white";
  const nav = document.querySelector("nav ul");
  nav.style.color = nav.style.color === "#333" ? "white" : "#333";
}

let postData;
window.onload = function () {
  fetch("/run-script")
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        postData = data.data;
        console.log(postData);

        const container = document.querySelector(".posting-container"); // 이 위치에 포스트 카드들을 추가합니다. 와우, posting-card는 클래스라서 앞에 점을 붙여줘야 한대요
        //궁금증 : 이게 서버사이드 렌더링(서버에서 html 만들어서 클라이언트에 전달하는 개념)이라서 이렇게 html로 map 돌려서 html 텍스트 자체를 다 만들어놓고 한번에 렌더링 시키는 게 더 나은 게 맞는 건가? 보통 리액트 사용할 때는 클라이언트 측에서 맵 돌리면서 한 컴포넌트 씩 화면에 만들어내는 거고...? 그래서 csr이 로딩 걸리면서 하나씩 천천히 생겨나고, ssr은 한 번에 빵 하고 나타나고...?
        postData.forEach((post) => {
          const cardHTML = `
          <div class="posting-card">

                <a href="https://velog.io${post["post_url"]}" class="post-url">
                    <img src="${post["thumbnail_url"]}" alt="썸네일" class="thumbnail-url" />
                </a>
                <h4 class="title">${post["title"]}</h4>
                <div class="description-wrapper">
                    <p class="description">${post["description"]}</p>
                </div>
                <div class="sub-info">
                    <span class="date">${post["date"]}</span>
                    <span>|</span>
                    <span class="comment-count">댓글: ${post["comment_count"]}개</span>
                </div>
                <a href="#" class="userinfo">
                    <img src="${post["author_profile_url"]}" alt="작성자 프로필" class="author-profile-url" />
                    <b class="author-name">${post["author_name"]}</b>
                </a>
                <div class="likes">${post["likes"]} 좋아요</div>
              </div>
        `;

          container.insertAdjacentHTML("beforeend", cardHTML);
        });
      }
    });
};
